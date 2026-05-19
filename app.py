import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import os

# Page Config
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Language Translation Tool")
st.write("Translate text instantly into multiple languages.")

# Languages
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# Text Input
text = st.text_area(
    "Enter text to translate",
    height=150
)

# Dropdowns
source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# Translate Button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # Translation
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation Completed ✅")

            # Display Result
            st.subheader("Translated Text")
            st.write(translated)

            # Copy Button
            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated)
                st.success("Copied to clipboard!")

            # Text-to-Speech
            tts = gTTS(
                text=translated,
                lang=languages[target_lang]
            )

            audio_file = "translated_audio.mp3"
            tts.save(audio_file)

            # Audio Player
            audio_bytes = open(audio_file, "rb").read()

            st.audio(audio_bytes, format="audio/mp3")

            # Download Button
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="⬇ Download Audio",
                    data=file,
                    file_name="translated_audio.mp3",
                    mime="audio/mp3"
                )

        except Exception as e:
            st.error(f"Error: {e}")