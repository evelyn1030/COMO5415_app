import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 3 • 1st Anniversary", page_icon="🌼", layout="wide")
st.title("Bloom 3 • The Mature Bloom (1st Anniversary)")

st.markdown("""
### 🌼 Symbolism
The third bloom in our *Endless Summer Garden* represents **growth and reflection** —  
the moment when the once-fragile seedlings of youth learned to stand tall against the wind.  
It was no longer about chasing the spotlight, but about **understanding their own rhythm**.  

This bloom captures a quiet kind of strength —  
the kind that keeps shining even when no one is watching.  
Through hardship and distance, the boys learned that growth often happens  
not in cheers, but in silence.  

---

### 🌙 Event
On **November 23, 2020**, *Teens in Times* celebrated their first anniversary.  
The stage was different this time — there was no live audience,  
no roaring cheers, only the echo of their own voices in an empty hall.  
Yet, that night felt more sincere than ever.  

They performed with calm confidence,  
transforming solitude into light.  
Each song became a letter to their past selves —  
a reminder of every early morning rehearsal,  
every stumble, every small victory that built who they had become.  

The anniversary concert wasn’t just a performance;  
it was a **mirror** — reflecting how far they had come,  
and how deeply they had learned to love what they do.  

---

### 🌿 Garden Meaning
This bloom symbolizes **maturity, endurance, and gratitude**.  
It reminds us that even when applause fades,  
faith and love can still carry dreams forward.  

For fans, it was a moment of deep connection —  
watching the boys turn loneliness into art,  
and silence into resonance.  

In our *Garden in Time*, this mature bloom will always mark the season  
when they stood on a quiet stage and proved that light  
does not need noise to be real. 💫  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b3_anniversary.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b3_anniversary.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/anniversary.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="1st Anniversary", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Anniversary image not found. Please place it at assets/milestones/anniversary.jpg")
