# Config.py
import streamlit as st
from pathlib import Path
from PIL import Image

def show_banner():
    """Display the campaign banner at the top of every page."""
    img_path = Path("assets/banner.png")
    if img_path.exists():
        image = Image.open(img_path)
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("`assets/banner.png` not found. Please place it in the assets folder.")
