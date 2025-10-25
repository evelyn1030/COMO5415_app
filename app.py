import streamlit as st

st.set_page_config(
    page_title="A Garden in Time: Our Endless Summer",
    page_icon="🌸",
    layout="wide",
)

with st.sidebar:
    st.image("assets/Logo.png",
             caption="Endless Summer • Project Logo",
             width="stretch")

pages = {
    "Garden": [
        st.Page("pages/Overview.py", title="Overview"),
        st.Page("pages/02_Prologue_DayNight.py", title="Prologue • The Garden’s Day and Night"),
        st.Page("pages/Timeline.py", title="Timeline • Seven Blooms"),
    ],

    "Blooms": [
        st.Page("pages/Milestone_Formation.py", title="Bloom 1 • The First Bloom (Debut Day)"),
        st.Page("pages/Milestone_OnFire.py", title="Bloom 2 • The Fiery Bloom (Youth On Fire)"),
        st.Page("pages/Milestone_Anniversary1st.py", title="Bloom 3 • The Mature Bloom (1st Anniversary)"),
        st.Page("pages/Milestone_SpringGala.py", title="Bloom 4 • The Radiant Bloom (Spring Festival Gala)"),
        st.Page("pages/Milestone_DancingElephants.py", title="Bloom 5 • The Transforming Bloom (The Age of Dancing Elephants)"),
        st.Page("pages/Milestone_Haikou.py", title="Bloom 6 • The Boundless Bloom (Haikou Concert)"),
        st.Page("pages/Milestone_Chongqing5th.py", title="Bloom 7 • The Golden Bloom (5th Anniversary in Chongqing)"),
    ],

    "Project Assets": [
        st.Page("pages/banner.py", title="Banner"),
        st.Page("pages/Poster.py", title="Poster"),
        st.Page("pages/Storyboard.py", title="Storyboard"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()
