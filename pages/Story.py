# pages/Story.py
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Website Storyboard", page_icon="📝", layout="wide")
st.title("Website Storyboard (Overall Web Design)")

# --- Part1 ---
img_path = Path("assets/website_flowchart.png")
if img_path.exists():
    image = Image.open(img_path)
    st.image(image, caption="Website Flowchart", use_container_width=True)
else:
    st.warning("`assets/website_flowchart.png` not found. Please place it in the assets folder.")

st.subheader("Framework")
st.markdown("""
**Header**: project title *A Garden in Time: Endless Summer* + navigation menu (Garden Overview, Timeline, Blooms, Project Assets).  
**Footer**: credits + course/project info.  
**Sidebar (Streamlit)**: persistent navigation (logo + page list).
""")

st.subheader("Main Pages")
st.markdown("""
**Garden Overview (Homepage)**  
- Content: Logo, tagline, introduction of “Endless Summer” concept.  
- Goal: provide entry point and establish metaphor of the “digital garden.”  

**Garden Timeline (Seven Blooms)**  
- Interactive poster with 7 clickable flowers.  
- Textual prompt: *“Click the flowers to explore milestones.”*  
- Goal: playful entry into milestone memories.  

**Bloom Pages (1–3 implemented, 4–7 placeholders)**  
- Still Image: event mini-poster (retro grainy style).  
- Textual Narrative: short poetic text about the milestone.  
- Video (planned): curated clip (performance, anniversary, etc.).  
- Audio (planned): snippets of songs or fan chants.  
- Goal: evoke memory and emotion of each milestone.  

**Project Assets (Banner, Poster, Animation)**  
- Dedicated sub-pages showcasing key visuals.  
- Banner and Poster: emphasize symbolic design choices.  
- Animation: placeholder now, to be replaced with motion graphic/video.  
- Goal: highlight project’s final deliverables and unify style.
""")

# --- Part 2: Animated Storyboard -------------------------------------------
import streamlit as st
from pathlib import Path
from PIL import Image

st.header("Animated Storyboard • The Fox’s Endless Summer Journey")

img_path = Path("assets/storyboard1.png")
if img_path.exists():
    image = Image.open(img_path)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="Storyboard — The Fox’s Endless Summer Journey", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("`assets/storyboard1.png` not found. Please place it in the assets folder.")

st.markdown("""
**Act 1 — Loneliness under the Apple Tree**  
A quiet field. A heavy apple tree at center. A small fox sits with its back to us, the sky a muted gray.  
*Emotion:* loneliness, confusion, longing.  
*On-screen:* *Alone, under the apple tree.*

**Act 2 — A Butterfly’s Guidance**  
A tiny glowing butterfly slips from the leaves and dances before the fox. The fox looks up; curiosity and hope flicker.  
*Emotion:* curiosity, calling, first hope.  
*On-screen:* *A tiny light appears.*

**Act 3 — Encounter in the Summer Field**  
The fox follows into a radiant hydrangea sea — **Endless Summer**. One bloom shines brighter than the rest: a symbol of *Teens in Times*.  
*Emotion:* surprise, discovery, meeting.  
*On-screen:* *Into the endless summer.*

**Act 4 — Song and Friendship**  
The fox and the special hydrangea stand side-by-side. Petals sway like music; a gentle song fills the air.  
*Emotion:* friendship, joy, healing.  
*On-screen:* *A song that heals, a bond that grows.*

**Act 5 — Sunset and a Promise**  
They watch the sunset together; the sky glows in orange and violet. The fox lifts a small travel bundle, eyes bright with resolve.  
*Emotion:* warmth, encouragement, new resolve.  
*On-screen:* *Together, we watch the setting sun.*

**Act 6 — Toward the Peak**  
The fox sets out toward a distant mountaintop. The hydrangea remains, smiling across the field. Dawn lights the ridge.  
*Emotion:* determination, shared growth, never giving up.  
**Final card:** *Our journey never ends. See you at the top. To be continued.*
""")
