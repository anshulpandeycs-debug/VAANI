import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="VAANI | SIH26172",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CSS — ONLY FOR VISUAL STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */
    .stApp {
        background: #07111F;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #F8FAFC !important;
    }

    /* Normal text */
    p, li {
        color: #A9B8C9;
    }

    /* Buttons */
    .stButton > button {
        border: 1px solid rgba(34, 211, 238, 0.30);
        background: #0B1C2D;
        color: #D9F9FF;
        border-radius: 10px;
    }

    .stButton > button:hover {
        border-color: #22D3EE;
        color: #22D3EE;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: #0A1727;
        border: 1px solid rgba(34, 211, 238, 0.16);
        border-radius: 16px;
        padding: 18px;
    }

    [data-testid="stMetricValue"] {
        color: #22D3EE;
    }

    [data-testid="stMetricLabel"] {
        color: #94A3B8;
    }

    /* Divider */
    hr {
        border-color: rgba(148, 163, 184, 0.12);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.caption("SIH26172  •  ISRO  •  EDGE AI")

st.title("VAANI")

st.subheader(
    "Low Latency and Efficient Voice Activator for Edge Devices"
)

st.write(
    """
    An **offline-first hybrid voice architecture** where everyday
    voice activation and local decisions remain on the edge, while
    remote ASR is used only when required.
    """
)

badge_columns = st.columns(6)

badges = [
    "Offline First",
    "TinyML",
    "Custom Keyword",
    "ESP32 Edge",
    "Low Latency",
    "Open Source",
]

for column, badge in zip(badge_columns, badges):
    with column:
        st.info(badge)


# ============================================================
# DIGITAL TWIN
# ============================================================

st.header("Interactive 3D Hardware Digital Twin")

st.write(
    """
    Software simulation of the physical VAANI edge architecture.
    Local listening remains active by default. Network streaming
    begins only after the custom wake keyword is detected.
    """
)


digital_twin = (
    Path(__file__).parent
    / "assets"
    / "digital_twin"
    / "index.html"
)


if digital_twin.exists():

    components.html(
        digital_twin.read_text(encoding="utf-8"),
        height=900,
        scrolling=False,
    )

else:

    st.error(
        "Digital Twin file not found: "
        "assets/digital_twin/index.html"
    )


# ============================================================
# SIH ENGINEERING TARGETS
# ============================================================

st.header("SIH Engineering Targets")

metric_columns = st.columns(4)

with metric_columns[0]:
    st.metric(
        label="Edge RAM Target",
        value="< 256 KB",
    )

with metric_columns[1]:
    st.metric(
        label="Idle CPU Target",
        value="< 10%",
    )

with metric_columns[2]:
    st.metric(
        label="Model Quantization",
        value="INT8",
    )

with metric_columns[3]:
    st.metric(
        label="Wake Keyword",
        value="Custom",
    )


# ============================================================
# EDGE ARCHITECTURE
# ============================================================

st.header("VAANI Edge Architecture")

st.write(
    """
    The architecture separates always-on local wake detection
    from optional post-wake remote speech processing.
    """
)

architecture = (
    "🎙️ I2S MEMS Microphone"
    "  →  Audio Capture"
    "  →  MFCC / Log-Mel"
    "  →  TinyML KWS"
    "  →  Wake Decision"
)

st.info(architecture)

architecture_columns = st.columns(2)

with architecture_columns[0]:

    st.subheader("NO — Stay Local")

    st.success(
        """
        Wake keyword not detected.

        Continue listening locally and keep the
        system in the low-resource edge state.
        """
    )


with architecture_columns[1]:

    st.subheader("YES — Start Streaming")

    st.warning(
        """
        Wake keyword detected.

        Start Wi-Fi streaming → Remote ASR →
        Response → Return to offline operation.
        """
    )


# ============================================================
# OPERATING MODES
# ============================================================

st.header("Two Operating Modes")

mode_columns = st.columns(2)

with mode_columns[0]:

    st.subheader("◉ Offline Mode")

    st.write(
        """
        Default operating state.

        Audio is processed locally for wake-word
        detection and local IoT actions.

        No continuous cloud audio streaming is required.
        """
    )


with mode_columns[1]:

    st.subheader("↗ Online Mode")

    st.write(
        """
        Activated only after wake detection when a
        command requires remote ASR.

        Post-wake audio is sent through Wi-Fi for
        remote processing.
        """
    )


# ============================================================
# PROJECT PIPELINE
# ============================================================

st.header("Six-Part Engineering Pipeline")

pipeline = [
    "1. Audio Capture + Edge Listening",
    "2. Custom Keyword Spotting AI",
    "3. Ultra-Low-Resource Edge Optimization",
    "4. Wake Detection + Audio Handoff",
    "5. Low-Latency Streaming + Remote ASR",
    "6. Testing + Benchmarking",
]

for item in pipeline:
    st.write("• " + item)


# ============================================================
# VALIDATION
# ============================================================

st.header("Validation")

validation_columns = st.columns(3)

with validation_columns[0]:

    st.subheader("Efficiency")

    st.write(
        """
        • RAM / Flash footprint

        • Idle CPU usage

        • Edge inference cost
        """
    )


with validation_columns[1]:

    st.subheader("Accuracy")

    st.write(
        """
        • True-positive rate

        • False activations/hour

        • Noise robustness
        """
    )


with validation_columns[2]:

    st.subheader("Latency")

    st.write(
        """
        • Wake detection time

        • Stream initiation

        • First packet arrival

        • P95 latency
        """
    )


# ============================================================
# PROJECT STATUS
# ============================================================

st.header("Project Status")

st.info(
    """
    **Current stage:** Interactive architecture and 3D digital-twin
    simulation.

    **Next engineering stages:** ESP32 firmware, custom keyword
    dataset/model, physical measurements, latency logging,
    and hardware validation.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "VAANI  •  SIH26172  •  ISRO  •  Edge AI  •  "
    "Low-Latency  •  Efficient  •  Offline-First"
)
