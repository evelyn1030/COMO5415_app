# pages/Timeline.py
from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates  # pip install streamlit-image-coordinates

st.set_page_config(page_title="Garden Timeline • Seven Blooms", page_icon="🗓️", layout="wide")
st.title("Garden Timeline • Seven Blooms")
import streamlit as st
from pathlib import Path


st.markdown("""
### 🌸 Explore the Blooms
Click on the flowers to discover hidden surprises about each milestone!  
*(Currently, only the **first three blooms** are available. More coming soon... 🌱)*
""")

candidates = [Path("assets/timeline.png"), Path("assets/main_poster.png")]
IMG_PATH = next((p for p in candidates if p.exists()), None)
if IMG_PATH is None:
    st.error("Timeline image not found. Put one at assets/timeline.png (or assets/main_poster.png).")
    st.stop()

# 展示宽度（页面里显示的宽度，可随意改）
DISPLAY_WIDTH = 1000

img = Image.open(IMG_PATH)
W, H = img.size

hotspots = [
    {"label": "Bloom 1 • The First Bloom (Debut Day)",        "center_pct": (0.147, 0.156), "r": 70, "page": "pages/Milestone_Formation.py"},
    {"label": "Bloom 2 • The Fiery Bloom (Youth On Fire)",    "center_pct": (0.147, 0.443), "r": 70, "page": "pages/Milestone_OnFire.py"},
    {"label": "Bloom 3 • The Mature Bloom (1st Anniversary)", "center_pct": (0.147, 0.794), "r": 70, "page": "pages/Milestone_Anniversary1st.py"},
    {"label": "Bloom 4 • ——",                                 "center_pct": (0.500, 0.156), "r": 70, "page": "pages/Milestone_4.py"},
    {"label": "Bloom 5 • ——",                                 "center_pct": (0.853, 0.156), "r": 70, "page": "pages/Milestone_5.py"},
    {"label": "Bloom 6 • ——",                                 "center_pct": (0.853, 0.443), "r": 70, "page": "pages/Milestone_6.py"},
    {"label": "Bloom 7 • ——",                                 "center_pct": (0.853, 0.794), "r": 70, "page": "pages/Milestone_7.py"},
]
# =========================================================

debug = st.toggle("Debug: show click coordinates", value=True,
                  help="Turn on to refine centers; paste new percentages back to `hotspots`.")

coords = streamlit_image_coordinates(str(IMG_PATH), width=DISPLAY_WIDTH)

def pct_to_px(cx_pct, cy_pct):
    return cx_pct * W, cy_pct * H

def hit_circle(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2

scale = W / DISPLAY_WIDTH

if coords:
    ox, oy = coords["x"] * scale, coords["y"] * scale
    if debug:
        st.info(f"Clicked display ({coords['x']:.1f}, {coords['y']:.1f}) → original ({ox:.1f}, {oy:.1f}); "
                f"as pct → (x={ox/W:.3f}, y={oy/H:.3f})")

    for hs in hotspots:
        cx, cy = pct_to_px(*hs["center_pct"])
        if hit_circle(ox, oy, cx, cy, hs["r"]):
            st.toast(f"Opening: {hs['label']}")
            try:
                st.switch_page(hs["page"])
            except Exception:
                st.warning(f"Target page not found: `{hs['page']}`. Create it or change the path.")
            st.stop()

    st.warning("Clicked outside all blooms. Use Debug to capture % coords and update `hotspots`.")

with st.sidebar:
    st.subheader("Garden Path")
    for hs in hotspots:
        st.markdown(f"- **{hs['label']}**")
    st.caption("Each bloom marks a milestone in our Endless Summer hydrangea garden.")
