# pages/Timeline.py
from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates  # pip install streamlit-image-coordinates
import os, json

st.set_page_config(page_title="Garden Timeline • Seven Blooms", page_icon="🗓️", layout="wide")
st.title("Garden Timeline • Seven Blooms")

st.markdown("""
### 🌸 Explore the Blooms
Click the flowers to open each milestone — or use the buttons below if you prefer.  
*(Right now all seven blooms are wired up.)*
""")

# ---------- helpers ----------
def page_path(*candidates: str) -> str:
    """Return the first existing path from candidates; otherwise the first (to expose error)."""
    for p in candidates:
        if os.path.exists(p):
            return p
    return candidates[0]

# ---- Load image safely ----
candidates_img = [Path("assets/timeline.png"), Path("assets/main_poster.png")]
IMG_PATH = next((p for p in candidates_img if p.exists()), None)

if IMG_PATH is None:
    st.error("❌ Timeline image not found. Add one at `assets/timeline.png` or `assets/main_poster.png`.")
    st.stop()

# Display image (choose a pleasant width; keep under 1100 for laptop screens)
DISPLAY_WIDTH = 980
img = Image.open(IMG_PATH)
W, H = img.size

# ---------- Target page paths (robust to naming variants) ----------
p_b1 = page_path("pages/Milestone_Formation.py")  # stable
p_b2 = page_path("pages/Milestone_OnFire.py")
p_b3 = page_path("pages/Milestone_Anniversary1st.py")

p_b4 = page_path(
    "pages/Milestone_SpringGala.py",
    "pages/Milestone SpringGala.py",
    "pages/Milestone 4 – Spring Bloom • CCTV Spring Festival Gala.py",
)
p_b5 = page_path(
    "pages/Milestone_DancingElephants.py",
    "pages/Milestone 5 – The Age of Dancing Elephants.py",
)
p_b6 = page_path(
    "pages/Milestone_Haikou.py",
    "pages/Milestone Haikou.py",
    "pages/Milestone 6 – Haikou Concert (First Stadium Show).py",
)
p_b7 = page_path(
    "pages/Milestone_Chongqing5th.py",
    "pages/Milestone 7 – Chongqing Concert (5th Anniversary).py",
)

# ---------- Hotspot configuration ----------
# center_pct = (x_pct, y_pct) in ORIGINAL image coordinates (0~1)
hotspots = [
    {"key": "b1", "label": "Bloom 1 • The First Bloom (Debut Day)",        "center_pct": (0.11, 0.15), "r": 65, "page": p_b1},
    {"key": "b2", "label": "Bloom 2 • The Fiery Bloom (Youth On Fire)",    "center_pct": (0.11, 0.40), "r": 65, "page": p_b2},
    {"key": "b3", "label": "Bloom 3 • The Mature Bloom (1st Anniversary)", "center_pct": (0.11, 0.69), "r": 65, "page": p_b3},
    {"key": "b4", "label": "Bloom 4 • The Radiant Bloom (Spring Festival Gala)", "center_pct": (0.50, 0.13), "r": 70, "page": p_b4},
    {"key": "b5", "label": "Bloom 5 • The Transforming Bloom (The Age of Dancing Elephants)", "center_pct": (0.89, 0.15), "r": 65, "page": p_b5},
    {"key": "b6", "label": "Bloom 6 • The Boundless Bloom (Haikou Concert)", "center_pct": (0.89, 0.40), "r": 65, "page": p_b6},
    {"key": "b7", "label": "Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)", "center_pct": (0.89, 0.69), "r": 65, "page": p_b7},
]


# ---------- Interaction image ----------
debug = st.toggle("Debug: show click coordinates & export hotspots", value=False,
                  help="Turn on to refine centers; paste new percentages back to `hotspots`.")

coords = streamlit_image_coordinates(str(IMG_PATH), width=DISPLAY_WIDTH)

def pct_to_px(cx_pct, cy_pct):
    return cx_pct * W, cy_pct * H

def hit_circle(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2

# scale factor: displayed → original
scale = W / DISPLAY_WIDTH

if coords:
    ox, oy = coords["x"] * scale, coords["y"] * scale
    if debug:
        st.info(
            f"Clicked display ({coords['x']:.1f}, {coords['y']:.1f}) → original ({ox:.1f}, {oy:.1f});  "
            f"as pct → (x={ox/W:.3f}, y={oy/H:.3f})"
        )

    # hit-test all blooms
    for hs in hotspots:
        cx, cy = pct_to_px(*hs["center_pct"])
        if hit_circle(ox, oy, cx, cy, hs["r"]):
            st.toast(f"Opening: {hs['label']}")
            try:
                st.switch_page(hs["page"])
            except Exception:
                st.warning(f"⚠️ Target page not found: `{hs['page']}`. Create it or adjust the path.")
            st.stop()

    if debug:
        st.warning("Clicked outside all blooms. Adjust centers with the percent readout above.")
    else:
        st.info("Tip: Try the petals! Or use the buttons below to open each bloom.")

# ---------- Accessible fallback: open via buttons (and page links) ----------
st.divider()
cols = st.columns(4)
for i, hs in enumerate(hotspots):
    with cols[i % 4]:
        if st.button(f"Open {hs['key'].upper()} →", key=f"btn_{hs['key']}", use_container_width=True):
            try:
                st.switch_page(hs["page"])
            except Exception:
                st.warning(f"⚠️ Target page not found: `{hs['page']}`.")

# also provide page_link list (nice on mobile)
st.markdown("#### Quick links")
links = []
for hs in hotspots:
    try:
        links.append(st.page_link(hs["page"], label=hs["label"]))
    except Exception:
        st.write(f"- *(missing)* {hs['label']} — `{hs['page']}`")

# ---------- Sidebar navigation / legend ----------
with st.sidebar:
    st.subheader("Garden Path")
    for hs in hotspots:
        st.markdown(f"- **{hs['label']}**")
    st.caption("Each bloom marks a milestone in our Endless Summer hydrangea garden.")

# ---------- Debug export ----------
if debug:
    st.divider()
    st.markdown("##### Current hotspot centers (copy back into code)")
    export = [
        {"label": hs["label"], "center_pct": hs["center_pct"], "r": hs["r"]}
        for hs in hotspots
    ]
    st.code(json.dumps(export, indent=2))
