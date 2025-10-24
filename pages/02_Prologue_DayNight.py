import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Prologue • The Garden’s Day and Night",
                   page_icon="🌗", layout="wide")


# ---------- Tabs: Day / Night ----------
day_tab, night_tab = st.tabs(["☀️ Day • Light & Beginnings", "🌙 Night • Reflection & Heritage"])

@st.cache_data(show_spinner=False)
def load_bytes(path: Path) -> bytes:
    """Read file as bytes for audio/video playback."""
    return path.read_bytes() if path.exists() else b''

# ---------------- DAY ----------------
with day_tab:
    st.subheader("A Fox’s Endless Summer Journey")
    st.write(
        "Symbolizes light, hope, and new beginnings. "
        "A gentle, sun-washed moment in our Endless Summer Garden."
    )

    # --- Feature video ---
    day_video = Path("assets/videos/fox_journey.mp4")
    if day_video.exists():
        st.video(load_bytes(day_video), format="video/mp4")
    else:
        st.info("Add the DAY animation video at: `assets/videos/fox_journey.mp4`")

    # --- Ambient audio ---
    day_audio = Path("assets/audio/day_ambience.mp3")
    if day_audio.exists():
        st.audio(load_bytes(day_audio), format="audio/mp3")
    else:
        st.info("Add the DAY ambience audio at: `assets/audio/day_ambience.mp3`")

    # --- Still image ---
    day_img = Path("assets/prologue/day_poster.jpg")
    if day_img.exists():
        with Image.open(day_img) as img:
            st.image(img.copy(), caption="Day • Endless Summer Light", width=520)
    else:
        st.warning("Optional image: place a poster at `assets/prologue/day_poster.jpg`")

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

    # --- Feature video ---
    night_video = Path("assets/prologue/chinese_men_1925_2025.mp4")
    if night_video.exists():
        st.video(load_bytes(night_video), format="video/mp4")
    else:
        st.info("Add the NIGHT feature video at: `assets/prologue/chinese_men_1925_2025.mp4`")

    # --- Ambient audio ---
    night_audio = Path("assets/audio/night_ambience.mp3")
    if night_audio.exists():
        st.audio(load_bytes(night_audio), format="audio/mp3")
    else:
        st.info("Add the NIGHT ambience audio at: `assets/audio/night_ambience.mp3`")

    # --- Still image ---
    night_img = Path("assets/prologue/night_poster.jpg")
    if night_img.exists():
        with Image.open(night_img) as img:
            st.image(img.copy(), caption="Night • Heritage & Quiet Strength", width=520)
    else:
        st.warning("Optional image: place a poster at `assets/prologue/night_poster.jpg`")

    with st.expander("Credits / Notes (Night)"):
        st.markdown("""
- Feature video: *Chinese Men: A Century in Style (1925–2025)* — add source or author attribution  
- Ambience: *Night ambience* (source + license, e.g., Freesound attribution)  
- Archival or fashion references: cite museums or photographers if applicable
        """)
