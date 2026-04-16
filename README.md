# 🎙️ Nova AI: Multilingual Voice Assistant

Nova AI is a premium, glassmorphic voice assistant built with **Streamlit** and **Gemini 2.5/3.1**. It captures voice input, processes it using Google's latest Generative AI models, and provides both text and synthesized speech responses.

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features
- **Glassmorphic UI:** Modern Dark Mode interface with frosted glass effects.
- **Voice-to-Text:** Real-time speech recognition using Google Speech API.
- **AI Intelligence:** Powered by Gemini 2.5 Flash for low-latency reasoning.
- **Text-to-Speech:** High-quality audio synthesis for AI responses.
- **Modular Architecture:** Clean folder structure (`src/`) for easy scalability.

## 🛠️ Project Structure
```text
Multilingual-AI-Assistant/
├── .streamlit/          # UI Theme configuration
├── src/
│   ├── helper.py        # Logic for Voice, AI, and TTS
│   ├── style.py         # Premium CSS Styling
│   └── __init__.py      # Package initialization
├── app.py               # Main Streamlit Application
├── .env                 # API Keys (Ignored by Git)
├── requirements.txt     # Dependency list
└── setup.py             # Local package installer