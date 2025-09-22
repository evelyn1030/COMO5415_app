# app.py
import streamlit as st

st.set_page_config(
    page_title="A Garden in Time: Our Endless Summer",
    page_icon="🌸",
    layout="wide",
)

# Sidebar with project logo
with st.sidebar:
    st.image("assets/Logo.png", caption="Endless Summer • Project Logo", use_container_width=True)

# Navigation structure
pages = {
    "Garden": [
        st.Page("pages/Story.py",    title="Overview"),
        st.Page("pages/Timeline.py", title="Timeline • Seven Blooms"),
    ],

    "Blooms": [
        st.Page("pages/Milestone_Formation.py",      title="Bloom 1 • The First Bloom (Debut Day)"),
        st.Page("pages/Milestone_OnFire.py",         title="Bloom 2 • The Fiery Bloom (Youth On Fire)"),
        st.Page("pages/Milestone_Anniversary1st.py", title="Bloom 3 • The Mature Bloom (1st Anniversary)"),
        # Future extensions:
        # st.Page("pages/Milestone_Bloom4.py", title="Bloom 4 • ..."),
        # st.Page("pages/Milestone_Bloom5.py", title="Bloom 5 • ..."),
        # st.Page("pages/Milestone_Bloom6.py", title="Bloom 6 • ..."),
        # st.Page("pages/Milestone_Bloom7.py", title="Bloom 7 • ..."),
    ],

    "Project Assets": [
        st.Page("pages/banner.py",  title="Banner"),
        st.Page("pages/Poster.py",  title="Poster"),
        st.Page("pages/2_Video.py", title="Animation"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()
