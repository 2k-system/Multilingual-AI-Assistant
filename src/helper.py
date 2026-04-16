import os
import logging
import speech_recognition as sr
from google import genai # Modern 2026 SDK
from gtts import gTTS
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
load_dotenv()

# Initialize Client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def voice_input():
    """Captures audio and converts to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except Exception as e:
        logging.error(f"Speech error: {e}")
        return None

def llm_model_object(user_text):
    """Sends text to Gemini 2.0 Flash"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite', 
            contents=user_text
        )
        return response.text
    except Exception as e:
        return f"AI Error: {e}"

def text_to_speech(text):
    """Saves response as MP3"""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
    except Exception as e:
        logging.error(f"TTS Error: {e}")
        
    