from setuptools import find_packages, setup

setup(
    name="Multilingual AI Assistant",
    version="0.0.0",
    author="sys",
    author_email="pranalidhawade@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)
