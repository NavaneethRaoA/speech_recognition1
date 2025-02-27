# speech_recognition
**speech recognition** which converts speech to text and also executes commands over speech to automate tasks.
You can do the following:
  * convert speech to text
  * Execute commands like open something in the system
  * search through voice in browser(Google)

> Have the attractive UI with buttons


To execute the code:

* STEP-1:
        Install libraries
            >pip install vosk pyaudio streamlit
            >pip install streamlit
            >pip install vosk
            >Vosk requires a pre-trained model for speech recognition. Download a model from:
                   🔗 https://alphacephei.com/vosk/models  (file:  vosk-model-small-en-us-0.15.zip (50MB))
            * Extract it into your project folder (e.g., speech_recognition_proj/vosk-model/).

* STEP-2:
   Find the code in the .py file
* STEP-3:
   To run the code use command
     > streamlit run offline_speech_gui.py
