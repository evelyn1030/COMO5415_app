import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 5 • The Age of Dancing Elephants", page_icon="🐘", layout="wide")
st.title("Bloom 5 • The Transforming Bloom (The Age of Dancing Elephants)")

st.markdown("""
### 🌸 Symbolism
This bloom stands for **transition and growth** —  
a time when innocence transforms into self-awareness and strength.

### 🎶 Event
The release of the **second album, “The Age of Dancing Elephants,”**  
marked a turning point in *Teens in Times’* journey,  
symbolizing their step into a new artistic and emotional maturity.

### 🌿 Garden Meaning
In the garden, this is the **turning bloom** — elegant yet powerful,  
reminding us that change is also a form of beauty.

Image to be replaced  
Music to be added  
Video to be added  
""")

img_path = Path("assets/milestones/dancingelephants.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="The Age of Dancing Elephants", width=480)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Album image not found. Please place it at assets/milestones/dancingelephants.jpg")

audio_path = Path("assets/audio/dancingelephants.mp3")
if audio_path.exists():
    st.audio(str(audio_path))
else:
    st.info("Add audio file at assets/audio/dancingelephants.mp3")
