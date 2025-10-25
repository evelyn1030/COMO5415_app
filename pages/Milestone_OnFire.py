import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 2 • Youth on Fire", page_icon="🔥", layout="wide")
st.title("Bloom 2 • The Fiery Bloom (Youth on Fire)")

st.markdown("""
### 🔥 Symbolism
The second bloom bursts with **energy, courage, and creation** —  
it represents the moment when the garden caught fire with passion.  
After the uncertainty of debut, the boys began to find their voice,  
turning the stage into a canvas for their own stories.  

This bloom burns bright like youth itself —  
reckless yet sincere, full of the will to prove that dreams built by their own hands  
can shine just as fiercely as those made under spotlights.  

---

### 🎤 Event
*Youth on Fire* marked a new chapter for *Teens in Times* —  
a fully **self-produced performance stage**,  
where the members choreographed, designed, and refined every detail by themselves.  

Through this project, they created many meaningful performances,  
such as **《一万次长大》 (“Ten Thousand Times of Growing Up”)**,  
which gave voice to vulnerable groups and reminded everyone  
that pop music could carry empathy, responsibility, and light.  

Their flames were not only artistic — they were **human**,  
warming countless hearts and inspiring fans who saw, perhaps for the first time,  
what sincerity and perseverance in youth truly look like.  

---

### 🌿 Garden Meaning
This bloom represents the **power of self-creation** —  
the courage to build something real even when no one expects it from you.  
It’s a symbol of passion refined into meaning,  
of young artists who no longer wait to be seen, but **choose to be heard**.  

In our *Garden in Time*,  
this fiery bloom keeps glowing with hope —  
a reminder that even in the fiercest blaze,  
there is always warmth, purpose, and love.  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b2_gradualwarmth.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b2_gradualwarmth.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/onfire.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Youth on Fire", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Youth on Fire image not found. Please place it at assets/milestones/onfire.jpg")
