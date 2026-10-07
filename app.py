import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VAANI — Agent Command Center",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Find VAANI website
# ---------------------------------------------------------

candidates = [
    Path("assets/website/index.html"),
    Path("assets/digital_twin/index.html"),
]

site = next((p for p in candidates if p.exists()), None)

# ---------------------------------------------------------
# Hide Streamlit chrome
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        html,
        body,
        [data-testid="stAppViewContainer"] {
            background: #05070b !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stSidebar"] {
            display: none !important;
        }

        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: none !important;
        }

        iframe {
            width: 100% !important;
            min-height: 1100px !important;
            border: 0 !important;
            display: block !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Load website
# ---------------------------------------------------------

if site:

    html = site.read_text(encoding="utf-8")

    components.html(
        html,
        height=1100,
        scrolling=True,
    )

else:

    st.error(
        """
        VAANI website not found.

        Expected one of:

        assets/website/index.html

        or

        assets/digital_twin/index.html
        """
    )
