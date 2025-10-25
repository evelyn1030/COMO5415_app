import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 6 • Haikou Concert", page_icon="🌅", layout="wide")
st.title("Bloom 6 • The Boundless Bloom (Haikou Concert)")

st.markdown("""
### 🌸 Symbolism
This bloom expands with **freedom and scale** —  
a full summer flower opening beneath the wide sky.

### 🎶 Event
On **May 2, 2023**, *Teens in Times* held their **first offline stadium concert** in **Haikou**,  
performing for tens of thousands of fans after years of anticipation.  
It was both a reward and a renewal — a testament to perseverance and love.

### 🌿 Garden Meaning
This bloom spreads across the horizon, celebrating connection between stage and audience —  
a symbol of unity and shared emotion.

""")

# Audio
st.subheader("Audio Reflection")
audio_file = open("assets/audio/b6_love1440.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

img_path = Path("assets/milestones/haikou.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="Haikou Stadium Concert", width=480)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Haikou concert image not found. Please place it at assets/milestones/haikou.jpg")

audio_path = Path("assets/audio/haikou.mp3")
if audio_path.exists():
    st.audio(str(audio_path))
else:
    st.info("Add audio file at assets/audio/haikou.mp3")

