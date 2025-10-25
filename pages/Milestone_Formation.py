import streamlit as st
from pathlib import Path
from PIL import Image


st.set_page_config(page_title="Bloom 1 • Debut Day", page_icon="🌱", layout="wide")
st.title("Bloom 1 • The First Bloom (Debut Day)")

st.markdown("""
### 🌸 Symbolism
The first hydrangea bloom in our Endless Summer Garden represents the **debut day**.  
It is tender and fragile, yet full of promise — just like the beginning of a new journey.

### 🎶 Event
This milestone marks the official **formation and debut** of *Teens in Times*.  

### 🌿 Garden Meaning
This bloom is the very first seed in our *Garden in Time*, symbolizing a hopeful start.
""")

# ---------- Audio ----------
from pathlib import Path
import streamlit as st

st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b1_popcorn.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b1_popcorn.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")


# Debut
img_path = Path("assets/milestones/debut.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Debut Day", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Debut Day image not found. Please place it at assets/milestones/debut.jpg")
