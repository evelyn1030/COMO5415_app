# pages/Overview.py
import streamlit as st

st.set_page_config(page_title="Overview", page_icon="🌸", layout="wide")

st.title("A Garden in Time: Our Endless Summer")

st.markdown("""
Welcome to **Endless Summer**, a digital garden of memories.  
Here, each bloom represents a milestone of growth, joy, and togetherness.  

Explore the pages to follow the journey — from the very first seedling to the radiant blooms of today.
""")

st.markdown("### Ready to explore the garden?")
if st.button("🌸 Enter the Garden →", type="primary", use_container_width=True):
    st.switch_page("pages/Timeline.py")
