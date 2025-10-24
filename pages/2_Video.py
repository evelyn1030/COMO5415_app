import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Animation", page_icon="🎬", layout="wide")
st.title("Animation · Coming Soon")

st.markdown("""
## 🌸 Coming Soon — *The Garden in Motion*

This section will soon showcase the **animated timeline of the Endless Summer Garden**.  
Each bloom will appear one by one, representing milestones in the journey of Teens in Times.  

✨ *Our story is still unfolding, and the animation will bring the blooms to life.*  
""")


img_path = Path("assets/animation_placeholder.png")
if img_path.exists():
    st.image(str(img_path), caption="Coming Soon — The Garden in Motion", width="stretch")
else:
    st.info("Animation is still in progress. Please check back later!")
