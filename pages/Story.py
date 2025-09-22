# pages/Story.py
import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Website Storyboard", page_icon="📝", layout="wide")
st.title("Website Storyboard (Overall Web Design)")

# --- 第一部分：网站流程图 ---
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

# --- 第二部分：动画分镜 ---
st.header("Animated Storyboard (Six Acts)")

img_path2 = Path("assets/storyboard1.png")
if img_path2.exists():
    image2 = Image.open(img_path2)
    st.image(image2, caption="Animated Storyboard", use_container_width=True)
else:
    st.warning("`assets/storyboard1.png` not found. Please place it in the assets folder.")

st.markdown("""
This six-act animated storyboard tells a visual story of growth and hope, framing the relationship between the fans and the group as a never-ending journey.

**Confusion and Waiting (Act 1):** The story begins in a dark, uncertain space filled with mist and confusion, symbolizing the start of the journey and past challenges.  

**Hope and Rebirth (Act 2):** A single drop of rain breaks the darkness, bringing hope and new beginnings, marking a turning point.  

**Meeting and Growth (Act 3):** The rain nurtures a splendid field of hydrangeas, representing the meeting and shared growth of the group and their fans. Two special flowers are highlighted as the journey's protagonists.  

**Warmth and Unity (Act 4):** The climax unfolds in the gentle light of a sunset, creating a warm and peaceful scene that symbolizes the beauty and unity found after overcoming obstacles.  

**A New Beginning (Act 5):** The sun sets, but a light of dawn appears in the distance, foreshadowing a new chapter filled with both challenges and hope.  

**An Eternal Promise (Act 6):** The animation ends by focusing on the road ahead, concluding with the powerful message: *"Our journey never ends. To be continued."* This perfectly captures the core spirit of the "growing-up idol" genre and the infinite possibilities of their shared path.  

This storyboard is not just a visual guide; it's an emotional narrative that translates abstract concepts into a tangible experience for the audience.
""")
