import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ============================================================
# VAANI — SIH26172
# Low Latency and Efficient Voice Activator for Edge Devices
# Offline-First Hybrid Edge Voice Architecture
# ============================================================

st.set_page_config(
    page_title="VAANI | SIH26172",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# THEME
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(37,99,235,.14), transparent 30%),
            radial-gradient(circle at 85% 20%, rgba(34,211,238,.10), transparent 28%),
            #050b14;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Remove Streamlit decoration */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* HERO */
    .hero {
        min-height: 500px;
        display: flex;
        align-items: center;
        padding: 60px 5%;
        border: 1px solid rgba(34,211,238,.18);
        border-radius: 28px;
        background:
            linear-gradient(135deg,
                rgba(8,20,38,.96),
                rgba(5,12,23,.88));
        box-shadow:
            0 0 70px rgba(37,99,235,.08),
            inset 0 0 50px rgba(34,211,238,.025);
        position: relative;
        overflow: hidden;
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 500px;
        height: 500px;
        border-radius: 50%;
        background: rgba(34,211,238,.06);
        filter: blur(80px);
        right: -150px;
        top: -150px;
    }

    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
    }

    .eyebrow {
        color: #22d3ee;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .hero h1 {
        font-size: clamp(48px, 7vw, 92px);
        line-height: .95;
        margin: 0;
        font-weight: 800;
        letter-spacing: -4px;
    }

    .hero h1 span {
        color: #22d3ee;
    }

    .hero-subtitle {
        font-size: 21px;
        line-height: 1.6;
        color: #cbd5e1;
        max-width: 850px;
        margin-top: 28px;
    }

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 30px;
    }

    .badge {
        border: 1px solid rgba(34,211,238,.3);
        background: rgba(34,211,238,.06);
        padding: 9px 15px;
        border-radius: 999px;
        color: #cbd5e1;
        font-size: 13px;
    }

    /* SECTION */
    .section {
        margin-top: 75px;
    }

    .section-label {
        color: #22d3ee;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .section-title {
        font-size: 36px;
        font-weight: 800;
        margin: 0 0 12px 0;
        color: #f8fafc;
    }

    .section-description {
        color: #94a3b8;
        font-size: 16px;
        line-height: 1.7;
        max-width: 850px;
        margin-bottom: 28px;
    }

    /* CARDS */
    .card {
        height: 100%;
        padding: 26px;
        border-radius: 18px;
        border: 1px solid rgba(148,163,184,.13);
        background: rgba(15,23,42,.72);
        transition: all .25s ease;
    }

    .card:hover {
        transform: translateY(-4px);
        border-color: rgba(34,211,238,.35);
        box-shadow: 0 15px 40px rgba(0,0,0,.25);
    }

    .card h3 {
        margin-top: 0;
        color: #f8fafc;
        font-size: 20px;
    }

    .card p {
        color: #94a3b8;
        line-height: 1.7;
        font-size: 14px;
    }

    .icon {
        font-size: 28px;
        margin-bottom: 15px;
    }

    /* METRICS */
    .metric {
        text-align: center;
        padding: 28px 15px;
        border-radius: 18px;
        background: rgba(15,23,42,.8);
        border: 1px solid rgba(34,211,238,.14);
    }

    .metric-value {
        font-size: 34px;
        font-weight: 800;
        color: #22d3ee;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 13px;
        margin-top: 6px;
    }

    /* FLOW */
    .flow {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin: 30px 0;
    }

    .flow-node {
        padding: 15px 20px;
        border: 1px solid rgba(34,211,238,.3);
        border-radius: 12px;
        background: rgba(8,20,38,.9);
        color: #e2e8f0;
        font-weight: 600;
        font-size: 14px;
        text-align: center;
    }

    .flow-arrow {
        color: #22d3ee;
        font-size: 22px;
    }

    /* MODE */
    .mode-local {
        border: 1px solid rgba(34,197,94,.3);
        background: rgba(34,197,94,.05);
    }

    .mode-online {
        border: 1px solid rgba(59,130,246,.3);
        background: rgba(59,130,246,.05);
    }

    .status-dot {
        display: inline-block;
        width: 9px;
        height: 9px;
        background: #22c55e;
        border-radius: 50%;
        margin-right: 8px;
        box-shadow: 0 0 12px #22c55e;
    }

    /* FOOTER */
    .footer {
        margin-top: 90px;
        padding: 30px 0;
        border-top: 1px solid rgba(148,163,184,.12);
        color: #64748b;
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
        <div class="hero-content">
            <div class="eyebrow">
                SIH26172 · ISRO · EDGE AI
            </div>

            <h1>
                VA<span>A</span>NI
            </h1>

            <div class="hero-subtitle">
                Low Latency and Efficient Voice Activator for Edge Devices.
                An <b>offline-first hybrid voice architecture</b> where
                everyday processing stays local and cloud ASR is used only
                when required.
            </div>

            <div class="badge-row">
                <div class="badge">Offline First</div>
                <div class="badge">TinyML</div>
                <div class="badge">Custom Keyword</div>
                <div class="badge">ESP32 Edge</div>
                <div class="badge">Low Latency</div>
                <div class="badge">Open Source</div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# PROBLEM
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">01 · Problem</div>
        <div class="section-title">Why edge-first voice activation?</div>
        <div class="section-description">
            Continuously sending microphone audio to remote servers can
            increase bandwidth use, latency and privacy exposure.
            VAANI separates always-on local wake detection from
            optional remote speech recognition.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="icon">☁️</div>
            <h3>Cloud-First Systems</h3>
            <p>
                Continuous dependence on network connectivity can introduce
                communication overhead and additional latency.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🔒</div>
            <h3>Privacy Exposure</h3>
            <p>
                Always transmitting microphone data creates a larger
                privacy surface than keeping wake detection on the device.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="icon">⚡</div>
            <h3>Latency</h3>
            <p>
                Network round trips should not be necessary for every
                local voice interaction.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# VAANI SOLUTION
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">02 · Solution</div>
        <div class="section-title">Offline first. Cloud when needed.</div>
        <div class="section-description">
            VAANI continuously listens locally using a lightweight custom
            keyword spotting model. Only after a valid wake event does
            the system optionally hand audio to remote ASR.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

local_col, online_col = st.columns(2)

with local_col:
    st.markdown(
        """
        <div class="card mode-local">
            <h3>
                <span class="status-dot"></span>
                OFFLINE MODE — DEFAULT
            </h3>
            <p>
                <b>Microphone → ESP32 → Feature Extraction → TinyML KWS
                → Local Decision → Local Action</b>
            </p>
            <p>
                Internet is not required for the local wake-detection
                pipeline and supported local actions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with online_col:
    st.markdown(
        """
        <div class="card mode-online">
            <h3>☁️ ONLINE MODE — WHEN REQUIRED</h3>
            <p>
                <b>Wake Detection → Audio Buffer → Wi-Fi → Remote ASR
                → Response</b>
            </p>
            <p>
                The online path is activated only after the local
                wake decision.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# SYSTEM FLOW
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">03 · Architecture</div>
        <div class="section-title">Complete VAANI system flow</div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="flow">
        <div class="flow-node">🎙️ I2S MEMS Mic</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">ESP32</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">MFCC / Log-Mel</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">TinyML KWS</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Wake Decision</div>
    </div>

    <div class="flow">
        <div class="flow-node">NO → Continue Local Listening</div>
        <div class="flow-arrow">│</div>
        <div class="flow-node">YES → Buffer Audio</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Wi-Fi</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Remote ASR</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Response</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 3D DIGITAL TWIN
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">04 · Interactive Digital Twin</div>
        <div class="section-title">VAANI 3D hardware simulation</div>
        <div class="section-description">
            Interactive software representation of the physical edge
            architecture. The model will allow component selection,
            camera focus, system-state animation and offline/online
            demonstrations.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

digital_twin = Path(__file__).parent / "assets" / "digital_twin" / "index.html"

if digital_twin.exists():
    components.html(
        digital_twin.read_text(encoding="utf-8"),
        height=850,
        scrolling=False,
    )
else:
    st.info(
        """
        3D Digital Twin module is being added.

        Expected location:

        `assets/digital_twin/index.html`
        """
    )

# ============================================================
# REQUIREMENTS
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">05 · SIH Requirements</div>
        <div class="section-title">Engineering targets</div>
    </section>
    """,
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        """
        <div class="metric">
            <div class="metric-value">&lt; 256 KB</div>
            <div class="metric-label">Target Edge RAM</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        """
        <div class="metric">
            <div class="metric-value">&lt; 10%</div>
            <div class="metric-label">Target Idle CPU</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        """
        <div class="metric">
            <div class="metric-value">Custom</div>
            <div class="metric-label">Keyword Required</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m4:
    st.markdown(
        """
        <div class="metric">
            <div class="metric-value">INT8</div>
            <div class="metric-label">Edge Optimization</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# TINYML PIPELINE
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">06 · TinyML</div>
        <div class="section-title">From audio to edge inference</div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="flow">
        <div class="flow-node">Audio Dataset</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Noise / Augmentation</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">MFCC / Log-Mel</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Tiny CNN / DS-CNN</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">INT8 Quantization</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">ESP32</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# VALIDATION
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">07 · Validation</div>
        <div class="section-title">What we will measure</div>
        <div class="section-description">
            Final claims will be based on measurements from the physical
            low-power hardware rather than simulated numbers.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

v1, v2, v3 = st.columns(3)

with v1:
    st.markdown(
        """
        <div class="card">
            <h3>Resource Efficiency</h3>
            <p>
                RAM footprint, Flash footprint, CPU utilization and
                power behavior during continuous local listening.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with v2:
    st.markdown(
        """
        <div class="card">
            <h3>Detection Accuracy</h3>
            <p>
                True-positive rate, false activations per hour,
                different speakers, noise conditions and distances.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with v3:
    st.markdown(
        """
        <div class="card">
            <h3>Latency</h3>
            <p>
                Measure wake-word ending to server receipt and
                report mean, median and P95 end-to-end latency.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# BUSINESS MODEL
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">08 · Business Model</div>
        <div class="section-title">From prototype to deployment</div>
    </section>
    """,
    unsafe_allow_html=True,
)

b1, b2, b3, b4 = st.columns(4)

with b1:
    st.markdown(
        """
        <div class="card">
            <h3>Target Users</h3>
            <p>
                IoT developers, embedded-system teams, industrial
                automation, smart-device manufacturers and
                privacy-sensitive voice applications.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with b2:
    st.markdown(
        """
        <div class="card">
            <h3>Value</h3>
            <p>
                Lightweight edge wake detection, lower unnecessary
                audio transmission and an offline-first architecture.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with b3:
    st.markdown(
        """
        <div class="card">
            <h3>Revenue Paths</h3>
            <p>
                Hardware kits, B2B integration, deployment engineering,
                enterprise support and managed ASR infrastructure.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with b4:
    st.markdown(
        """
        <div class="card">
            <h3>Scale</h3>
            <p>
                Prototype → pilot → site deployment → multi-device
                fleet → multi-site edge infrastructure.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# ROADMAP
# ============================================================

st.markdown(
    """
    <section class="section">
        <div class="section-label">09 · Roadmap</div>
        <div class="section-title">Building VAANI step by step</div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="flow">
        <div class="flow-node">PS Analysis</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Dataset</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">KWS Model</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Quantization</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">ESP32</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Streaming</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Remote ASR</div>
        <div class="flow-arrow">→</div>
        <div class="flow-node">Benchmarking</div>
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
        VAANI · SIH26172 · Low Latency and Efficient Voice Activator
        for Edge Devices · ISRO
        <br><br>
        Offline-first edge intelligence. Cloud when needed.
    </div>
    """,
    unsafe_allow_html=True,
)
