import streamlit as st
from pathlib import Path
from PIL import Image


st.set_page_config(page_title="Bloom 2 • Youth On Fire", page_icon="🔥", layout="wide")
st.title("Bloom 2 • The Fiery Bloom (Youth On Fire)")

st.markdown("""
### 🌸 Symbolism
This bloom bursts with **heat and light**, embodying passion, energy, and a fearless drive forward.  
Its vivid magenta and blue tones reflect both the vibrance of youth and the intensity of their voices.  

### 🎶 Event
The **Youth On Fire** era was marked by the company’s **self-produced music stages**.  
These performances created **many classic stages and iconic choreographies**,  
establishing a unique identity for the group.  

Beyond artistry, the boys also used this era to **speak up for marginalized and disadvantaged groups**,  
showing that music and performance can carry both beauty and social meaning.  

### 🌿 Garden Meaning
In the garden, this is the **fiery bloom of summer** — radiant, brave, and unafraid to stand tall for others.

Image to be replaced
Music to be added
Video to be added
""")

# On Fire
img_path = Path("assets/milestones/onfire.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Youth On Fire", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Youth On Fire image not found. Please place it at assets/milestones/onfire.jpg")

