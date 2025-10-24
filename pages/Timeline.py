# pages/Timeline.py
from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import os

st.set_page_config(page_title="Garden Timeline • Seven Blooms", page_icon="🗓️", layout="wide")

# ---------- Header ----------
st.title("Garden Timeline • Seven Blooms")
st.markdown("""
### 🌸 Explore the Blooms  
Click the flowers to explore each milestone of *Endless Summer*.  
""")

# ---------- Helper ----------
def page_path(*candidates: str) -> str:
    """Return the first existing path from candidates; otherwise the first (for clarity)."""
    for p in candidates:
        if os.path.exists(p):
            return p
    return candidates[0]

# ---------- Load image ----------
candidates_img = [Path("assets/timeline.png"), Path("assets/main_poster.png")]
IMG_PATH = next((p for p in candidates_img if p.exists()), None)

if IMG_PATH is None:
    st.error("❌ Timeline image not found. Add one at `assets/timeline.png` or `assets/main_poster.png`.")
    st.stop()

# 🔧 Load and resize image to reduce load time
DISPLAY_WIDTH = 880  # smaller than before (was 980)
img = Image.open(IMG_PATH)
W, H = img.size
ratio = DISPLAY_WIDTH / W
H_display = int(H * ratio)

# ---------- Page Paths ----------
p_b1 = page_path("pages/Milestone_Formation.py")
p_b2 = page_path("pages/Milestone_OnFire.py")
p_b3 = page_path("pages/Milestone_Anniversary1st.py")
p_b4 = page_path("pages/Milestone_SpringGala.py")
p_b5 = page_path("pages/Milestone_DancingElephants.py")
p_b6 = page_path("pages/Milestone_Haikou.py")
p_b7 = page_path("pages/Milestone_Chongqing5th.py")

# ---------- Hotspots ----------
hotspots = [
    {"label": "Bloom 1 • The First Bloom (Debut Day)",        "center_pct": (0.11, 0.15), "r": 55, "page": p_b1},
    {"label": "Bloom 2 • The Fiery Bloom (Youth On Fire)",    "center_pct": (0.11, 0.40), "r": 55, "page": p_b2},
    {"label": "Bloom 3 • The Mature Bloom (1st Anniversary)", "center_pct": (0.11, 0.69), "r": 55, "page": p_b3},
    {"label": "Bloom 4 • The Radiant Bloom (Spring Festival Gala)", "center_pct": (0.50, 0.13), "r": 60, "page": p_b4},
    {"label": "Bloom 5 • The Transforming Bloom (The Age of Dancing Elephants)", "center_pct": (0.89, 0.15), "r": 55, "page": p_b5},
    {"label": "Bloom 6 • The Boundless Bloom (Haikou Concert)", "center_pct": (0.89, 0.40), "r": 55, "page": p_b6},
    {"label": "Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)", "center_pct": (0.89, 0.69), "r": 55, "page": p_b7},
]

# ---------- Interaction (do hit-test in DISPLAY space) ----------
coords = streamlit_image_coordinates(str(IMG_PATH), width=DISPLAY_WIDTH)

def pct_to_px_display(cx_pct, cy_pct):
    return cx_pct * DISPLAY_WIDTH, cy_pct * H_display

def hit_circle_display(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2

if coords:
    ox, oy = float(coords["x"]), float(coords["y"])  # click in display-space
    for hs in hotspots:
        cx, cy = pct_to_px_display(*hs["center_pct"])  # center in display-space
        r = hs["r"]  # radius also in display-space pixels
        if hit_circle_display(ox, oy, cx, cy, r):
            st.toast(f"Opening: {hs['label']}")
            try:
                st.switch_page(hs["page"])
            except Exception:
                st.warning(f"⚠️ Target page not found: `{hs['page']}`.")
            st.stop()


# ---------- Buttons (reduced layout) ----------
st.divider()
st.markdown("### Quick Access")

col1, col2, col3 = st.columns(3)
buttons = [col1, col2, col3] * 3  # repeat columns

for i, hs in enumerate(hotspots):
    with buttons[i]:
        if st.button(hs["label"], width="stretch"):
            try:
                st.switch_page(hs["page"])
            except Exception:
                st.warning(f"⚠️ Target page not found: `{hs['page']}`.")

# ---------- Sidebar ----------
with st.sidebar:
    st.subheader("Garden Path")
    for hs in hotspots:
        st.markdown(f"- {hs['label']}")
    st.caption("Each bloom marks a milestone in our Endless Summer journey.")
