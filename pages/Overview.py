# pages/Overview.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Overview • A Garden in Time", page_icon="🌸", layout="wide")

# ---------- Animated glowing background + base styles ----------
st.markdown("""
<style>
body {
  background:
    radial-gradient(circle at 25% 25%, rgba(255,225,240,0.65) 0%, transparent 40%),
    radial-gradient(circle at 75% 75%, rgba(220,235,255,0.55) 0%, transparent 45%),
    radial-gradient(circle at 50% 100%, rgba(255,240,220,0.55) 0%, transparent 60%),
    linear-gradient(180deg, #fffafc 0%, #f3f9ff 100%);
  background-size: 200% 200%;
  animation: glowmove 18s ease-in-out infinite alternate;
}

/* soft motion of light spots */
@keyframes glowmove {
  0%   { background-position: 0% 0%, 100% 100%, 50% 50%, 0% 0%; }
  100% { background-position: 100% 100%, 0% 0%, 50% 50%, 0% 100%; }
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
    backdrop-filter: blur(8px);
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

# ---------- Helper ----------
def find_asset(*names: str) -> Path | None:
    for n in names:
        p = Path(n)
        if p.exists():
            return p
    return None

# ---------- Banner ----------
banner_path = find_asset("assets/banner.webp", "assets/banner.png", "assets/banner.jpg")
if banner_path:
    st.image(str(banner_path), caption="A Garden in Time • Endless Summer", width="stretch")
else:
    st.warning("Banner image not found. Place one at `assets/banner.webp|png|jpg`.")

# ---------- Title ----------
st.title("A Garden in Time: Our Endless Summer")
st.markdown("<p class='subtitle'>A digital garden of memory, growth, and light.</p>", unsafe_allow_html=True)

# ---------- Poetic Narrative (left) + Poster (right) ----------
col_left, col_right = st.columns([7, 5], gap="large")

with col_left:
    st.markdown("""
<div class="poetic-block">
In this digital garden, every bloom holds a memory.<br/>
Some are tender and new, like the first light of spring;<br/>
some carry the warmth of summer, glowing with laughter and song.<br/><br/>

<b>A Garden in Time</b> is not just a website —<br/>
it is a living archive of <i>Endless Summer</i>,<br/>
where design, sound, and motion grow together like flowers in the same soil.<br/><br/>

Each petal remembers a moment:<br/>
the first debut, the trembling stage lights,<br/>
the voices that met in the dark and learned to sing as one.<br/><br/>

This garden was built for those who once stood under the same sky —<br/>
for the dreamers, the believers,<br/>
the ones who kept their hearts open even when the seasons changed.<br/><br/>

Here, light and shadow coexist.<br/>
Growth is not always gentle, yet it is always beautiful.<br/>
Step inside, and you may find pieces of your own story<br/>
rooted in the soil of time, still alive, still blooming.
</div>
""", unsafe_allow_html=True)

with col_right:
    poster_path = find_asset(
        "assets/main_poster.webp",
        "assets/main_poster.png",
        "assets/poster.png",
        "assets/poster.jpg"
    )
    if poster_path:
        st.image(str(poster_path), caption="Project Poster", width="stretch")
    else:
        st.info("Poster not found. Add one at `assets/main_poster.webp|png|jpg`.")

# ---------- Enter the Garden Button ----------
st.markdown("<div class='enter-btn'>", unsafe_allow_html=True)
if st.button("🌸 Enter the Garden →", type="primary", width="stretch"):
    st.switch_page("pages/02_Prologue_DayNight.py")
st.markdown("</div>", unsafe_allow_html=True)
