import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Poster", page_icon="🖼️", layout="wide")
st.title("Poster")


tab_concept, tab_final = st.tabs(["Concept & Symbolism", "Final Poster"])

with tab_concept:
    st.subheader("Concept & Symbolism")
    st.markdown("""
The **poster** is the central art piece of this campaign.  
Its retro illustration style and grainy texture stay consistent with the banner, ensuring a coherent visual system.  

### 🌸 Symbolism
- **Purple-blue hydrangea** → represents the group *Teens in Times*.  
- **Yellow hydrangea** → represents the fans *Popcorns*.  

Both blooms stand side-by-side under a **soft, glowing archway** — a protected, shared space that signifies **mutual support and companionship**.  

### ✨ Layered Messaging
- **“ENDLESS SUMMER”**: the brand promise — our love is an endless summer; our future keeps blooming.  
- **“Our journey never ends. Our bond is an endless summer.”**: sincere reinforcement of this promise.  
- **“I Clearly See You.”**: inspired by *My Altay*. In Kazakh culture, bonds arise from being seen.  
  → This affirms the **mutual recognition and deep connection** between the group and the fans.  
""")

with tab_final:
    st.subheader("Final Poster")
    img_path = Path("assets/main_poster.png")
    if img_path.exists():
        image = Image.open(img_path)
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(image, caption="Campaign Poster", width=700)  # 保持比 milestone 大
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("`assets/main_poster.png` not found. Please place your poster image in the assets folder.")
