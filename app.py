
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


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

# Your actual website location is the first option.
CANDIDATE_HTML_FILES = [
    BASE_DIR / "assets" / "digital_twin" / "index.html",
    BASE_DIR / "assets" / "website" / "index.html",
    BASE_DIR / "website" / "index.html",
    BASE_DIR / "index.html",
    BASE_DIR / "assets" / "index.html",
]


def find_website_file():
    """Find index.html in the expected project locations."""

    for candidate in CANDIDATE_HTML_FILES:
        if candidate.is_file():
            return candidate

    # Fallback: search the project directory recursively.
    # Avoid virtual environments and Git internals.
    excluded_dirs = {".git", ".venv", "venv", "__pycache__"}

    try:
        for candidate in BASE_DIR.rglob("index.html"):
            if any(part in excluded_dirs for part in candidate.parts):
                continue

            if candidate.is_file():
                return candidate

    except OSError:
        pass

    return None


HTML_FILE = find_website_file()


# ============================================================
# STREAMLIT STYLING
# ============================================================

st.markdown(
    """
    <style>
        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }

        [data-testid="stAppViewContainer"] > .main {
            padding-top: 0 !important;
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        iframe {
            display: block;
            width: 100%;
            border: none !important;
        }

        html,
        body,
        [data-testid="stAppViewContainer"] {
            overflow-x: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CHECK WHETHER THE WEBSITE EXISTS
# ============================================================

if HTML_FILE is None:
    st.error("VAANI website file could not be found.")

    st.markdown(
        """
        The Streamlit application is running, but it cannot
        find the website HTML file.

        Make sure `index.html` is committed to your GitHub
        repository at the following location:
        """
    )

    st.code(
        "your-repository/\n"
        "├── app.py\n"
        "├── requirements.txt\n"
        "└── assets/\n"
        "    └── digital_twin/\n"
        "        └── index.html",
        language="text",
    )

    st.markdown("**Expected file path:**")

    st.code(
        str(BASE_DIR / "assets" / "digital_twin" / "index.html"),
        language="text",
    )

    st.markdown("**HTML files found in the project:**")

    try:
        found_html_files = [
            str(path.relative_to(BASE_DIR))
            for path in BASE_DIR.rglob("*.html")
            if not any(
                part in {".git", ".venv", "venv", "__pycache__"}
                for part in path.parts
            )
        ]
    except OSError:
        found_html_files = []

    if found_html_files:
        st.code(
            "\n".join(found_html_files),
            language="text",
        )
    else:
        st.warning(
            "No HTML files were found. Upload index.html "
            "to GitHub and commit the file."
        )

    st.info(
        "After adding the missing file, restart or reboot "
        "your Streamlit app."
    )

    st.stop()


# ============================================================
# LOAD THE WEBSITE HTML
# ============================================================

try:
    html_content = HTML_FILE.read_text(encoding="utf-8")

except (OSError, UnicodeError) as error:
    st.error("VAANI could not read the website file.")

    st.code(
        f"File: {HTML_FILE}\nError: {error}",
        language="text",
    )

    st.stop()


# ============================================================
# RENDER THE WEBSITE
# ============================================================

components.html(
    html_content,
    height=16000,
    scrolling=True,
)


# ============================================================
# INTEGRATION STATUS
# ============================================================
#
# This application loads and displays the website.
#
# It does not automatically connect to:
# - ESP32 / ESP32-S3 hardware
# - A trained keyword spotting model
# - Live RAM or CPU telemetry
# - A remote ASR server
#
# These features require separate backend, model,
# network, and firmware integrations.
#
# ============================================================

