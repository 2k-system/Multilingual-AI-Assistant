import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
from src.style import apply_premium_style
import time

def main():
    st.set_page_config(page_title="System AI", page_icon="🎙️", layout="centered")
    apply_premium_style()

    # Header Section
    st.markdown("<h1 style='text-align: center;'>NOVA <span style='color:#00f2ff'>AI</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.7;'>Your Multilingual Voice Intelligence</p>", unsafe_allow_html=True)
    st.divider()

    # Interaction Layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔴 TAP TO SPEAK", use_container_width=True):
            status_placeholder = st.empty()
            status_placeholder.markdown("<div class='status-pulse'></div><b>Listening...</b>", unsafe_allow_html=True)
            
            user_text = voice_input()
            
            if user_text:
                status_placeholder.empty()
                st.markdown(f"**You:** {user_text}")
                
                with st.status("Generating Response...", expanded=True) as status:
                    ai_response = llm_model_object(user_text)
                    text_to_speech(ai_response)
                    status.update(label="Response Ready!", state="complete", expanded=False)
                
                # Display Result in a Glass Card
                st.write(ai_response)
                
                if st.audio("speech.mp3"):
                    st.success("Audio synthesized successfully.")
            else:
                status_placeholder.error("I missed that. Try again?")

if __name__ == "__main__":
    main()