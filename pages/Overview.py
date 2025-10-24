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

from pathlib import Path
import streamlit as st

def find_asset(*names: str) -> Path | None:
    for n in names:
        p = Path(n)
        if p.exists():
            return p
    return None

# ---------- Soft twinkle lights (CSS-only, lightweight, no Chinese comments) ----------
st.markdown("""
<style>
.twinkle-layer {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

/* Small glowing dots floating slowly */
.twinkle-dot {
  position: absolute;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.1) 70%, transparent 100%);
  filter: blur(0.6px);
  animation: twinkle 3.8s ease-in-out infinite;
  opacity: 0.75;
}

@keyframes twinkle {
  0%, 100% { transform: translate3d(0, 0, 0) scale(1); opacity: 0.65; }
  50%      { transform: translate3d(0, -6px, 0) scale(1.08); opacity: 0.95; }
}

/* Randomized positions and delays for a natural look */
.twinkle-dot:nth-child(1)  { left: 8%;   top: 16%; animation-delay: 0.1s;  transform: scale(0.9); }
.twinkle-dot:nth-child(2)  { left: 18%;  top: 72%; animation-delay: 0.5s;  transform: scale(1.1); }
.twinkle-dot:nth-child(3)  { left: 28%;  top: 38%; animation-delay: 1.1s; }
.twinkle-dot:nth-child(4)  { left: 36%;  top: 14%; animation-delay: 0.3s;  transform: scale(0.8); }
.twinkle-dot:nth-child(5)  { left: 44%;  top: 80%; animation-delay: 1.6s;  transform: scale(1.2); }
.twinkle-dot:nth-child(6)  { left: 52%;  top: 26%; animation-delay: 0.8s; }
.twinkle-dot:nth-child(7)  { left: 60%;  top: 60%; animation-delay: 1.9s;  transform: scale(0.85); }
.twinkle-dot:nth-child(8)  { left: 68%;  top: 18%; animation-delay: 0.2s;  transform: scale(1.05); }
.twinkle-dot:nth-child(9)  { left: 76%;  top: 70%; animation-delay: 2.2s; }
.twinkle-dot:nth-child(10) { left: 84%;  top: 34%; animation-delay: 0.6s;  transform: scale(0.95); }
.twinkle-dot:nth-child(11) { left: 12%;  top: 50%; animation-delay: 1.4s;  transform: scale(1.15); }
.twinkle-dot:nth-child(12) { left: 90%;  top: 12%; animation-delay: 2.6s;  transform: scale(0.8); }

main, section, .block-container { position: relative; z-index: 1; }
</style>

<!-- Lightweight 12-point twinkle layer -->
<div class="twinkle-layer">
  <span class="twinkle-dot"></span><span class="twinkle-dot"></span><span class="twinkle-dot"></span>
  <span class="twinkle-dot"></span><span class="twinkle-dot"></span><span class="twinkle-dot"></span>
  <span class="twinkle-dot"></span><span class="twinkle-dot"></span><span class="twinkle-dot"></span>
  <span class="twinkle-dot"></span><span class="twinkle-dot"></span><span class="twinkle-dot"></span>
</div>
""", unsafe_allow_html=True)


# ---------- Banner ----------
banner_path = find_asset("assets/banner.webp", "assets/banner.png", "assets/banner.jpg")
if banner_path:
    st.image(str(banner_path), caption="A Garden in Time • Endless Summer", use_container_width=True)
else:
    st.warning("Banner image not found. Place one at `assets/banner.webp|png|jpg`.")


# ---------- Title ----------
st.title("A Garden in Time: Our Endless Summer")
st.markdown("<p class='subtitle'>A digital garden of memory, growth, and light.</p>", unsafe_allow_html=True)

# ---------- Banner ----------
banner_path = find_asset("assets/banner.webp", "assets/banner.png", "assets/banner.jpg")
if banner_path:
    st.image(str(banner_path), caption="A Garden in Time • Endless Summer", use_container_width=True)
else:
    st.warning("Banner image not found. Place one at `assets/banner.webp|png|jpg`.")


# ---------- Enter the Garden Button ----------
st.markdown("<div class='enter-btn'>", unsafe_allow_html=True)
if st.button("🌸 Enter the Garden →", type="primary", use_container_width=True):
    st.switch_page("pages/Timeline.py")
st.markdown("</div>", unsafe_allow_html=True)
