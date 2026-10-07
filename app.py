import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VAANI | SIH26172",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

site = Path("assets/website/index.html")

if site.exists():
    components.html(
        site.read_text(encoding="utf-8"),
        height=7200,
        scrolling=False,
    )
else:
    st.error(
        "VAANI animated website not found. "
        "Make sure assets/website/index.html exists."
    )
