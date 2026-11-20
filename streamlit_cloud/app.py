"""Streamlit Community Cloud portfolio adapter for game.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Minesweeper"
ICON = "💣"
DESC = "A classic Minesweeper board with flags, safe first click and win detection."
CATEGORY = "Python game / Web adaptation"
NOTICE = "The playable browser game below is served by Vercel and embedded in Streamlit; the original Tkinter app runs locally."
GITHUB = "https://github.com/mohsinattasial/game"
VERCEL = "https://mohsin-minesweeper.vercel.app"
LOCAL_COMMAND = "python main.py"
FEATURES = ["Python Tkinter original","Safe first move","Browser playable version"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Interactive browser edition")
st.caption("The following interactive view is embedded from the separate Vercel deployment.")
import streamlit.components.v1 as components
components.iframe(VERCEL, height=760, scrolling=True)

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
