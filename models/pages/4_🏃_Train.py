import streamlit as st
import cv2
from cvzone.PoseModule import PoseDetector
import math
import numpy as np
import plotly.graph_objects as go
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ---- HEADER SECTION ----
css_styles = """
    <style>
    .header-container {
        background-color: #9C0000;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        animation: fadeIn 2s ease-in-out;
    }
    .header-container h1 {
        color: #FFFFFF;
        font-size: 48px;
        margin: 0;
        animation: slideInFromLeft 1.5s ease-in-out;
    }
    .header-container p {
        color: #FFFFFF;
        font-size: 24px;
        animation: slideInFromRight 1.5s ease-in-out;
    }

    /* Adjust margin between header and content */
    .content-container {
        margin-top: 50px;
    }
    
    /* Animation Keyframes */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideInFromLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideInFromRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    </style>
"""

# Apply the CSS styles
st.markdown(css_styles, unsafe_allow_html=True)

# Header for the Train page
header_html = """
    <div class="header-container">
        <h1>Train Here</h1>
        <p>Unleash your potential and power with our dynamic training sessions</p>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# ---- SPACE ADJUSTMENT FOR CONTENT ----
st.markdown('<div class="content-container"></div>', unsafe_allow_html=True)

def main():
    app_mode = st.sidebar.selectbox("Choose the exercise", 
                                    ["About", "Left Dumbbell", "Right Dumbbell", "Squats", "Pushups", "Shoulder press"])

    if app_mode == "About":
        about_page()
    elif app_mode in ["Left Dumbbell", "Right Dumbbell", "Squats", "Pushups", "Shoulder press"]:
        exercise_page(app_mode)

def about_page():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Welcome to the Training arena")
        st.markdown("Choose the workout you wish to do from the sidebar")
        st.write("##")
        st.write("""
        Here are few general instructions to follow while doing the workout:

        - It is necessary for you to provide web cam access. If you do not have a webcam, kindly attach an external camera while performing exercises.
        - Please avoid crowded places as the model can only detect 1 person. 
        - Please ensure that the surrounding is well lit so that the camera can detect you.
        - Please make sure the camera is focused on you based on the exercise so that the system can detect the angles and give you the correct input on form and count reps.

        With all that out of the way, Its time for you to get pumped up
        """)

    with col2:
        st.image('./gif/ham.gif')

def exercise_page(exercise):
    st.markdown(f"## {exercise}")
    weight = st.slider('What is your weight?', 20, 130, 40)
    st.write(f"I'm {weight} kgs")

    st.write("-------------")

    goal_calorie = st.slider('Set a goal calorie to burn', 1, 200, 15)
    st.write(f"I want to burn {goal_calorie} kcal")
    
    st.write("-------------")

    st.write("Click on the Start button to start the live video feed.")
    st.write("##")

    if st.button("Start"):
        try:
            run_exercise_tracking(exercise, weight, goal_calorie)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

def run_exercise_tracking(exercise, weight, goal_calorie):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open camera.")
        return
    
    detector = PoseDetector(detectionCon=0.7, trackCon=0.7)
    
    counter = 0
    direction = 0
    
    frame_placeholder = st.empty()
    
    while True:
        ret, img = cap.read()
        if not ret:
            st.error("Error: Could not read frame from camera.")
            break
        
        img = cv2.resize(img, (640, 480))
        
        try:
            img = detector.findPose(img, draw=False)
            lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
            
            if len(lmList) > 0:
                angle = calculate_angle(lmList, exercise)
                
                # Count reps
                if angle >= 160:
                    if direction == 0:
                        counter += 0.5
                        direction = 1
                if angle <= 30:
                    if direction == 1:
                        counter += 0.5
                        direction = 0
                
                # Draw counter on image
                cv2.putText(img, f"Count: {int(counter)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(img, channels="RGB")
            
        except Exception as e:
            logger.error(f"Error in pose detection: {str(e)}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Calculate calories burned
    calories_burned = calculate_calories(exercise, counter, weight)
    display_results(counter, calories_burned, goal_calorie)

def calculate_angle(lmList, exercise):
    if exercise == "Left Dumbbell":
        return angle_3_points(lmList, 11, 13, 15)
    elif exercise == "Right Dumbbell":
        return angle_3_points(lmList, 12, 14, 16)
    elif exercise == "Squats":
        return angle_3_points(lmList, 24, 26, 28)
    elif exercise == "Pushups":
        return angle_3_points(lmList, 11, 13, 15)
    elif exercise == "Shoulder press":
        left_angle = angle_3_points(lmList, 11, 13, 15)
        right_angle = angle_3_points(lmList, 12, 14, 16)
        return min(left_angle, right_angle)

def angle_3_points(lmList, p1, p2, p3):
    x1, y1 = lmList[p1][1:3]
    x2, y2 = lmList[p2][1:3]
    x3, y3 = lmList[p3][1:3]
    
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    return angle

def calculate_calories(exercise, reps, weight):
    calorie_factors = {
        "Left Dumbbell": 0.25,
        "Right Dumbbell": 0.25,
        "Squats": 0.3,
        "Pushups": 0.32,
        "Shoulder press": 0.22
    }
    return calorie_factors[exercise] * reps

def display_results(reps, calories_burned, goal_calorie):
    st.write("---------")
    st.write("## Analytics") 
    st.write(f"You did {int(reps)} reps")   
    
    st.write(f"You have burned {calories_burned:.2f} kcal of calories")
    if calories_burned < goal_calorie:
        st.write("You have not achieved your goal. Try again")
    else:
        st.write("You have achieved your goal. Congratulations")
    
    fig = go.Figure(data=[go.Bar(x=['Exercise'], y=[calories_burned], name='Calories Burned')])
    fig.add_trace(go.Bar(x=['Exercise'], y=[goal_calorie], name='Goal Calorie'))
    fig.update_layout(title='Calories Burned vs Goal', xaxis_title='Exercise', yaxis_title='Calories')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()