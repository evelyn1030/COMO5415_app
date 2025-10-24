# pages/Overview.py
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Overview • A Garden in Time", page_icon="🌸", layout="wide")

# ---------- Custom Style ----------
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #fffafc 0%, #f3f9ff 100%);
}
.main .block-container { position: relative; z-index: 1; } /* content above glow layer */

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

/* -------- Ambient subtle glow dots (background) -------- */
.ambient-glow {
  position: fixed; inset: 0; z-index: 0;
  pointer-events: none; overflow: hidden;
}
.glow-dot {
  position: absolute;
  width: 18px; height: 18px; border-radius: 50%;
  opacity: 0.65;
  background: radial-gradient(circle,
              rgba(255, 183, 197, 0.85) 0%,
              rgba(255, 183, 197, 0.45) 40%,
              rgba(255, 183, 197, 0.0) 70%);
  filter: blur(0.2px);
  animation: float 14s ease-in-out infinite, breathe 5.6s ease-in-out infinite;
}
.glow-dot.c2 { background: radial-gradient(circle,
              rgba(173, 216, 230, 0.85) 0%,
              rgba(173, 216, 230, 0.45) 40%,
              rgba(173, 216, 230, 0.0) 70%); }
.glow-dot.c3 { background: radial-gradient(circle,
              rgba(255, 201, 150, 0.85) 0%,
              rgba(255, 201, 150, 0.45) 40%,
              rgba(255, 201, 150, 0.0) 70%); }

@keyframes float {
  0%   { transform: translate3d(0,0,0) scale(1); }
  50%  { transform: translate3d(var(--dx, 12px), var(--dy, -16px), 0) scale(1.08); }
  100% { transform: translate3d(0,0,0) scale(1); }
}
@keyframes breathe {
  0%,100% { opacity: 0.60; }
  50%     { opacity: 0.85; }
}
@media (max-width: 820px) {
  .glow-dot { width: 14px; height: 14px; }
}
</style>
""", unsafe_allow_html=True)

# ---------- Ambient Glow Layer (does not block clicks) ----------
st.markdown("""
<div class="ambient-glow">
  <div class="glow-dot"   style="left:8%;   top:14%;  --dx:10px;  --dy:-12px;"></div>
  <div class="glow-dot c2" style="left:20%;  top:28%;  --dx:-8px;  --dy:-18px;"></div>
  <div class="glow-dot c3" style="left:32%;  top:12%;  --dx:12px;  --dy:-10px;"></div>

  <div class="glow-dot"   style="left:72%;  top:18%;  --dx:-10px; --dy:-14px;"></div>
  <div class="glow-dot c2" style="left:84%;  top:30%;  --dx:9px;   --dy:-12px;"></div>
  <div class="glow-dot c3" style="left:90%;  top:12%;  --dx:-12px; --dy:-8px;"></div>

  <div class="glow-dot"   style="left:14%;  top:68%;  --dx:8px;   --dy:-10px;"></div>
  <div class="glow-dot c2" style="left:26%;  top:82%;  --dx:-6px;  --dy:-14px;"></div>
  <div class="glow-dot c3" style="left:40%;  top:74%;  --dx:12px;  --dy:-12px;"></div>

  <div class="glow-dot"   style="left:60%;  top:76%;  --dx:-10px; --dy:-16px;"></div>
  <div class="glow-dot c2" style="left:74%;  top:84%;  --dx:10px;  --dy:-10px;"></div>
  <div class="glow-dot c3" style="left:88%;  top:68%;  --dx:-8px;  --dy:-12px;"></div>
</div>
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
