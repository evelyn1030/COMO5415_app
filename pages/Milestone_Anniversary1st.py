import streamlit as st
from pathlib import Path
from PIL import Image


st.set_page_config(page_title="Bloom 3 • 1st Anniversary", page_icon="🎉", layout="wide")
st.title("Bloom 3 • The Mature Bloom (1st Anniversary)")

st.markdown("""
### 🌸 Symbolism
The full hydrangea cluster represents **maturity** — layered, abundant, and deeply colored.  
This bloom symbolizes resilience and the ability to thrive even in difficult conditions.

### 🎶 Event
The **1st Anniversary Concert** took place during the pandemic.  
Although there were **no live audiences**, the boys still poured their energy into rehearsals,  
carefully preparing the stage and delivering their performance with dedication and heart.  

### 🌿 Garden Meaning
This is the **mature bloom** of the Endless Summer Garden — growing stronger despite challenges,  
and radiating hope that the seasons of connection and music will continue.
""")

from pathlib import Path
from PIL import Image
import streamlit as st

img_path = Path("assets/milestones/anniversary1st.jpg")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="1st Anniversary Concert", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("1st Anniversary image not found. Please place it at assets/milestones/anniversary1st.jpg")
