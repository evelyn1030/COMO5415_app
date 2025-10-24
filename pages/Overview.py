# pages/Overview.py
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Overview • A Garden in Time", page_icon="🌸", layout="wide")

# ---------- Soft static background (no animation, super lightweight) ----------
st.markdown("""
<style>
body {
    background:
        radial-gradient(circle at 30% 20%, rgba(255, 223, 236, 0.55) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(210, 230, 255, 0.45) 0%, transparent 50%),
        radial-gradient(circle at 50% 90%, rgba(255, 240, 220, 0.45) 0%, transparent 55%),
        linear-gradient(180deg, #fffafc 0%, #f3f9ff 100%);
}

/* Page structure */
.poetic-block {
    font-size: 1.1rem;
    line-height: 1.8;
    font-family: 'Georgia', 'Times New Roman', serif;
    background: rgba(255,255,255,0.6);
    padding: 2.5rem;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    margin-top: 1rem;
    margin-bottom: 2rem;
    animation: fadein 1.6s ease-in;
}
@keyframes fadein { from {opacity:0;} to {opacity:1;} }

h1 {
    font-family: 'Cinzel', serif;
    text-align: center;
    margin-bottom: 0.2em;
}
.subtitle {
    text-align: center;
    font-style: italic;
    color: #777;
    margin-bottom: 2em;
}
.enter-btn {
    text-align: center;
    margin-top: 1.5em;
}
</style>
""", unsafe_allow_html=True)

# ---------- Banner ----------
banner_path = Path("assets/banner.png")
if banner_path.exists():
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(str(banner_path), caption="A Garden in Time • Endless Summer", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("Banner image not found. Place it at assets/banner.png")

# ---------- Title ----------
st.title("A Garden in Time: Our Endless Summer")
st.markdown("<p class='subtitle'>A digital garden of memory, growth, and light.</p>", unsafe_allow_html=True)

# ---------- Poetic Narrative ----------
st.markdown("""
<div class="poetic-block">

In this digital garden, every bloom holds a memory.  
Some are tender and new, like the first light of spring;  
some carry the warmth of summer, glowing with laughter and song.  

**A Garden in Time** is not just a website —  
it is a living archive of *Endless Summer*,  
where design, sound, and motion grow together like flowers in the same soil.  

Each petal remembers a moment:  
the first debut, the trembling stage lights,  
the voices that met in the dark and learned to sing as one.  

This garden was built for those who once stood under the same sky —  
for the dreamers, the believers,  
the ones who kept their hearts open even when the seasons changed.  

Here, light and shadow coexist.  
Growth is not always gentle, yet it is always beautiful.  
Step inside, and you may find pieces of your own story  
rooted in the soil of time, still alive, still blooming.

</div>
""", unsafe_allow_html=True)

# ---------- Enter the Garden Button ----------
st.markdown("<div class='enter-btn'>", unsafe_allow_html=True)
if st.button("🌸 Enter the Garden →", type="primary", use_container_width=True):
    st.switch_page("pages/Timeline.py")
st.markdown("</div>", unsafe_allow_html=True)
