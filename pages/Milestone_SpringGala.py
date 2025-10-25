import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 4 • Spring Festival Gala", page_icon="✨", layout="wide")
st.title("Bloom 4 • The Radiant Bloom (Spring Festival Gala)")

st.markdown("""
### ✨ Symbolism
The fourth bloom bursts open like a sunrise — dazzling, confident, and full of vitality.  
After walking through quiet nights and unseen rehearsals, the boys finally stepped into a light  
that reached millions.  

This bloom represents **recognition and pride** —  
the moment their long-nurtured sincerity was seen by the world.  
It was not just a performance, but a declaration:  
that hard work, kindness, and belief in one’s craft can truly illuminate a national stage.  

---

### 🌟 Event
In **February 2021**, *Teens in Times* appeared on the **Spring Festival Gala**,  
the most watched show in China.  
They performed under the grand lights, standing shoulder to shoulder with senior artists —  
no longer the unknown boys from practice rooms,  
but representatives of a new generation,  
bringing fresh energy to a stage watched by millions of families.  

That night, their song carried warmth and youth across the country.  
It wasn’t only a milestone in career,  
but a quiet promise to continue shining —  
for every dream that once felt small, for every young person still trying.  

---

### 🌿 Garden Meaning
The *Radiant Bloom* embodies **recognition, hope, and shared light**.  
It teaches that when one bloom shines, its glow can touch countless others.  
This was the moment when their personal growth became a collective pride —  
not only for fans, but for everyone who witnessed their journey from obscurity to brilliance.  

In our *Garden in Time*,  
this bloom stands for the first dawn that painted the whole sky golden —  
proof that light, when born from sincerity,  
will always find its way. 🌅  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b4_springgala.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b4_springgala.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/springgala.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Spring Festival Gala", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Spring Festival Gala image not found. Please place it at assets/milestones/springgala.jpg")
