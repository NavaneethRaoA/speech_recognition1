import os
import json
import vosk
import pyaudio
import streamlit as st
import subprocess
import webbrowser

# Path to Vosk model
MODEL_PATH = "vosk-model-small-en-us-0.15"

# Streamlit UI Setup
st.set_page_config(page_title="Offline Voice Assistant", page_icon="🎤")
st.title("🎙️ Offline Voice Assistant")
st.markdown("**Speak a command, and I'll execute it!**")

# UI Layout
col1, col2 = st.columns(2)
#with col1:
    #st.image("https://cdn-icons-png.flaticon.com/512/3794/3794562.png", width=100)
with col2:
    st.write("### 👂 Voice Commands")

# Check if Vosk model exists
if not os.path.exists(MODEL_PATH):
    st.error("❌ Vosk model not found! Please download and extract it.")
    st.stop()

# Load Vosk model
model = vosk.Model(MODEL_PATH)

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Function to execute commands
def process_command(text):
    text = text.lower()
    st.success(f"🗣️ You said: **{text}**")

    if "open notepad" in text:
        subprocess.run("notepad.exe", shell=True)
        st.success("📝 Opened Notepad!")

    elif "open calculator" in text:
        subprocess.run("calc.exe", shell=True)
        st.success("🖩 Opened Calculator!")

    elif "open file explorer" in text:
        subprocess.run("explorer.exe", shell=True)
        st.success("📂 Opened File Explorer!")

    elif "play music" in text:
        music_path = "C:\\Users\\Public\\Music\\Sample Music\\song.mp3"  # Change this path
        subprocess.run(["start", music_path], shell=True)
        st.success("🎵 Playing Music!")

    elif "search google for" in text:
        query = text.replace("search google for", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            st.success(f"🔎 Searched Google for: {query}")

    else:
        st.warning("❓ Command not recognized.")

# Speech recognition function
def recognize_speech():
    st.write("🎤 **Listening... Speak now.**")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                process_command(text)
            break  # Stop after processing one command

# Add Buttons
st.markdown("### 🎛️ Controls")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎧 Start Listening"):
        recognize_speech()
with col2:
    if st.button("🛑 Stop Listening"):
        stream.stop_stream()
        st.warning("Stopped Listening.")
with col3:
    if st.button("🔄 Clear Output"):
        st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("💡 **Supported Commands:**")
st.markdown("- 📝 **Open Notepad**")
st.markdown("- 🖩 **Open Calculator**")
st.markdown("- 📂 **Open File Explorer**")
st.markdown("- 🎵 **Play Music**")
st.markdown("- 🔎 **Search Google for [your query]**")
