# pages/Overview.py
import streamlit as st
from pathlib import Path

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

/* Content card */
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
    animation: fadein 1.0s ease-in;
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
.enter-btn { text-align: center; margin-top: 1.5em; }
</style>
""", unsafe_allow_html=True)

# ---------- Banner (lazy load + max width limit) ----------
# Prefer webp if available (smaller), otherwise png
banner_path = Path("assets/banner.webp") if Path("assets/banner.webp").exists() else Path("assets/banner.png")

if banner_path.exists():
    st.markdown(
        f"""
        <div style="text-align:center; margin-bottom: 8px;">
            <img src="{banner_path.as_posix()}"
                 alt="A Garden in Time • Endless Summer Banner"
                 loading="lazy"
                 style="max-width:1200px; width:90%; height:auto; border-radius:10px;
                        box-shadow:0 6px 18px rgba(0,0,0,0.10);" />
            <div style="color:#999; font-size:12px; margin-top:6px;">
                A Garden in Time • Endless Summer
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Banner image not found. Place one at assets/banner.webp or assets/banner.png")

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
