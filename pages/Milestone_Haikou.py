import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 6 • The Gentle Return (Haikou Concert)", page_icon="🌊", layout="wide")
st.title("Bloom 6 • The Gentle Return (Haikou Concert)")

st.markdown("""
### 🌊 Symbolism
The sixth bloom unfolds beneath the Haikou sky —  
soft, humid, and full of light after years of distance.  
It represents **reunion and clarity**,  
the moment when tears turned into a mirror,  
and both the boys and their fans could finally *see each other clearly* again.  

This bloom whispers:  
> “We are here, after all the waiting. We still see you.”  

---

### 🌧️ Event
On **May 2, 2023**, *Teens in Times* held their first offline concert in three and a half years.  
When they looked down from the stage,  
the sight of tens of thousands of fans — eyes glistening through tears —  
felt like the first sunrise after a long storm.  

That night, every glance, every note,  
washed away three years of fog and separation.  
The boys sang *I Always See You*,  
and for the first time, those words were not metaphor —  
they were truth spoken through trembling voices.  

For the audience, it was release.  
For them, it was homecoming.  

---

### 🌿 Garden Meaning
The *Gentle Return* bloom stands for **reconnection, forgiveness, and mutual healing**.  
It reminds us that love is not erased by time —  
it only deepens when tested.  

Under the soft Haikou rain,  
they met again not as idols and fans,  
but as companions who had waited through silence.  
Their tears carried gratitude more than pain.  

In our *Garden in Time*,  
this bloom glows like twilight on calm water —  
a promise that no matter how far one drifts,  
they will always find their way back to the light. 🌥️  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b6_gradualwarmth.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b6_gradualwarmth.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/haikou.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Haikou Concert • 'I Always See You'", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Haikou Concert image not found. Please place it at assets/milestones/haikou.jpg")
