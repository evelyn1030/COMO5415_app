import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)", page_icon="🏙️", layout="wide")
st.title("Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)")

st.markdown("""
### 🏙️ Symbolism
The seventh and final bloom glows in **Chongqing** —  
the city where *Teens in Times* first took root.  
It was here, beside the **Jialing River**, that their journey began —  
where seven young boys trained, dreamed, and built the foundation of everything to come.  

Now, five years later, they return to the same city,  
not as trainees, but as artists who have grown under the light of time.  
This **Golden Bloom** represents **maturity, faith, and continuation** —  
a homecoming of hearts and an unbroken promise:  

> “We’re still walking forward — together.”  

---

### ✨ Event
At the **5th Anniversary Concert in Chongqing**,  
the stage shimmered like the city lights reflected on the river.  
Five years of laughter, sweat, and perseverance came together in one night.  

Chongqing — their place of origin, their training ground,  
the city that once held their earliest dreams —  
now welcomed them back in golden light.  

Some wondered if this might be their last performance as a group,  
as they step into adulthood and pursue new paths:  
music, acting, creation.  
But when they stood beneath the familiar skyline and smiled at each other,  
their answer was clear:  

> “No, this isn’t the end.  
> We still have a long way to go.”  

It wasn’t farewell —  
it was **a renewal of their vow**,  
a reminder that the roots planted in Chongqing  
will keep growing wherever the road leads.  

---

### 🌿 Garden Meaning
The **Golden Bloom** symbolizes **growth without separation**.  
Even as each member reaches toward his own horizon,  
their roots remain intertwined in the same soil —  
the soil of **Jialing’s riverside youth**.  

This bloom reminds us that:  
> growing up doesn’t mean walking away —  
> it means carrying the past forward with courage.  

In our *Garden in Time*,  
this final bloom shines like sunset over the Jialing River —  
warm, steadfast, and eternal.  

It whispers to everyone who has walked with them:  
> “We began here, we grew here,  
> and no matter where the wind takes us,  
> we will always return to where the light first found us.” 🌄  
""")

# ---------- Audio ----------
st.subheader("Audio Reflection")

audio_path = Path("assets/audio/b7_goodbyesorrow.mp3")
if not audio_path.exists():
    audio_path = Path("assets/audio/b7_goodbyesorrow.MP3")

if audio_path.exists():
    st.audio(str(audio_path), format="audio/mp3")
else:
    st.warning(f"⚠️ Audio file not found: {audio_path}")

# ---------- Image ----------
img_path = Path("assets/milestones/chongqing5.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Chongqing • 5th Anniversary Concert", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Chongqing 5th Anniversary image not found. Please place it at assets/milestones/chongqing5.jpg")
