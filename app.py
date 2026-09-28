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
# GLOBAL STYLE
# ============================================================

st.markdown(
    """
    <style>

    html, body, [data-testid="stAppViewContainer"] {
        background: #07111F !important;
        color: #F8FAFC !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* HERO */

    .hero {
        padding: 42px 46px;
        border: 1px solid rgba(34, 211, 238, 0.20);
        border-radius: 24px;

        background:
            radial-gradient(
                circle at 80% 20%,
                rgba(34, 211, 238, 0.08),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                rgba(9, 25, 43, 0.98),
                rgba(5, 15, 28, 0.98)
            );

        box-shadow:
            0 20px 80px rgba(0, 0, 0, 0.35);
    }

    .kicker {
        color: #22D3EE;
        font-weight: 800;
        letter-spacing: 4px;
        font-size: 14px;
        margin-bottom: 12px;
    }

    .hero-title {
        margin: 0;
        font-size: clamp(50px, 8vw, 92px);
        line-height: 0.95;
        font-weight: 900;
        letter-spacing: -4px;
        color: #F8FAFC;
    }

    .hero-title span {
        color: #22D3EE;
    }

    .hero-subtitle {
        max-width: 900px;
        margin-top: 22px;
        color: #A9B8C9;
        font-size: 18px;
        line-height: 1.7;
    }

    .hero-subtitle b {
        color: #E8FAFF;
    }

    /* BADGES */

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 25px;
    }

    .badge {
        border: 1px solid rgba(34, 211, 238, 0.22);
        background: rgba(34, 211, 238, 0.07);
        color: #D9F9FF;

        padding: 8px 14px;
        border-radius: 999px;

        font-size: 13px;
        font-weight: 600;
    }

    /* SECTION */

    .section-title {
        margin-top: 46px;
        margin-bottom: 8px;

        font-size: 30px;
        font-weight: 800;
        color: #F8FAFC;
    }

    .section-description {
        color: #94A3B8;
        margin-bottom: 18px;
        line-height: 1.6;
    }

    /* CARDS */

    .info-card {
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 18px;

        padding: 24px;

        background:
            linear-gradient(
                145deg,
                rgba(11, 28, 45, 0.98),
                rgba(7, 19, 32, 0.98)
            );

        min-height: 150px;
    }

    .info-card h3 {
        margin-top: 0;
        color: #E8FAFF;
    }

    .info-card p {
        color: #94A3B8;
        line-height: 1.6;
    }

    /* METRICS */

    .metric-card {
        border: 1px solid rgba(34, 211, 238, 0.16);
        border-radius: 18px;

        padding: 22px;

        background: #0A1727;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: #22D3EE;
    }

    .metric-label {
        margin-top: 4px;
        color: #94A3B8;
        font-size: 13px;
    }

    /* FLOW */

    .flow {
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 18px;

        padding: 25px;

        background: #0A1727;

        color: #D9F9FF;
        line-height: 2;
        text-align: center;
        font-weight: 600;
    }

    .flow span {
        color: #22D3EE;
        margin: 0 8px;
    }

    /* FOOTER */

    .footer {
        margin-top: 50px;
        padding: 25px 0;

        border-top: 1px solid rgba(148, 163, 184, 0.12);

        color: #64748B;
        text-align: center;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <section class="hero">

        <div class="kicker">
            SIH26172 · ISRO · EDGE AI
        </div>

        <h1 class="hero-title">
            VA<span>A</span>NI
        </h1>

        <div class="hero-subtitle">
            Low Latency and Efficient Voice Activator for Edge Devices.
            An <b>offline-first hybrid voice architecture</b> where
            everyday voice activation and local decisions remain on the
            edge, while remote ASR is used only when required.
        </div>

        <div class="badge-row">

            <div class="badge">
                Offline First
            </div>

            <div class="badge">
                TinyML
            </div>

            <div class="badge">
                Custom Keyword
            </div>

            <div class="badge">
                ESP32 Edge
            </div>

            <div class="badge">
                Low Latency
            </div>

            <div class="badge">
                Open Source
            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DIGITAL TWIN
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Interactive 3D Hardware Digital Twin
    </div>

    <div class="section-description">
        Software simulation of the physical VAANI edge architecture.
        Local listening remains active by default. Network streaming
        begins only after the custom wake keyword is detected.
    </div>
    """,
    unsafe_allow_html=True,
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
        "Digital Twin not found. "
        "Expected file: assets/digital_twin/index.html"
    )


# ============================================================
# SYSTEM ARCHITECTURE
# ============================================================

st.markdown(
    """
    <div class="section-title">
        VAANI Edge Architecture
    </div>

    <div class="section-description">
        The architecture separates always-on local wake detection
        from optional post-wake remote speech processing.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="flow">

        I2S MEMS Microphone

        <span>→</span>

        Audio Capture

        <span>→</span>

        MFCC / Log-Mel

        <span>→</span>

        TinyML KWS

        <span>→</span>

        Wake Decision

        <br>

        NO

        <span>→</span>

        Continue Local Listening

        &nbsp;&nbsp;&nbsp;

        YES

        <span>→</span>

        Wi-Fi

        <span>→</span>

        Remote ASR

        <span>→</span>

        Response

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIH ENGINEERING TARGETS
# ============================================================

st.markdown(
    """
    <div class="section-title">
        SIH Engineering Targets
    </div>
    """,
    unsafe_allow_html=True,
)


metric_cols = st.columns(4)


metrics = [
    ("< 256 KB", "Edge RAM target"),
    ("< 10%", "Idle CPU target"),
    ("INT8", "Quantized TinyML"),
    ("Custom", "Wake keyword"),
]


for col, (value, label) in zip(metric_cols, metrics):

    with col:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-value">
                    {value}
                </div>

                <div class="metric-label">
                    {label}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# TWO OPERATING MODES
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Two Operating Modes
    </div>
    """,
    unsafe_allow_html=True,
)


mode_cols = st.columns(2)


with mode_cols[0]:

    st.markdown(
        """
        <div class="info-card">

            <h3>◉ Offline Mode</h3>

            <p>
                Default operating state. Audio is processed locally
                for wake-word detection and local IoT actions.
                No continuous cloud audio streaming is required.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


with mode_cols[1]:

    st.markdown(
        """
        <div class="info-card">

            <h3>↗ Online Mode</h3>

            <p>
                Activated only after wake detection when a command
                requires remote ASR. The post-wake audio stream is
                sent through Wi-Fi for remote processing.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# PROJECT STATUS
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Project Status
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="info-card">

        <h3>Current Development</h3>

        <p>
            Interactive architecture and 3D digital-twin simulation
            are being developed as the public demonstration layer.
            The next engineering stages are the ESP32 firmware,
            custom keyword dataset/model, physical measurements,
            latency logging, and hardware validation.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        VAANI · SIH26172 · ISRO · Edge AI

        <br>

        Low-Latency · Efficient · Offline-First · Open Source

    </div>
    """,
    unsafe_allow_html=True,
)
