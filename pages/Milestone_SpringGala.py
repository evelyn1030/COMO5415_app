import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 4 • CCTV Spring Festival Gala", page_icon="🏮", layout="wide")
st.title("Bloom 4 • The Radiant Bloom (Spring Festival Gala)")

st.markdown("""
### 🌸 Symbolism
This radiant bloom embodies **recognition and light** — the moment when their music reached millions of homes.  
It reflects not only fame but also a shared heartbeat with the audience across the nation.  

### 🎶 Event
In **2021**, *Teens in Times* appeared on the **CCTV Spring Festival Gala**,  
performing *“奔跑的青春 (Running Youth)”* in collaboration with **THE9**.  
This performance marked their **first appearance on the national stage**,  
uniting two generations of youth in a vibrant celebration of energy and hope.  

### 🌿 Garden Meaning
This bloom shines like the **lanterns of spring**, reminding us that growth also means being seen —  
to bloom brightly and share light with others.

""")

# audio
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b4_drunk.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b4_drunk.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")



img_path = Path("assets/milestones/springgala.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="2021 CCTV Spring Festival Gala", width=480)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Spring Gala image not found. Please place it at assets/milestones/springgala.jpg")

audio_path = Path("assets/audio/springgala.mp3")
if audio_path.exists():
    st.audio(str(audio_path))
else:
    st.info("Add audio file at assets/audio/springgala.mp3")
