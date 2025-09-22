import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Banner", page_icon="🏷️", layout="wide")
st.title("Banner")

# 设置 tab
tab1, tab2 = st.tabs(["Concept & Symbolism", "Final Banner"])

with tab1:
    st.subheader("Concept & Symbolism")
    st.markdown("""
The banner serves as a powerful visual gateway for the campaign on social media and digital platforms.  
Its design is guided by a clear set of aesthetic and conceptual principles.  

The banner adopts a distinct **retro illustration style** with a prominent grainy texture, giving it a nostalgic and timeless quality.  
The two hydrangeas, mirroring the meaning in the logo, anchor the foreground, while a stylized archway symbolizes a shared, protected space.  

The color scheme features a blend of **warm, sun-kissed hues and cooler blues and greens**.  
This palette evokes a gentle summer atmosphere while creating a soft, vintage aesthetic.  

👉 Regarding the introduction of the text on the banner, the detailed explanation is reflected in the **Poster** section.
""")

with tab2:
    st.subheader("Final Banner")
    img_path = Path("assets/banner.png")
    if img_path.exists():
        image = Image.open(img_path)
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(image, caption="Campaign Banner", width=700)  # 居中 + 稍大
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("`assets/banner.png` not found. Please place your banner image in the assets folder.")
