# pages/02_Prologue_DayNight.py
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Prologue • The Garden’s Day and Night",
                   page_icon="🌗", layout="wide")

# ---------- Minimal CSS: fade-in + gentle gradient ----------
st.markdown("""
<style>
/* page fade-in */
.main > div { animation: fadein 0.9s ease-in; }
@keyframes fadein { from {opacity:0} to {opacity:1} }

/* soft card */
.garden-card {
  background: rgba(255,255,255,0.6);
  backdrop-filter: blur(6px);
  border-radius: 16px; padding: 18px 22px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}

/* section heading */
h2, h3 { margin-top: 0.2rem; }

/* keep images moderate width */
.garden-img { display:block; margin: 8px auto 2px auto; max-width: 520px; border-radius: 12px; }

/* gradient band under title */
.garden-band {
  height: 8px; width: 100%;
  background: linear-gradient(90deg, #b9e6ff, #f7c9ff, #b9e6ff);
  border-radius: 999px; margin: 4px 0 18px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("Prologue • The Garden’s Day and Night")
st.caption("After the Overview → the garden’s heartbeat before the blooms.")
st.markdown('<div class="garden-band"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="garden-card">
<h3>Purpose</h3>
<p>To represent the emotional heartbeat of the project — how both <b>light</b> and <b>darkness</b> nurture growth.</p>
</div>
""", unsafe_allow_html=True)

# ---------- helper: safe byte loader for media ----------
@st.cache_data(show_spinner=False)
def load_bytes(path: Path) -> bytes:
    return path.read_bytes() if path.exists() else b""

# ---------- Tabs: Day / Night ----------
day_tab, night_tab = st.tabs(["☀️ Day • Light & Beginnings", "🌙 Night • Reflection & Heritage"])

# ---------------- DAY ----------------
with day_tab:
    colL, colR = st.columns([7, 5], gap="large")

    with colL:
        # Use the GitHub LFS link instead of local file
        st.video("https://media.githubusercontent.com/media/evelyn1030/COMO5415_app/main/assets/prologue/fox_journey.mp4")

    with colR:
        st.subheader("A Fox’s Endless Summer Journey")
        st.markdown("""
**What you’ll see**  
A lone fox wanders through shifting light until it meets a blooming hydrangea —  
a symbol of encounter, understanding, and shared growth.  
Together they journey toward the mountain, where dreams and promises intertwine.

**Why it matters**  
The story reflects the bond between fans and artists —  
two worlds connected by empathy and hope, walking side by side toward the same summit.  
It captures how light and companionship transform solitude into courage.

**Design notes**  
• Dreamlike palette blending sunrise warmth and pastel glow  
• Gentle rhythm and emotional pacing echoing companionship  
• Visual motifs of *growth, resonance,* and *spiritual connection*
        """)


# ---------------- NIGHT ----------------
with night_tab:
    colL, colR = st.columns([7, 5], gap="large")

    with colL:
        night_video = Path("assets/prologue/chinese_men_1925_2025.mp4")
        if night_video.exists():
            st.video(load_bytes(night_video), format="video/mp4")
        else:
            st.info("Add the NIGHT video at: assets/prologue/chinese_men_1925_2025.mp4")

    with colR:
        st.subheader("Chinese People: A Century in Motion (1925–2025)")
        st.markdown("""
    **What you’ll see**  
    A century in motion — from linen robes to streetwear,  
    from silent portraits to confident stances.  
    Set to a remix of the Yunnan folk song *Mi Du Shan Ge*,  
    this fast-cut montage transforms tradition into pulse and rhythm.

    **Why it matters**  
    Night stands for *reflection* — not stillness, but awakening.  
    The film captures how Chinese people have carried heritage into modern life,  
    reframing identity through movement, music, and style.

    **Design notes**  
    • Dynamic pacing synced with rhythmic beats  
    • Visual layering of past and present textures  
    • Focus on *heritage, vitality,* and *cultural rebirth*
        """)

