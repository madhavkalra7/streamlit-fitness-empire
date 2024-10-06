import streamlit as st

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
        <h1>Chatbot</h1>
        <p>Get instant support and personalized advice with Fitness Empire's Bot, your intelligent AI fitness companion</p>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# ---- SPACE ADJUSTMENT FOR CONTENT ----
st.markdown('<div class="content-container"></div>', unsafe_allow_html=True)
# Add chatbot widget with enhanced size and CSS animations
chatbot_script = """
<style>
    .chatbot-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .chat-widget {
        width: 80%; /* Adjust width as needed */
        height: 600px; /* Adjust height as needed */
        border: 2px solid #6366f1;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        transform: perspective(600px) rotateX(15deg); /* 3D Effect */
        animation: float 5s ease-in-out infinite;
    }

    @keyframes float {
        0% {
            transform: translateY(0) rotateX(15deg);
        }
        50% {
            transform: translateY(-10px) rotateX(15deg);
        }
        100% {
            transform: translateY(0) rotateX(15deg);
        }
    }
</style>

<div class="chatbot-container">
    <iframe 
        class="chat-widget"
        src="https://bots.easy-peasy.ai/bot/39c1f447-146f-48a0-b3f6-987d573e61cd"
        frameborder="0">
    </iframe>
</div>
"""

# Embed the chatbot in your Streamlit app with custom CSS
st.components.v1.html(chatbot_script, height=650)
