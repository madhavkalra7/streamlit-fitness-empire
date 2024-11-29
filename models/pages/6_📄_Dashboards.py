import streamlit as st
import base64

st.set_page_config(page_title="Dashboards",page_icon="models/images/FE.png",layout="wide")

css_styles = """
<style>
/* Container for the header */
.header-container {
    background-color: #9C0000;
    padding: 20px;
    text-align: center;
    border-radius: 10px;
    animation: fadeIn 2s ease-in-out;
}

/* Styling and animation for the header text */
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
/* Container for images */
.image-box {
    display: inline-block;
    padding: 10px;
    margin: 10px;
    border: 2px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s, box-shadow 0.3s;
}

/* Styling for images */
.image-box img {
    max-width: 100%;
    border-radius: 10px;
    margin: 0; /* Reset margin */
    padding: 0; /* Reset padding */
    display: block; /* Ensure block display */
}

/* Hover effect for image container */
.image-box:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
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
st.markdown(css_styles, unsafe_allow_html=True)

st.markdown("""
<div class="header-container">
    <h1>Interactive Power BI Dashboards</h1>
    <p>Explore insights and trends with dynamic visualizations</p>
</div>
""", unsafe_allow_html=True)

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_paths = [
    "models/images/dashboard1.jpg",
    "models/images/dashboard2.jpg",
    "models/images/dashboard3.jpg",
    "models/images/dashboard4.jpg",
    "models/images/dashboard5.jpg",
    "models/images/dashboard6.jpg",
    "models/images/dashboard7.jpg",
]

for image_path in image_paths:
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-box"><img src="data:image/jpeg;base64,{image_base64}" alt="Dashboard Image"></div>', unsafe_allow_html=True)
