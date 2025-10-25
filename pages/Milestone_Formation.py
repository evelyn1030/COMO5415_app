import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 1 • Debut Day", page_icon="🌱", layout="wide")
st.title("Bloom 1 • The First Bloom (Debut Day)")

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


st.markdown("""
### 🌸 Symbolism
The first hydrangea bloom in our *Endless Summer Garden* marks the **debut day** —  
a quiet beginning that would later blossom into a journey of light, growth, and connection.  
It represents not only a start, but also a **promise**: seven young boys stepping onto the stage,  
their dreams still tender yet burning with sincerity.  

It was the moment when uncertainty met courage,  
when a seed of belief began to take root — destined to bloom across time.  

---

### 🎶 Event
On **August 25, 2019**, *Teens in Times* officially formed.  
Few people noticed that day, and the lights were dim —  
but even in a small corner of the world, something extraordinary began.  
They recorded, performed, and built everything from the ground up,  
proving that even without spotlights, **passion can shine through the dark**.  

Their debut was not just a stage moment; it was an act of **faith** —  
a belief that genuine effort, unity, and youthful hope could one day move hearts.  

---

### 🌿 Garden Meaning
This bloom is the very first seed in our *Garden in Time*,  
symbolizing **hope, resilience, and the courage to begin**.  
Every petal holds a story of perseverance,  
and every melody echoes the shared heartbeat of the group and their fans.  

For those who have followed them from the start,  
this bloom will always represent the day we met —  
the day our stories intertwined,  
and we began to grow *together*. 🌱  
""")



# ---------- Image ----------
img_path = Path("assets/milestones/debut.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Debut Day", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Debut Day image not found. Please place it at assets/milestones/debut.jpg")
