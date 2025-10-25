import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 5 • The Age of Dancing Elephants", page_icon="🌾", layout="wide")
st.title("Bloom 5 • The Transforming Bloom (The Age of Dancing Elephants)")

st.markdown("""
### 🌾 Symbolism
The fifth bloom — *The Age of Dancing Elephants* — represents **transformation and self-realization**.  
In Chinese culture, “舞象之年” marks the transition from youth to maturity,  
when a young person learns to carry both strength and tenderness in equal measure.  

This bloom is no longer soft or fiery — it is steady, grounded, and aware.  
It stands for the moment when the boys of *Teens in Times* grew into young men,  
ready to bear the weight of meaning, creation, and responsibility.  

---

### 🐘 Event
During this stage, the group entered university life while balancing intense schedules.  
They faced sleepless nights, long rehearsals, and quiet solitude behind campus walls.  
It was a time of exhaustion and longing —  
but also one that revealed their astonishing discipline and self-drive.  

As the world debated their future, the boys kept walking,  
turning confusion into conviction.  
Their documentary *The Age of Dancing Elephants* captured this exact crossroad —  
when the spotlight dimmed, yet their inner light began to glow from within.  

It was no longer about fame.  
It was about asking deeper questions:  
**“Who are we becoming? What does it mean to grow, to create, to stay kind?”**  

---

### 🌱 Garden Meaning
This bloom embodies **growth through reflection**.  
It reminds us that every dream must pass through the stage of questioning —  
that real strength is built not in applause, but in persistence.  

Like the elephants of the earth, slow yet powerful,  
*TNT* learned to move with patience and purpose.  
Their journey became not just a story of idols,  
but a story of **youth finding meaning** in their own way.  

In our *Garden in Time*, this transforming bloom whispers:  
> “To dance is not to escape the storm, but to learn to move within it.”  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b5_vermilion.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b5_vermilion.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/dancingelephants.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="The Age of Dancing Elephants", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Dancing Elephants image not found. Please place it at assets/milestones/dancingelephants.jpg")
