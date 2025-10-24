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

# ---------- Tabs: Day / Night ----------
day_tab, night_tab = st.tabs(["☀️ Day • Light & Beginnings", "🌙 Night • Reflection & Heritage"])

# ---------------- DAY ----------------
with day_tab:
    st.subheader("A Fox’s Endless Summer Journey")
    st.write(
        "Symbolizes light, hope, and new beginnings. "
        "A gentle, sun-washed moment in our Endless Summer Garden."
    )

    # --- Video placeholder (animation) ---
    day_video = Path("assets/videos/fox_journey.mp4")
    if day_video.exists():
        st.video(str(day_video))
    else:
        st.info("Add the DAY animation video at: `assets/videos/fox_journey.mp4`")

    # --- Ambient audio (manual play for browser compatibility) ---
    day_audio = Path("assets/audio/day_ambience.mp3")
    if day_audio.exists():
        st.audio(str(day_audio))
    else:
        st.info("Add the DAY ambience audio at: `assets/audio/day_ambience.mp3`")

    # --- Still image(s) ---
    day_img = Path("assets/prologue/day_poster.jpg")
    if day_img.exists():
        img = Image.open(day_img)
        st.image(img, caption="Day • Endless Summer Light", use_column_width=False, width=520)
    else:
        st.warning("Optional image: place a poster at `assets/prologue/day_poster.jpg`")

    # Notes block for attribution
    with st.expander("Credits / Notes (Day)"):
        st.markdown("""
- Animation: *A Fox’s Endless Summer Journey* (add your credit or self-made note)  
- Ambience: (source + license, e.g., Freesound attribution)  
- Any supporting visuals: list sources here
        """)

# ---------------- NIGHT ----------------
with night_tab:
    st.subheader("Chinese Men: A Century in Style (1925–2025)")
    st.write(
        "Represents reflection, heritage, and inner strength — "
        "night as a quiet soil where roots deepen."
    )

    # --- Video placeholder (montage/essay film) ---
    night_video = Path("assets/videos/chinese_men_1925_2025.mp4")
    if night_video.exists():
        st.video(str(night_video))
    else:
        st.info("Add the NIGHT feature video at: `assets/videos/chinese_men_1925_2025.mp4`")

    # --- Ambient audio (manual play) ---
    night_audio = Path("assets/audio/night_ambience.mp3")
    if night_audio.exists():
        st.audio(str(night_audio))
    else:
        st.info("Add the NIGHT ambience audio at: `assets/audio/night_ambience.mp3`")

    # --- Still image(s) ---
    night_img = Path("assets/prologue/night_poster.jpg")
    if night_img.exists():
        img = Image.open(night_img)
        st.image(img, caption="Night • Heritage & Quiet Strength", use_column_width=False, width=520)
    else:
        st.warning("Optional image: place a poster at `assets/prologue/night_poster.jpg`")

    with st.expander("Credits / Notes (Night)"):
        st.markdown("""
- Video essay / montage: add author + year + license  
- Ambience: (source + license)  
- Archival or fashion references: cite image owners / museums if used
        """)

# ---------- Back / Next nav hints ----------
st.divider()
cols = st.columns([1,1,1,4])
with cols[0]:
    st.page_link("app.py", label="← Overview")
with cols[1]:
    st.page_link("pages/03_Milestone_Formation.py", label="Next: Bloom 1 →", disabled=False)
