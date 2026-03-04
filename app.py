import streamlit as st
from streamlit_webrtc import webrtc_streamer
import numpy as np
import matplotlib.pyplot as plt

st.title("Loudness & Frequency Analyzer 🔊")

# Define the audio processing logic
def audio_frame_callback(frame):
    sound_array = frame.to_ndarray()
    # Perform a simple math check for volume
    amplitude = np.abs(sound_array).mean()
    return frame

# The WebRTC component that opens your mic
webrtc_streamer(
    key="audio-filter",
    audio_frame_callback=audio_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

st.write("When you click START, this app uses your mic to see sound waves!")
