import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from textwrap import dedent
import pandas as pd


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
# GLOBAL CSS
# ============================================================

st.markdown(dedent("""
<style>

:root {
    --bg: #050B14;
    --panel: #0B1624;
    --panel2: #0F1D2D;
    --blue: #2563EB;
    --cyan: #22D3EE;
    --green: #22C55E;
    --orange: #F59E0B;
    --red: #EF4444;
    --white: #F8FAFC;
    --muted: #94A3B8;
    --line: rgba(148,163,184,.16);
}

.stApp {
    background:
        radial-gradient(circle at 8% 5%, rgba(37,99,235,.16), transparent 25%),
        radial-gradient(circle at 92% 8%, rgba(34,211,238,.10), transparent 24%),
        linear-gradient(180deg,#050B14 0%,#07111F 50%,#050B14 100%);
    color: var(--white);
}

.block-container {
    max-width: 1320px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

html, body, [class*="css"] {
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}

/* ---------- ANIMATED BACKGROUND ---------- */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background:
        radial-gradient(circle at 50% 35%, rgba(34,211,238,.045), transparent 30%),
        radial-gradient(circle at 20% 75%, rgba(37,99,235,.045), transparent 28%),
        radial-gradient(circle at 82% 62%, rgba(34,211,238,.035), transparent 25%);
    animation: vaaniAmbientPulse 9s ease-in-out infinite alternate;
}

.stApp::after {
    content: "";
    position: fixed;
    inset: -15%;
    z-index: 0;
    pointer-events: none;
    opacity: .5;
    background-image:
        radial-gradient(circle, rgba(255,255,255,.85) 0 1px, transparent 1.5px),
        radial-gradient(circle, rgba(34,211,238,.65) 0 1px, transparent 1.5px),
        radial-gradient(circle, rgba(255,255,255,.45) 0 1.5px, transparent 2px);
    background-size: 115px 115px, 173px 173px, 257px 257px;
    background-position: 8px 20px, 70px 40px, 130px 10px;
    animation: vaaniStarDrift 22s linear infinite;
}

@keyframes vaaniAmbientPulse {
    from { opacity: .65; transform: scale(1); }
    to { opacity: 1; transform: scale(1.025); }
}

@keyframes vaaniStarDrift {
    from { transform: translate3d(0,-3%,0); }
    to { transform: translate3d(3%,12%,0); }
}

/* Extra falling-star streaks */
section.main > div:first-child::before,
section.main > div:first-child::after {
    content: "";
    position: fixed;
    top: -12%;
    left: 12%;
    width: 2px;
    height: 80px;
    z-index: 0;
    pointer-events: none;
    opacity: 0;
    transform: rotate(32deg);
    background: linear-gradient(
        to bottom,
        transparent,
        rgba(103,232,249,.75),
        transparent
    );
    box-shadow:
        280px 120px 0 rgba(103,232,249,.0),
        520px 260px 0 rgba(103,232,249,.0),
        760px 80px 0 rgba(103,232,249,.0);
    animation: vaaniMeteor 8s linear infinite;
}

section.main > div:first-child::after {
    left: 58%;
    animation-delay: -4.5s;
    animation-duration: 11s;
}

@keyframes vaaniMeteor {
    0%, 62% {
        opacity: 0;
        transform: translate3d(0,-18vh,0) rotate(32deg);
    }
    68% { opacity: .8; }
    82% {
        opacity: 0;
        transform: translate3d(32vw,105vh,0) rotate(32deg);
    }
    100% { opacity: 0; }
}

/* Subtle dinosaur silhouettes looking toward the star field */
.stApp .block-container::before {
    content: "🦖";
    position: fixed;
    left: 2.5%;
    bottom: 14px;
    z-index: 1;
    pointer-events: none;
    font-size: clamp(34px, 4.5vw, 68px);
    opacity: .055;
    filter: grayscale(1) brightness(1.9) drop-shadow(0 0 14px rgba(34,211,238,.25));
    transform: scaleX(-1);
    animation: vaaniDinoLook 5s ease-in-out infinite;
}

.stApp .block-container::after {
    content: "🦕";
    position: fixed;
    right: 3%;
    bottom: 18px;
    z-index: 1;
    pointer-events: none;
    font-size: clamp(30px, 4vw, 60px);
    opacity: .045;
    filter: grayscale(1) brightness(1.9) drop-shadow(0 0 14px rgba(34,211,238,.2));
    animation: vaaniDinoLook 6s ease-in-out infinite reverse;
}

@keyframes vaaniDinoLook {
    0%,100% { transform: translateY(0) scaleX(-1); }
    50% { transform: translateY(-6px) scaleX(-1.03); }
}

@media (prefers-reduced-motion: reduce) {
    .stApp::before,
    .stApp::after,
    section.main > div:first-child::before,
    section.main > div:first-child::after,
    .stApp .block-container::before,
    .stApp .block-container::after {
        animation: none !important;
    }
}

</style>
"""), unsafe_allow_html=True)



# ============================================================
# DATA / EVIDENCE
# ============================================================

FX = 95.98

VOICE_2025_USD_M = 366.3
VOICE_2030_USD_M = 954.3

VOICE_2025_CR = VOICE_2025_USD_M * FX / 10
VOICE_2030_CR = VOICE_2030_USD_M * FX / 10

SAM_CR = VOICE_2025_CR * 0.25
SOM_CR = SAM_CR * 0.03

IOT_2025_USD_M = 50140
IOT_2030_USD_M = 95800

IOT_2025_CR = IOT_2025_USD_M * FX / 10
IOT_2030_CR = IOT_2030_USD_M * FX / 10

STT_USD_MIN = 0.016
STT_INR_MIN = STT_USD_MIN * FX


SOURCES = {
    "S1": "https://sih2026.vuce.in/ps/SIH26172",
    "S2": "https://www.marketsandmarkets.com/Market-Reports/geography/speech-voice-recognition-market/india",
    "S3": "https://www.marketsandmarkets.com/Market-Reports/geography/internet-of-things-market/India",
    "S4": "https://cloud.google.com/speech-to-text/pricing",
    "S5": "https://www.petsymposium.org/popets/2020/popets-2020-0072.php",
    "S6": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2226569&lang=1&reg=1",
    "S7": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2083808&lang=1&reg=3",
    "S8": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2291171&lang=1&reg=1",
    "S9": "https://documentation.espressif.com/esp32_s3_datasheet_en.pdf",
    "S10": "https://www.espressif.com/en/node/4993",
    "S11": "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/high-accuracy-keyword-spotting-on-cortex-m-processors",
    "S12": "https://research.google/blog/launching-the-speech-commands-dataset/",
    "S13": "https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa",
    "S14": "https://www.wavtron.in/products/esp32-s3-devkitc-n16r8-dev-board",
    "S15": "https://findmychips.com/part/inmp441-mems-high-precision-omnidirectional-microphone-module-i2s-bb3069",
    "S16": "https://store.electrobot.co.in/product/inmp441",
}


def source_link(label, key):
    st.markdown(
        dedent(f"""
        <div class="source">
            <b>{label}</b>
            ·
            <a href="{SOURCES[key]}" target="_blank">
                {key} source ↗
            </a>
        </div>
        """),
        unsafe_allow_html=True,
    )


def section(number, title, description=""):
    st.markdown(
        dedent(f"""
        <div class="section-kicker">SECTION {number}</div>
        <div class="section-title">{title}</div>
        <div class="section-description">{description}</div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    dedent("""
    <div class="hero">

        <div class="kicker">
            SMART INDIA HACKATHON 2026 · SIH26172 · ISRO · HARDWARE
        </div>

        <h1>VAANI</h1>

        <div class="hero-subtitle">
            Local Wake. Remote Intelligence.
        </div>

        <div class="hero-text">
            VAANI is an edge-first voice activation architecture designed
            for low-power devices. It continuously detects a custom keyword
            locally using a compact TinyML model and activates remote speech
            recognition only after a valid wake event.
        </div>

        <br>

        <span class="badge">CUSTOM KWS</span>
        <span class="badge">TINYML</span>
        <span class="badge">EDGE AI</span>
        <span class="badge">OFFLINE-FIRST</span>
        <span class="badge">POST-WAKE STREAMING</span>
        <span class="badge">ESP32-S3</span>
        <span class="badge">OPEN-SOURCE</span>

    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# TOP METRICS
# ============================================================

st.write("")

c1, c2, c3, c4 = st.columns(4)

top_metrics = [
    ("<256 KB", "SIH edge RAM boundary", "SIH TARGET"),
    ("<10%", "Idle continuous-listening CPU", "SIH TARGET"),
    (f"₹{VOICE_2025_CR:,.0f} Cr", "India voice/speech market · 2025", "EXTERNAL"),
    ("101.78 Cr", "India internet subscribers · Sep 2025", "EXTERNAL"),
]

for col, (number, label, typ) in zip(
    [c1, c2, c3, c4],
    top_metrics
):
    with col:
        st.markdown(
            dedent(f"""
            <div class="metric-card">
                <div class="metric-number">{number}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-type">{typ}</div>
            </div>
            """),
            unsafe_allow_html=True,
        )


# ============================================================
# 1 — PROBLEM STATEMENT
# ============================================================

section(
    "01",
    "The Problem — SIH26172",
    "Why a lightweight local wake-up layer is required before cloud speech processing."
)

st.markdown(
    dedent("""
    <div class="info-box">
    <b>Problem in one sentence:</b>
    Voice-controlled IoT devices need continuous listening, but sending
    audio continuously to remote speech processing can increase network
    dependency, latency, processing cost and privacy exposure.
    </div>
    """),
    unsafe_allow_html=True,
)

st.write(
    """
    SIH26172 asks for an ultra-lightweight and highly accurate custom
    keyword-spotting system running locally on a low-power device.
    After the custom keyword is detected, subsequent audio should be
    efficiently streamed to remote ASR with minimal data overhead and latency.
    """
)

source_link("Official SIH26172 problem statement", "S1")


p1, p2, p3 = st.columns(3)

with p1:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">01 · Continuous Listening</div>
        <div class="card-text">
        The edge device must inspect incoming audio continuously without
        requiring a full cloud speech-recognition stack to run all the time.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">02 · False Activation</div>
        <div class="card-text">
        Incorrect wake events can unnecessarily trigger recording,
        network transmission and speech-recognition processing.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with p3:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">03 · Low Latency</div>
        <div class="card-text">
        The system must minimize the time between the keyword ending,
        local detection and the first audio packet reaching remote ASR.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# 2 — VAANI SOLUTION
# ============================================================

section(
    "02",
    "VAANI Solution",
    "The key design decision is to separate always-on activation from heavy speech intelligence."
)

st.markdown(
    dedent("""
    <div class="green-box">
    <b>Core architecture:</b>
    Keep the wake decision local. Keep ordinary ambient audio local.
    Open the network speech path only after a valid custom wake event.
    </div>
    """),
    unsafe_allow_html=True,
)

solution = """
digraph G {
    rankdir=LR;
    bgcolor="transparent";

    node [
        shape=box,
        style="rounded,filled",
        fillcolor="#0B1624",
        color="#22D3EE",
        fontcolor="white",
        fontname="Arial",
        penwidth=1.5
    ];

    mic [label="I2S MEMS\\nMicrophone"];
    audio [label="Audio Capture\\nPCM Buffer"];
    dsp [label="DSP\\nMFCC / Log-Mel"];
    kws [label="TinyML\\nCustom KWS"];
    decision [label="Confidence +\\nTemporal Decision"];

    no [label="NO\\nKeep Listening Locally", color="#22C55E"];
    yes [label="YES\\nWake Event", color="#F59E0B"];

    preroll [label="Ring Buffer\\nPre-roll"];
    stream [label="Post-wake\\nAudio Stream"];
    asr [label="Remote\\nASR"];
    app [label="Transcript /\\nApplication"];

    mic -> audio -> dsp -> kws -> decision;

    decision -> no [label="NO"];
    decision -> yes [label="YES"];

    yes -> preroll -> stream -> asr -> app;
}
"""

st.graphviz_chart(solution, use_container_width=True)

a, b = st.columns(2)

with a:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">
        <span class="status-local">LOCAL PATH</span>
        </div>
        <div class="card-text">
        Microphone → DSP → TinyML KWS → confidence decision.
        <br><br>
        This path operates continuously on the edge device.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with b:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">
        <span class="status-network">NETWORK PATH</span>
        </div>
        <div class="card-text">
        Wake → pre-roll → audio streaming → remote ASR → application.
        <br><br>
        This path is activated only after a valid wake event.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# 3 — WHY THE PROBLEM IS REAL
# ============================================================

section(
    "03",
    "Why the Problem Is Real",
    "External Indian market and technical evidence supporting the opportunity."
)

e1, e2, e3, e4 = st.columns(4)

with e1:
    st.metric(
        "India Voice/Speech",
        f"₹{VOICE_2025_CR:,.0f} Cr",
        "2025 external estimate",
    )

with e2:
    st.metric(
        "India IoT",
        f"₹{IOT_2025_CR/100000:,.2f} Lakh Cr",
        "2025 external estimate",
    )

with e3:
    st.metric(
        "Rural Internet",
        "42.77 Cr",
        "Sep 2025",
    )

with e4:
    st.metric(
        "Village Connectivity",
        "98.09%",
        "Dec 2025",
    )

st.caption(
    "These are external statistics and market estimates. "
    "They are not measurements produced by VAANI."
)

evidence = pd.DataFrame({
    "Evidence": [
        "India speech & voice recognition",
        "India IoT market",
        "Internet subscribers",
        "Rural internet subscribers",
        "Villages with mobile connectivity",
        "Smart Cities Mission",
        "Electronics production",
        "External smart-speaker study",
    ],
    "Numeric fact": [
        "US$366.3M in 2025 → US$954.3M in 2030; 21.1% CAGR",
        "US$50.14B in 2025 → US$95.8B in 2030; 13.8% CAGR",
        "101.78 crore at 30 Sep 2025",
        "42.77 crore at 30 Sep 2025",
        "98.09% reported mobile connectivity at 31 Dec 2025",
        "8,066 projects / ₹1,64,669 Cr orders; 7,352 completed by Nov 2024",
        "Over ₹13 lakh crore production; approximately 25 lakh jobs",
        "0.95 misactivations/hour in an external US/UK study",
    ],
    "Use in VAANI": [
        "Market opportunity",
        "IoT deployment ecosystem",
        "Connected-device opportunity",
        "Rural deployment relevance",
        "Connectivity context",
        "Public-sector deployment context",
        "Indian hardware ecosystem",
        "False-activation problem context",
    ],
})

st.dataframe(
    evidence,
    use_container_width=True,
    hide_index=True,
)


source_link("India voice market", "S2")
source_link("India IoT market", "S3")
source_link("India connectivity", "S6")
source_link("Smart Cities Mission", "S7")
source_link("Indian electronics ecosystem", "S8")
source_link("External wake-word research", "S5")


# ============================================================
# 4 — COST AND NETWORK
# ============================================================

section(
    "04",
    "Cost + Network Logic",
    "Why edge gating can reduce unnecessary remote speech-processing usage."
)

st.write(
    f"""
    A public reference price for Google Cloud Speech-to-Text V2 Standard
    is US$0.016/min for the stated pricing tier. Using the dated reference
    exchange rate of ₹{FX:.2f}/US$, this corresponds to approximately
    ₹{STT_INR_MIN:.2f}/minute.
    """
)

source_link("Google Cloud Speech-to-Text pricing", "S4")

mins = [5, 15, 30, 60]

cost_df = pd.DataFrame({
    "Daily remote ASR minutes": mins,
    "Monthly minutes": [x * 30 for x in mins],
    "Reference monthly ASR cost (₹)": [
        x * 30 * STT_INR_MIN for x in mins
    ],
})

st.bar_chart(
    cost_df.set_index("Daily remote ASR minutes")[
        "Reference monthly ASR cost (₹)"
    ]
)

st.dataframe(
    cost_df,
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    dedent("""
    <div class="info-box">
    <b>Important:</b> this is a cost scenario, not a claim that VAANI
    has already achieved a specific percentage reduction.
    Actual savings must be measured using network traffic and ASR-session logs.
    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# 5 — UNIQUENESS
# ============================================================

section(
    "05",
    "What Makes VAANI Different",
    "The differentiation is architectural: local activation + selective remote intelligence."
)

comparison = pd.DataFrame({
    "Dimension": [
        "Always-on decision",
        "Network dependency",
        "Keyword",
        "Idle resource strategy",
        "Audio transmission",
        "Measurement focus",
    ],
    "Cloud-first voice architecture": [
        "Remote processing may be involved",
        "Network may affect activation",
        "Often ecosystem-defined",
        "General speech stack can be heavier",
        "May involve broader remote audio flow",
        "Primarily application / UX oriented",
    ],
    "VAANI": [
        "Local custom KWS",
        "Wake decision remains local",
        "Deployment-specific custom keyword",
        "Compact DSP + INT8 KWS",
        "Post-wake streaming",
        "RAM + CPU + TPR + false activations + T0→T3",
    ],
})

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True,
)

u1, u2, u3 = st.columns(3)

with u1:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">Edge-first</div>
        <div class="card-text">
        The device decides locally whether the user actually activated it.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with u2:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">Custom keyword</div>
        <div class="card-text">
        VAANI is designed around a custom project-specific activation phrase,
        not a pre-trained commercial wake word.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with u3:
    st.markdown(
        dedent("""
        <div class="card">
        <div class="card-title">Measurable</div>
        <div class="card-text">
        Performance is evaluated using embedded-system metrics rather than
        only desktop model accuracy.
        </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

st.write(
    """
    Compact keyword spotting on microcontrollers is an established research
    direction. External embedded benchmarks demonstrate that small KWS
    models can be designed for constrained processors. These references
    establish feasibility of the technology class; they are not VAANI results.
    """
)

source_link("Arm Cortex-M keyword-spotting reference", "S11")


# ============================================================
# 6 — HARDWARE
# ============================================================

section(
    "06",
    "Physical Hardware Architecture",
    "The intended prototype uses a low-power MCU, I2S microphone and wireless post-wake path."
)

hardware = pd.DataFrame({
    "Component": [
        "ESP32-S3",
        "I2S MEMS microphone",
        "TinyML runtime",
        "Wi-Fi",
        "Remote ASR backend",
    ],
    "Role": [
        "Edge MCU + local inference + connectivity",
        "Digital audio capture",
        "Local KWS inference",
        "Post-wake transport",
        "Speech recognition after activation",
    ],
    "Why it matters": [
        "MCU-class deployment",
        "Digital low-noise audio interface",
        "Low-resource inference",
        "Fast handoff after wake",
        "Heavy processing stays off the MCU",
    ],
})

st.dataframe(
    hardware,
    use_container_width=True,
    hide_index=True,
)

source_link("ESP32-S3 datasheet", "S9")
source_link("ESP32-S3 documentation", "S10")

st.caption(
    "Prototype component prices vary by supplier and quantity. "
    "Example Indian listings are references only and should not be treated as manufacturing BOM prices."
)

source_link("ESP32-S3 Indian price reference", "S14")
source_link("INMP441 reference", "S15")


# ============================================================
# 7 — DIGITAL TWIN
# ============================================================

section(
    "07",
    "Interactive 3D Digital Twin",
    "A visual representation of the intended physical VAANI architecture."
)

st.markdown(
    dedent("""
    <div class="green-box">
    <b>Offline-first behavior:</b>
    The microphone and KWS operate locally.
    The network path appears only after a valid wake event.
    </div>
    """),
    unsafe_allow_html=True,
)

st.write(
    """
    The digital twin represents the physical architecture using a 3D
    hardware-style scene. Components can be inspected to understand their
    role in the VAANI pipeline.
    """
)

twin_path = Path("assets/digital_twin/index.html")

if twin_path.exists():

    components.html(
        twin_path.read_text(encoding="utf-8"),
        height=820,
        scrolling=False,
    )

else:

    st.warning(
        "3D digital twin not found. "
        "Make sure assets/digital_twin/index.html exists in the repository."
    )


# ============================================================
# 8 — SIH VALIDATION
# ============================================================

section(
    "08",
    "SIH Validation Dashboard",
    "Every important claim should eventually map to a reproducible hardware measurement."
)

st.markdown(
    dedent("""
    <div class="warning-box">
    <b>Evidence rule:</b>
    External benchmarks are not VAANI measurements.
    The final prototype must replace target values with actual hardware logs.
    </div>
    """),
    unsafe_allow_html=True,
)

metrics = pd.DataFrame({
    "Metric": [
        "RAM",
        "Idle CPU",
        "True-positive rate",
        "False activations/hour",
        "Miss rate",
        "Inference latency",
        "Wake → ASR latency",
        "Power",
    ],
    "SIH / engineering target": [
        "<256 KB",
        "<10%",
        "High",
        "Near zero",
        "Low",
        "Low",
        "T3 − T0",
        "Low",
    ],
    "How VAANI should measure it": [
        "Peak runtime + model arena + buffers",
        "Continuous idle listening",
        "Correct detections / wake trials",
        "False wakes / hour",
        "Missed wakes / wake trials",
        "DSP + model execution timing",
        "Mean / median / P95",
        "Current / energy during idle and active",
    ],
    "Final evidence": [
        "MCU log",
        "CPU profiling log",
        "Test dataset",
        "Long-duration test",
        "Wake test",
        "Inference profiler",
        "T0-T3 timestamp log",
        "Power measurement",
    ],
})

st.dataframe(
    metrics,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# 9 — LATENCY
# ============================================================

section(
    "09",
    "Wake-to-ASR Latency",
    "A reproducible timing chain for the SIH latency requirement."
)

latency = """
digraph G {

    rankdir=LR;
    bgcolor="transparent";

    node [
        shape=box,
        style="rounded,filled",
        fillcolor="#0B1624",
        fontcolor="white",
        color="#60A5FA",
        fontname="Arial",
        penwidth=1.5
    ];

    t0 [label="T0\\nKeyword ends"];
    t1 [label="T1\\nLocal detection"];
    t2 [label="T2\\nStream starts"];
    t3 [label="T3\\nFirst server packet"];

    t0 -> t1 -> t2 -> t3;
}
"""

st.graphviz_chart(
    latency,
    use_container_width=True,
)

st.markdown(
    dedent("""
    <div class="info-box">
    <b>Primary latency metric:</b> T3 − T0
    <br><br>
    Also report:
    <br>
    • T1 − T0 = local detection time
    <br>
    • T2 − T1 = stream-start overhead
    <br>
    • T3 − T2 = network handoff time
    <br>
    • Mean, median and P95
    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# 10 — MARKET
# ============================================================

section(
    "10",
    "India Market Opportunity — TAM / SAM / SOM",
    "A transparent market-sizing model based on an external India speech and voice market estimate."
)

st.write(
    f"""
    The primary TAM is the reported India speech and voice recognition
    market. The external 2025 estimate is US$366.3M.
    At ₹{FX:.2f}/US$, the converted value is approximately
    ₹{VOICE_2025_CR:,.0f} crore.
    """
)

market_df = pd.DataFrame({
    "Market layer": ["TAM", "SAM", "SOM"],
    "Value (₹ crore)": [
        VOICE_2025_CR,
        SAM_CR,
        SOM_CR,
    ],
})

st.bar_chart(
    market_df.set_index("Market layer")["Value (₹ crore)"]
)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(
        dedent(f"""
        <div class="metric-card">
        <div class="metric-number">₹{VOICE_2025_CR:,.0f} Cr</div>
        <div class="metric-label">TAM — India voice/speech market</div>
        <div class="metric-type">EXTERNAL MARKET ESTIMATE</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        dedent(f"""
        <div class="metric-card">
        <div class="metric-number">₹{SAM_CR:,.0f} Cr</div>
        <div class="metric-label">SAM — modeled 25% edge/IoT subset</div>
        <div class="metric-type">MODELED ASSUMPTION</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        dedent(f"""
        <div class="metric-card">
        <div class="metric-number">₹{SOM_CR:,.1f} Cr</div>
        <div class="metric-label">SOM — modeled 3% SAM scenario</div>
        <div class="metric-type">PLANNING SCENARIO</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

st.markdown(
    dedent("""
    <div class="info-box">

    <b>TAM calculation</b>
    <br>
    US$366.3M × ₹95.98/US$ ≈ ₹3,516 Cr

    <br><br>

    <b>SAM calculation</b>
    <br>
    TAM × 25% ≈ ₹879 Cr

    <br><br>

    <b>SOM calculation</b>
    <br>
    SAM × 3% ≈ ₹26.4 Cr/year

    <br><br>

    SAM and SOM are explicitly modeled assumptions for planning.
    They are not published market figures and are not forecasts.

    </div>
    """),
    unsafe_allow_html=True,
)

source_link("India speech and voice market", "S2")

st.caption(
    f"Broader ecosystem context: India IoT market is estimated externally "
    f"at US$50.14B in 2025 and US$95.8B in 2030."
)


# ============================================================
# 11 — BUSINESS MODEL
# ============================================================

section(
    "11",
    "Business Model",
    "How VAANI can move from a technical prototype into a sustainable B2B edge-AI product."
)

business = pd.DataFrame({
    "Customer": [
        "IoT OEM",
        "Industrial integrator",
        "Enterprise fleet",
        "Government / public-sector project",
        "Hardware buyer / developer",
    ],
    "Problem they pay to solve": [
        "Need embedded voice activation",
        "Need customized voice interfaces",
        "Need fleet-wide deployment",
        "Need local/low-connectivity voice interfaces",
        "Need ready reference hardware",
    ],
    "What they pay for": [
        "Custom KWS + firmware integration",
        "Reference design + engineering",
        "Support + updates + deployment",
        "Project implementation",
        "Hardware + integration",
    ],
    "Revenue model": [
        "Per-device / product-family license",
        "Project contract",
        "Annual support",
        "Government contract / project",
        "Hardware margin + services",
    ],
})

st.dataframe(
    business,
    use_container_width=True,
    hide_index=True,
)


business_flow = """
digraph G {

    rankdir=LR;
    bgcolor="transparent";

    node [
        shape=box,
        style="rounded,filled",
        fillcolor="#0B1624",
        fontcolor="white",
        color="#22D3EE",
        fontname="Arial",
        penwidth=1.5
    ];

    core [label="VAANI\\nReference Technology"];
    pilot [label="Pilot\\nDeployment"];
    custom [label="Custom KWS +\\nFirmware"];
    deploy [label="OEM / Enterprise\\nDeployment"];
    support [label="Annual Support +\\nUpdates"];
    fleet [label="Fleet\\nExpansion"];

    core -> pilot -> custom -> deploy -> support -> fleet;

    fleet -> custom [label="New products"];
}
"""

st.graphviz_chart(
    business_flow,
    use_container_width=True,
)

st.markdown(
    dedent("""
    <div class="info-box">
    <b>Commercial principle:</b>
    VAANI is positioned primarily as an edge-AI technology layer and
    reference architecture. Commercialization can combine integration
    contracts, per-device licensing, hardware, support and deployment services.
    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# 12 — SCALABILITY
# ============================================================

section(
    "12",
    "Scalability — Prototype to Large Deployment",
    "The architecture separates device-side activation from scalable remote intelligence."
)

scale = pd.DataFrame({
    "Stage": [
        "Prototype",
        "Pilot",
        "Production",
        "Large deployment",
    ],
    "Indicative device scale": [
        "1–10",
        "10–100",
        "100–10,000",
        "10,000+",
    ],
    "Infrastructure": [
        "Device + test ASR",
        "Provisioning + logging",
        "Fleet management + monitoring",
        "Regional backend + scalable ASR workers",
    ],
    "Main engineering focus": [
        "Measurement",
        "Reliability + versioning",
        "Operations + support",
        "Autoscaling + cost control",
    ],
})

st.dataframe(
    scale,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# 13 — VALIDATION AND IMPACT
# ============================================================

section(
    "13",
    "Validation + Real-World Impact",
    "The final demonstration should connect technical measurements directly to user impact."
)

impact = pd.DataFrame({
    "Desired outcome": [
        "Less unnecessary audio transfer",
        "Lower remote ASR usage",
        "Local activation",
        "MCU-class deployment",
        "Lower false activation rate",
        "Low-latency handoff",
        "Network resilience",
    ],
    "How to demonstrate it": [
        "Packet capture during idle listening",
        "Compare ASR minutes with and without edge gating",
        "T0 → T1 local detection",
        "RAM / Flash / CPU measurement",
        "False activations/hour",
        "T0 → T3 timing",
        "Run wake detection with network unavailable",
    ],
    "Evidence": [
        "Network log",
        "ASR usage log",
        "MCU timestamps",
        "Profiler output",
        "Long-duration test",
        "Latency log",
        "Offline test video/log",
    ],
})

st.dataframe(
    impact,
    use_container_width=True,
    hide_index=True,
)

st.markdown(
    dedent("""
    <div class="warning-box">
    <b>Do not label these results as achieved until measured.</b>
    The website currently presents the engineering target and validation
    method. Once hardware testing is complete, the actual measured values
    should replace the target placeholders.
    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# 14 — ROADMAP
# ============================================================

section(
    "14",
    "Implementation Roadmap",
    "The project progresses from architecture to a measured physical prototype and finally to deployment."
)

roadmap = pd.DataFrame({
    "Phase": [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
    ],
    "Stage": [
        "Architecture",
        "Dataset",
        "TinyML",
        "MCU",
        "Wake Handoff",
        "Hardening",
        "Demonstration",
        "Productization",
    ],
    "Deliverable": [
        "PS traceability + system architecture",
        "Custom keyword + negatives + noise",
        "Compact KWS + INT8",
        "Real-time microphone + local inference",
        "Ring buffer + post-wake streaming",
        "Noise + distance + unseen-speaker tests",
        "Physical device + digital twin",
        "Pilot fleet + OTA + support",
    ],
})

st.dataframe(
    roadmap,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# 15 — TECHNOLOGY STACK
# ============================================================

section(
    "15",
    "Technology Stack",
    "Open-source and embedded-oriented technologies supporting the VAANI architecture."
)

stack = pd.DataFrame({
    "Layer": [
        "Audio",
        "DSP",
        "AI",
        "Edge Runtime",
        "MCU",
        "Connectivity",
        "Backend",
        "Visualization",
    ],
    "Technology": [
        "I2S MEMS microphone",
        "MFCC / Log-Mel features",
        "Custom TinyML KWS",
        "TensorFlow Lite Micro / equivalent",
        "ESP32-S3",
        "Wi-Fi",
        "Python / remote ASR service",
        "Streamlit + HTML + Three.js",
    ],
    "Purpose": [
        "Continuous audio capture",
        "Compact feature extraction",
        "Wake-word classification",
        "MCU inference",
        "Edge execution",
        "Post-wake communication",
        "Heavy speech processing",
        "Portfolio + digital twin",
    ],
})

st.dataframe(
    stack,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# 16 — FINAL SIH POSITIONING
# ============================================================

section(
    "16",
    "VAANI in One View",
    "The complete system can be understood as one simple engineering loop."
)

final_flow = """
digraph G {

    rankdir=LR;
    bgcolor="transparent";

    node [
        shape=box,
        style="rounded,filled",
        fillcolor="#0B1624",
        fontcolor="white",
        color="#22D3EE",
        fontname="Arial",
        penwidth=1.6
    ];

    listen [label="ALWAYS-ON\\nLOCAL LISTENING"];
    kws [label="CUSTOM\\nTINYML KWS"];
    decision [label="WAKE?"];

    offline [label="NO\\nSTAY OFFLINE", color="#22C55E"];
    wake [label="YES\\nWAKE EVENT", color="#F59E0B"];

    buffer [label="PRE-ROLL\\nBUFFER"];
    network [label="WI-FI\\nSTREAM"];
    asr [label="REMOTE\\nASR"];
    response [label="RESPONSE"];

    listen -> kws -> decision;

    decision -> offline [label="NO"];
    offline -> listen;

    decision -> wake [label="YES"];
    wake -> buffer -> network -> asr -> response;

    response -> listen;
}
"""

st.graphviz_chart(
    final_flow,
    use_container_width=True,
)

st.markdown(
    dedent("""
    <div class="green-box">
    <b>VAANI principle:</b>
    Local intelligence decides when the device should listen remotely.
    Remote intelligence is used only when the user actually activates the system.
    </div>
    """),
    unsafe_allow_html=True,
)


# ============================================================
# 17 — RESEARCH SOURCES
# ============================================================

section(
    "17",
    "Research Sources",
    "Important external facts used throughout this portfolio."
)

source_names = {
    "S1": "SIH26172 Problem Statement",
    "S2": "MarketsandMarkets — India Speech & Voice Recognition",
    "S3": "MarketsandMarkets — India IoT",
    "S4": "Google Cloud — Speech-to-Text Pricing",
    "S5": "PoPETs — Smart-Speaker Misactivation Research",
    "S6": "PIB — India Internet / Rural Connectivity",
    "S7": "PIB — Smart Cities Mission",
    "S8": "PIB / MeitY — Electronics Production",
    "S9": "Espressif — ESP32-S3 Datasheet",
    "S10": "Espressif — ESP32-S3 Documentation",
    "S11": "Arm — Keyword Spotting on Cortex-M",
    "S12": "Google Research — Speech Commands Dataset",
    "S13": "MeitY — DPDP Rules 2025",
    "S14": "Wavtron India — ESP32-S3 Reference Price",
    "S15": "FindMyChips — INMP441 Reference",
    "S16": "Electrobot India — INMP441 Reference",
}

for key, name in source_names.items():
    st.markdown(
        dedent(f"""
        <div class="source">
            <b>{key}</b> — {name}
            ·
            <a href="{SOURCES[key]}" target="_blank">
                Open source ↗
            </a>
        </div>
        """),
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    dedent("""
    <div class="footer">
        <b>VAANI · SIH26172</b><br><br>
        Edge-first voice activation for low-power intelligent devices.<br>
        External market figures are identified as external.
        TAM/SAM/SOM values are modelled.
        VAANI hardware performance must be measured before being labelled as achieved.
    </div>
    """),
    unsafe_allow_html=True,
)
