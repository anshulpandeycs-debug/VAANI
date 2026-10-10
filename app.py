
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# VAANI — LOW-LATENCY EDGE KEYWORD SPOTTING
# Streamlit application entry point
# ============================================================

st.set_page_config(
    page_title="VAANI | Edge KWS",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ------------------------------------------------------------
# Resolve paths relative to this file.
# This works even when Streamlit uses a different working folder.
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

HTML_FILE = (
    BASE_DIR
    / "assets"
    / "website"
    / "index.html"
)


# ------------------------------------------------------------
# Streamlit page styling
# ------------------------------------------------------------

st.markdown(
    """
    <style>
        /* Hide standard Streamlit navigation and footer */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        /* Remove default content spacing */
        [data-testid="stAppViewContainer"] > .main {
            padding-top: 0 !important;
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Make the embedded website fill the available width */
        iframe {
            display: block;
            width: 100%;
            border: none !important;
        }

        /* Avoid horizontal overflow */
        html,
        body,
        [data-testid="stAppViewContainer"] {
            overflow-x: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# Verify the website file exists before loading it
# ------------------------------------------------------------

if not HTML_FILE.is_file():
    st.error("VAANI website file could not be found.")

    st.markdown(
        """
        The application expects the following file structure:

        ```text
        VAANI/
        ├── app.py
        ├── requirements.txt
        └── assets/
            └── website/
                └── index.html
        ```
        """
    )

    st.code(
        f"Expected HTML file:\n{HTML_FILE}",
        language="text",
    )

    st.info(
        "Create the assets/website folder and upload "
        "the complete index.html file before redeploying."
    )

    st.stop()


# ------------------------------------------------------------
# Read the complete website
# ------------------------------------------------------------

try:
    html_content = HTML_FILE.read_text(encoding="utf-8")

except OSError as error:
    st.error("VAANI could not read the website file.")

    st.code(str(error), language="text")

    st.stop()


# ------------------------------------------------------------
# Render the website
# ------------------------------------------------------------

components.html(
    html_content,
    height=16000,
    scrolling=True,
)


# ============================================================
# IMPORTANT
#
# This file renders the front-end website.
# It does not independently connect to:
# - ESP32 / ESP32-S3 hardware
# - A trained KWS model
# - Live RAM or CPU telemetry
# - A remote ASR server
#
# Those integrations require their own backend and firmware.
# ============================================================
