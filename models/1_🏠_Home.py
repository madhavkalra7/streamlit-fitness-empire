import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Fitness Trainer", page_icon=":tada:", layout="wide")

# Refresh the page every 2000 milliseconds (2 seconds)
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("D:\\Downloads\\AI-Fitness-Trainer-main\\AI-Fitness-Trainer-main\\models\\styles\\styles.css")

# Load Lottie animations
music = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ikk4jhps.json")
podcast = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_JjpNLdaKYX.json")

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
header_html = """
    <div class="header-container">
        <h1>AI Fitness Trainer</h1>
        <p>Step into a fitter future: Welcome to your Fitness Empire!</p>
    </div>
"""

# Display the animated header
st.markdown(header_html, unsafe_allow_html=True)

# Set scroll position on page load
scroll_js = """
<script>
    window.onload = function() {
        window.scrollTo(0, 0);
    }
</script>
"""

st.markdown(scroll_js, unsafe_allow_html=True)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.write("## About us")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
        st.write(
            """
            - We are thrilled to have you here on our platform dedicated to empowering and inspiring individuals on their journey towards a healthier and fitter lifestyle. Whether you're a seasoned fitness enthusiast or just starting your fitness journey, we have everything you need to reach your goals and achieve the best version of yourself.
            
            - What sets us apart is the fact that we provide personalized assistance at the comfort of your home or any place of your choice at a price that is both convenient and much cheaper than traditional gyms.

            Let your fitness journey start here!
            Join us today and embark on a transformative experience that will enhance your physical and mental well-being. Let's build strength, resilience, and a healthier future together!
            """
        )

    with right_column:
        st.image("D:\\PBL-3\\WhatsApp Image 2024-10-03 at 21.02.55_623dc771.jpg", width=400, caption="NO PAIN NO GAIN")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Get fit, Jam on, Repeat :headphones:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(music, height=300, key="music")
    with text_column:
        st.write("##")
        st.subheader("Workout music")
        st.write(
            """
            Power up your workout with the ultimate music fuel!
            """
        )
        st.markdown("[Have a Listen...](https://open.spotify.com/playlist/6N0Vl77EzPm13GIOlEkoJn?si=9207b7744d094bd3)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(podcast, height=300, key="podcast")
    with text_column:
        st.write("##")
        st.subheader("Podcast")
        st.write(
            """
            Take your workouts to the next level with our immersive podcast that pumps you up from start to finish!
            """
        )
        st.markdown("[Have a listen...](https://open.spotify.com/playlist/09Ig7KfohF5WmU9RhbDBjs?si=jyZ79y3wQgezrEDHim0NvQ)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/c722428e42528bf09a0c149f6b7d3909" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
