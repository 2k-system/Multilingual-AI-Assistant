import streamlit as st

def apply_premium_style():
    custom_css = """
    <style>
        /* Glassmorphism Effect for containers */
        [data-testid="stVerticalBlock"] > div:has(div.element-container) {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }

        /* Customizing the Record Button */
        div.stButton > button {
            background: linear-gradient(135deg, #00f2ff 0%, #007bff 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 50px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 242, 255, 0.3);
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 242, 255, 0.5);
            color: white;
        }

        /* Animated Pulse for the "Listening" state */
        .status-pulse {
            width: 12px;
            height: 12px;
            background: #ff4b4b;
            border-radius: 50%;
            display: inline-block;
            margin-right: 10px;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 75, 75, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)