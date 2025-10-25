import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 7 • Chongqing 5th Anniversary", page_icon="🌻", layout="wide")
st.title("Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)")

st.markdown("""
### 🌸 Symbolism
The final bloom glows with **gratitude and fulfillment** —  
a golden hue symbolizing the warmth of five years of companionship.

### 🎶 Event
On **November 23, 2024**, *Teens in Times* returned to **Chongqing**  
for their **5th Anniversary Concert**.  
The city where many memories began witnessed their evolution and maturity.

### 🌿 Garden Meaning
This bloom completes the cycle — a return to the roots,  
where music and youth intertwine once more.

Image to be replaced  
Music to be added  
Video to be added  
""")

# Audio
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b7_goodbyesorrow.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b7_goodbyesorrow.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")


img_path = Path("assets/milestones/chongqing.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="Chongqing 5th Anniversary Concert", width=480)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Chongqing concert image not found. Please place it at assets/milestones/chongqing.jpg")

audio_path = Path("assets/audio/chongqing.mp3")
if audio_path.exists():
    st.audio(str(audio_path))
else:
    st.info("Add audio file at assets/audio/chongqing.mp3")
