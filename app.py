import googletrans
import speech_recognition
import gtts
import streamlit as st
from PIL import Image

# Set page title and header
st.title("Speech to Text and Translation")

languages = googletrans.LANGUAGES

col1, col2 = st.columns(2)
with col1:
    option = st.selectbox('Select your Language', languages.values())
    # Get the language code based on the selected language
    language_code = next(key for key, value in languages.items() if value == option)

with col2:
    option2 = st.selectbox('Select Translation Language', languages.values())
    language_code2 = next(key for key, value in languages.items() if value == option2)

# Speech Recognition
recognizer = speech_recognition.Recognizer()

text = ""  # Initialize the 'text' variable

if st.button("Speak now"):
    with speech_recognition.Microphone() as source:
        logo_url = "https://img.freepik.com/premium-vector/microphone-logo-design-inspiration_57043-231.jpg"
        width = 150  # desired width in pixels
        height = 100  # desired height in pixels

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{logo_url}" alt="logo" width="{width}" height="{height}" style="object-fit: contain;">
            </div>
            """,
            unsafe_allow_html=True
        )

        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=language_code)
        st.write("Recognized Text:", text)

    # Translation
    translator = googletrans.Translator()
    translation = translator.translate(text, dest=language_code2)
    translated_text = translation.text
    st.write("Translated Text:", translated_text)

    # Convert Text to Audio
    converted_audio = gtts.gTTS(translated_text, lang=language_code2)
    converted_audio.save("convert6.mp3")
    st.audio("convert6.mp3", format="audio/mp3")
