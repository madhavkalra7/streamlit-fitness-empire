import streamlit as st
import time

st.set_page_config(page_title="Developers", page_icon="models/images/FE.png", layout="wide")

st.markdown(
    """
    <style>
    @keyframes slideInLeft {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    .slide-in-left {
        animation: slideInLeft 1s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="slide-in-left">Meet Our Team</h1>', unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .team-member {
        display: flex;
        align-items: center;
        margin: 20px 0;
        padding: 20px;
        border: 2px solid white;
        border-radius: 10px;
        background-color: #9C0000;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }

    .team-member:hover {
        transform: scale(1.05);
    }

    .team-member img {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        transition: transform 0.3s;
    }

    .team-member img:hover {
        transform: rotate(10deg);
    }

    .social-icons {
        display: grid;  /* Use grid layout */
        grid-template-columns: repeat(4, 1fr);  /* Four equal columns for icons */
        justify-items: center;  /* Center the icons */
        margin-top: 10px;  /* Add some space above the icons */
    }

    .social-icons a {
        margin: 0 5px;  /* Add some margin between icons */
        transition: transform 0.3s;
        color: white;  /* Set icon color */
    }

    .social-icons a:hover {
        transform: scale(1.2);
    }

    .animate {
        animation: fadeIn 2s;
    }

    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    .name-container {
        background-color: #9C0000;  /* Red background */
        padding: 10px;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Load Font Awesome
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# Define a function to display team member information
def display_member(name, role, image_path, about_text, social_links):
    col1, col2 = st.columns([1, 1])  # Create two columns
    with col1:
        st.markdown(f"<div class='team-member animate'>{name}</div>", unsafe_allow_html=True)  # Team member name as an animated heading
        st.write(role)  # Display the team member's role
        st.write(about_text)  # About section text
        
        # Social media icons
        st.write("## Connect with Me")
        st.markdown("<div class='social-icons'>", unsafe_allow_html=True)  # Start social icons div
        for platform, link in social_links.items():
            if platform == "Instagram":
                st.markdown(f'<a href="{link}" target="_blank"><i class="fab fa-instagram" style="font-size: 30px;"></i></a>', unsafe_allow_html=True)
            elif platform == "LinkedIn":
                st.markdown(f'<a href="{link}" target="_blank"><i class="fab fa-linkedin" style="font-size: 30px;"></i></a>', unsafe_allow_html=True)
            elif platform == "Email":
                st.markdown(f'<a href="mailto:{link}"><i class="fas fa-envelope" style="font-size: 30px;"></i></a>', unsafe_allow_html=True)
            elif platform == "Phone":
                st.markdown(f'<a href="tel:{link}"><i class="fas fa-phone" style="font-size: 30px;"></i></a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)  # End social icons div

    with col2:
        st.image(image_path, use_column_width=True)  # Display the team member's image


# Member 1 (Your details)
your_about_text = "Hii, I am Madhav Kalra. Project Head"  # Unique about text for you
your_social_links = {
    "Instagram": "https://www.instagram.com/madhavkalra._",  # Your Instagram link
    "LinkedIn": "https://www.linkedin.com/in/madhav-kalra",  # Your LinkedIn link
    "Email": "madhavkalra2005@gmail.com",  # Your email address
    "Phone": "+919813569096"  # Your phone number
}
display_member("<h2>Madhav Kalra</h2>", "Student", "models/images/mk.jpg", your_about_text, your_social_links)  # Update the image path

# Member 2 (Madhav Goyal)
member1_about_text = "Hello! I'm Madhav Goyal, a passionate learner in tech."  # Unique about text for member 1
member1_social_links = {
    "Instagram": "https://www.instagram.com/madhavgoyal._",  # Link for member 1
    "LinkedIn": "https://www.linkedin.com/in/madhav-goyal",  # Link for member 1
    "Email": "goyal.madhav@example.com",  # Link for member 1
    "Phone": "+919876543210"  # Link for member 1
}
display_member("<h2>Madhav Goyal</h2>", "Student", "models/images/mg.jpg", member1_about_text, member1_social_links)  # Update the image path

# Member 3 (Manekas Singh)
member2_about_text = "Hi, I'm Manekas Singh, eager to innovate and explore."  # Unique about text for member 2
member2_social_links = {
    "Instagram": "https://www.instagram.com/manekassingh",  # Link for member 2
    "LinkedIn": "https://www.linkedin.com/in/manekas-singh",  # Link for member 2
    "Email": "singh.manekas@example.com",  # Link for member 2
    "Phone": "+917056419844"  # Link for member 2
}
display_member("<h2>Manekas Singh</h2>", "Student", "models/images/ms.jpg", member2_about_text, member2_social_links)  # Update the image path

# Add a loading animation
with st.spinner('Loading...'):
    time.sleep(2) 
