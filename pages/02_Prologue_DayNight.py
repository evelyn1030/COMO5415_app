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
        day_video = Path("assets/videos/fox_journey.mp4")
        if day_video.exists():
            st.video(load_bytes(day_video), format="video/mp4")
        else:
            st.info("Add the DAY video at: assets/videos/fox_journey.mp4")

    with colR:
        st.subheader("A Fox’s Endless Summer Journey")
        st.markdown("""
**What you’ll see**  
A sun-washed moment where a small fox takes its first brave steps in the hydrangea garden.

**Why it matters**  
Day represents *beginnings* — light, hope, and the courage to start.

**Design notes**  
• Warm tone, airy pacing  
• Soft grain + gentle motion  
• Focus on *growth* and *connection*
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
        st.subheader("Chinese Men: A Century in Style (1925–2025)")
        st.markdown("""
**What you’ll see**  
A calm, archival-style montage tracing silhouettes, fabric, and posture across a century.

**Why it matters**  
Night symbolizes *reflection* — heritage, quiet strength, and roots that deepen.

**Design notes**  
• Grounded tone, steady rhythm  
• Subtle texture overlays  
• Emphasis on *continuity* and *dignity*
        """)
