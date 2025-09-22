# app.py
import streamlit as st

st.set_page_config(
    page_title="A Garden in Time: Our Endless Summer",
    page_icon="🌸",
    layout="wide",
)

with st.sidebar:
    st.image("assets/Logo.png", caption="Endless Summer • Project Logo", use_container_width=True)

pages = {
    "Garden": [  # 原 Project
        st.Page("pages/Story.py",    title="Garden Overview"),                 # 原 Project Description / Storyboard
        st.Page("pages/banner.py",   title="Banner"),
        st.Page("pages/Poster.py",   title="Poster"),
        st.Page("pages/Timeline.py", title="Garden Timeline • Seven Blooms"),
        st.Page("pages/2_Video.py",  title="Animation"),
    ],
    "Blooms": [  # 原 Milestones
        st.Page("pages/Milestone_Formation.py",      title="Bloom 1 • The First Bloom (Debut Day)"),
        st.Page("pages/Milestone_OnFire.py",         title="Bloom 2 • The Fiery Bloom (Youth On Fire)"),
        st.Page("pages/Milestone_Anniversary1st.py", title="Bloom 3 • The Mature Bloom (1st Anniversary)"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()
