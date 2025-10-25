# pages/Storyboard.py
import streamlit as st
from pathlib import Path
from PIL import Image
from Config import show_banner

st.set_page_config(page_title="Website & Animation Storyboard", page_icon="📝", layout="wide")

st.title("Storyboard • Website & Animation")

# ---------- Banner ----------
show_banner()

# ---------- Website Storyboard ----------
st.header("Website Storyboard (Overall Web Design)")

img_path = Path("assets/website_flowchart.png")
if img_path.exists():
    image = Image.open(img_path)
    st.image(image, caption="Website Structure Overview", use_column_width=True)
else:
    st.warning("`assets/website_flowchart.png` not found. Please place it in the assets folder.")

st.subheader("Framework")
st.markdown("""
**Header** – Displays the project title *A Garden in Time: Endless Summer* and sets a calm, poetic tone for the entire site.  
**Sidebar** – Provides persistent navigation, featuring the logo and clear page hierarchy: *Garden*, *Blooms*, and *Project Assets*.  
Together, they create a consistent visual frame that makes the experience intuitive and immersive.
""")

st.subheader("Main Pages")
st.markdown("""
**Garden Overview (Homepage)**  
Introduces the concept and mood of the project — a poetic garden that grows through light and memory. Serves as the narrative entry point for visitors.  

**Prologue • The Garden’s Day and Night**  
Combines animation and video to express the emotional duality of *hope* and *reflection*.  

**Timeline • Seven Blooms**  
An interactive timeline of the creative process, where seven symbolic blooms represent different stages of growth and collaboration.  

**Blooms 1–7**  
Each Bloom page presents a milestone with mini posters, short texts, and embedded media. The sequence mirrors emotional and creative progression.  

**Project Assets**  
Archives key visual materials — *Banner*, *Poster*, and *Storyboard* — connecting the narrative world to its design and production foundation.
""")


# ---------- Animation Storyboard ----------
st.header("Animated Storyboard • The Fox’s Endless Summer Journey")

story_img = Path("assets/storyboard1.png")
if story_img.exists():
    image = Image.open(story_img)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image(image, caption="Storyboard — The Fox’s Endless Summer Journey", width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("`assets/storyboard1.png` not found. Please place it in the assets folder.")

st.markdown("""
This animated short tells a story of loneliness and growth.  
A little fox, lost under an apple tree, meets a glowing butterfly that leads it into a sea of hydrangeas —  
a metaphor for *Teens in Times* and the healing power of music and friendship.

**Act 1 – Loneliness under the Apple Tree**  
A quiet field, muted sky, a fox sits alone. *Emotion:* solitude, longing.  

**Act 2 – A Butterfly’s Guidance**  
A small glowing butterfly dances before the fox. *Emotion:* curiosity, awakening.  

**Act 3 – Encounter in the Summer Field**  
The fox follows into the radiant hydrangea sea — *Endless Summer*.  

**Act 4 – Song and Friendship**  
The hydrangea sings, petals swaying like music. *Emotion:* joy, healing.  

**Act 5 – Sunset and Promise**  
They watch the sunset together, sharing warmth and courage.  

**Act 6 – Toward the Peak**  
The fox sets off toward the distant mountaintop.  
**Final Message:** *Our journey never ends. To be continued.*
""")
