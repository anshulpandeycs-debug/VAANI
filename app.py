
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="VAANI — SIH26172",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Theme / styling
# -----------------------------
st.markdown("""
<style>
:root {
  --navy:#07111F;
  --blue:#2563EB;
  --cyan:#22D3EE;
  --white:#F8FAFC;
  --slate:#64748B;
  --panel:#0D1B2A;
}
html, body, [class*="css"] {
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.stApp {
  background:
    radial-gradient(circle at 15% 10%, rgba(37,99,235,.18), transparent 28%),
    radial-gradient(circle at 85% 15%, rgba(34,211,238,.10), transparent 25%),
    linear-gradient(180deg, #07111F 0%, #091523 48%, #07111F 100%);
  color:#F8FAFC;
}
.block-container {max-width: 1250px; padding-top: 2rem; padding-bottom: 4rem;}
.hero {
  padding: 42px 34px;
  border:1px solid rgba(34,211,238,.20);
  border-radius:24px;
  background:linear-gradient(135deg, rgba(13,27,42,.96), rgba(7,17,31,.92));
  box-shadow:0 20px 70px rgba(0,0,0,.28);
}
.kicker {color:#22D3EE; font-size:.82rem; letter-spacing:.16em; text-transform:uppercase; font-weight:700;}
.hero h1 {font-size:4rem; line-height:1; margin:.25rem 0 .8rem; color:#F8FAFC;}
.hero p {font-size:1.12rem; color:#CBD5E1; max-width:900px;}
.badge {
 display:inline-block; padding:6px 11px; margin:4px 6px 4px 0;
 border-radius:999px; background:rgba(37,99,235,.16);
 border:1px solid rgba(37,99,235,.35); color:#BFDBFE; font-size:.78rem;
}
.metricbox {
 padding:18px; border-radius:16px; min-height:120px;
 background:rgba(13,27,42,.82); border:1px solid rgba(148,163,184,.14);
}
.metricbox .n {font-size:1.75rem; font-weight:800; color:#F8FAFC;}
.metricbox .l {font-size:.82rem; color:#94A3B8;}
.metricbox .s {font-size:.72rem; color:#22D3EE; margin-top:7px;}
.section {
 margin-top:34px; margin-bottom:14px;
}
.smallsource {font-size:.74rem; color:#94A3B8;}
.local {color:#22D3EE; font-weight:700;}
.network {color:#60A5FA; font-weight:700;}
.warning {
 padding:14px 16px; border-left:4px solid #F59E0B;
 background:rgba(245,158,11,.08); border-radius:8px; color:#FDE68A;
}
.source {
 padding:10px 12px; border-left:3px solid #22D3EE;
 background:rgba(34,211,238,.06); border-radius:7px;
 margin:7px 0;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Evidence constants
# -----------------------------
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
    st.markdown(f'<div class="source"><b>{label}</b> · <a href="{SOURCES[key]}" target="_blank">{key} source</a></div>', unsafe_allow_html=True)

# -----------------------------
# Hero
# -----------------------------
st.markdown("""
<div class="hero">
  <div class="kicker">SMART INDIA HACKATHON 2026 · ISRO · HARDWARE · SMART AUTOMATION</div>
  <h1>VAANI</h1>
  <p><b>Local Wake. Remote Intelligence.</b><br>
  An edge-first voice activation layer that detects a custom keyword locally on a resource-constrained MCU and invokes remote speech recognition only after a valid wake event.</p>
  <span class="badge">SIH26172</span>
  <span class="badge">Custom KWS</span>
  <span class="badge">TinyML</span>
  <span class="badge">Offline-first</span>
  <span class="badge">Post-wake streaming</span>
  <span class="badge">Open-source stack</span>
</div>
""", unsafe_allow_html=True)

st.write("")
c1,c2,c3,c4 = st.columns(4)
for c, n, l, s in [
    (c1,"<256 KB","SIH edge RAM boundary","S1"),
    (c2,"<10%","SIH idle CPU boundary","S1"),
    (c3,"₹3,516 Cr","India voice/speech market, 2025","S2"),
    (c4,"101.78 Cr","India internet subscribers, Sep 2025","S6"),
]:
    with c:
        st.markdown(f'<div class="metricbox"><div class="n">{n}</div><div class="l">{l}</div><div class="s">{s} · source</div></div>', unsafe_allow_html=True)

# -----------------------------
# Problem
# -----------------------------
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.header("1. The Problem — SIH26172")
st.write(
    "SIH26172 asks for an ultra-lightweight custom keyword-spotting system that runs locally on a low-power device. "
    "After detecting the keyword, the device should efficiently stream subsequent audio to remote ASR with minimal overhead and latency. "
    "The evaluation explicitly focuses on RAM/Flash, idle CPU, true-positive rate, false activations and wake-to-ASR latency."
)
source_link("Official problem-statement record", "S1")

p1,p2,p3 = st.columns(3)
with p1:
    st.subheader("Always listening")
    st.write("The device must continuously inspect audio without turning the full speech stack into an always-on cloud workload.")
with p2:
    st.subheader("False activations")
    st.write("A wrong wake event can create unwanted recordings, ASR sessions, cost and privacy exposure.")
with p3:
    st.subheader("Latency")
    st.write("The wake-word end → first server packet interval is a direct SIH evaluation metric.")

# -----------------------------
# Evidence
# -----------------------------
st.header("2. Why the Problem Is Real — Indian + Technical Evidence")

e1,e2,e3,e4 = st.columns(4)
with e1:
    st.metric("India voice/speech", f"₹{VOICE_2025_CR:,.0f} Cr", "2025 reported market value")
with e2:
    st.metric("India IoT", f"₹{IOT_2025_CR/100000:,.2f} lakh Cr", "2025 reported market value")
with e3:
    st.metric("Rural internet", "42.77 Cr", "Sep 2025")
with e4:
    st.metric("Village mobile coverage", "98.09%", "Dec 2025")

st.caption("Source basis: S2, S3, S6. INR conversions use ₹95.98/US$ as a dated reference rate; market values are external research estimates.")

evidence = pd.DataFrame({
    "Evidence": [
        "India speech & voice recognition market",
        "India IoT market",
        "Internet subscribers in India",
        "Rural internet subscribers",
        "Villages with mobile connectivity",
        "Smart Cities Mission projects",
        "Electronics production",
        "External smart-speaker misactivation study",
    ],
    "Numeric fact": [
        "US$366.3M in 2025 → US$954.3M in 2030; 21.1% CAGR",
        "US$50.14B in 2025 → US$95.8B in 2030; 13.8% CAGR",
        "101.78 crore at 30 Sep 2025",
        "42.77 crore at 30 Sep 2025",
        "98.09% of villages reported with mobile connectivity at 31 Dec 2025",
        "8,066 projects / ₹1,64,669 Cr orders; 7,352 completed by 15 Nov 2024",
        "Over ₹13 lakh crore production; ~25 lakh jobs reported in 2026",
        "0.95 misactivations/hour in a controlled US/UK study",
    ],
})
st.dataframe(evidence, use_container_width=True, hide_index=True)
source_link("India voice market", "S2")
source_link("India IoT market", "S3")
source_link("India connectivity", "S6")
source_link("Smart Cities Mission", "S7")
source_link("Electronics ecosystem", "S8")
source_link("Wake-word misactivation research", "S5")

# -----------------------------
# Cost / ASR
# -----------------------------
st.header("3. Cost + Network Logic")
st.write(
    f"Google Cloud Speech-to-Text V2 Standard is publicly listed at US$0.016/min for the first 500,000 minutes/month/account. "
    f"At the dated reference rate of ₹{FX:.2f}/US$, that is approximately ₹{STT_INR_MIN:.2f}/minute."
)
source_link("Cloud ASR price reference", "S4")

mins = [5,15,30,60]
cost_df = pd.DataFrame({
    "Daily ASR minutes": mins,
    "Monthly minutes": [m*30 for m in mins],
    "Reference monthly ASR cost (₹)": [m*30*STT_INR_MIN for m in mins],
})
st.bar_chart(cost_df.set_index("Daily ASR minutes")["Reference monthly ASR cost (₹)"])
st.caption("Scenario arithmetic only. Excludes other cloud/network/storage costs and is not a VAANI measured bill.")

st.info(
    "VAANI's claim is not “cloud is bad.” The engineering claim is: keep the always-on wake decision local and "
    "invoke remote ASR only after the user actually wakes the device."
)

# -----------------------------
# Solution
# -----------------------------
st.header("4. VAANI Solution")
st.write("The system has a deliberately narrow job: local activation first, remote speech intelligence second.")

flow = """
digraph G {
rankdir=LR;
node [shape=box style="rounded,filled" fillcolor="#0D1B2A" fontcolor="white" color="#22D3EE"];
mic [label="I2S MEMS\\nMicrophone"];
pcm [label="PCM\\nBuffer"];
dsp [label="MFCC / Log-Mel\\nDSP"];
kws [label="Tiny INT8\\nCustom KWS"];
dec [label="Confidence +\\nTemporal Decision"];
keep [label="NO → Keep\\nListening Locally"];
pre [label="YES → Ring Buffer\\nPre-roll"];
stream [label="Post-wake\\nAudio Stream"];
asr [label="Remote\\nASR"];
app [label="Transcript /\\nApplication"];
mic->pcm->dsp->kws->dec;
dec->keep [label="NO"];
dec->pre [label="YES"];
pre->stream->asr->app;
}
"""
st.graphviz_chart(flow, use_container_width=True)

a,b = st.columns(2)
with a:
    st.subheader("LOCAL path")
    st.markdown("**Mic → DSP → KWS → decision**")
    st.write("Ordinary ambient audio stays on the edge. The device does not need remote ASR to decide whether the wake word occurred.")
with b:
    st.subheader("NETWORK path")
    st.markdown("**Wake → pre-roll → stream → ASR**")
    st.write("Only after a valid wake event does the system open the remote speech path.")

# -----------------------------
# Uniqueness
# -----------------------------
st.header("5. Uniqueness — System-Level, Not Hype")
comparison = pd.DataFrame({
    "Dimension": ["Always-on decision","Network dependency","Custom keyword","Idle resource design","Streaming policy","Measurement"],
    "Cloud-first voice path": [
        "Remote processing may be involved before useful command audio is known",
        "Wake experience can depend on network",
        "Often fixed ecosystem keyword",
        "General speech stack may be too heavy for MCU",
        "Can involve broad/continuous remote audio path",
        "Often UX-focused rather than MCU-budget focused",
    ],
    "VAANI": [
        "Local custom KWS",
        "Wake decision is local",
        "Deployment-specific custom keyword",
        "Compact KWS + DSP + INT8",
        "Stream only after local wake",
        "RAM + CPU + TPR + false activations/hour + T0→T3",
    ],
})
st.dataframe(comparison, use_container_width=True, hide_index=True)

st.write(
    "Compact KWS is an established field. Published work such as “Hello Edge” demonstrated that DS-CNN-style architectures can be "
    "tuned for microcontrollers; one reported evaluation achieved 95.4% accuracy. Arm also published a Cortex-M example of roughly "
    "70 KB memory for the KWS application and about 12 ms per inference in its stated setup. These are external benchmarks, not VAANI results."
)
source_link("Arm KWS benchmark", "S11")

# -----------------------------
# Hardware
# -----------------------------
st.header("6. Hardware Feasibility")
hw = pd.DataFrame({
    "Component": ["ESP32-S3", "I2S MEMS microphone", "TinyML runtime", "Wi-Fi"],
    "Role": [
        "MCU + local inference + connectivity",
        "Digital audio capture",
        "Compact local KWS inference",
        "Post-wake ASR transport",
    ],
    "Reference": [
        "512 KB SRAM, up to 240 MHz, Wi-Fi/BLE, vector instructions",
        "INMP441-class I2S MEMS mic",
        "Open-source micro inference stack",
        "Integrated 2.4 GHz Wi-Fi on ESP32-S3",
    ],
})
st.dataframe(hw, use_container_width=True, hide_index=True)
source_link("ESP32-S3 datasheet", "S9")
source_link("ESP32-S3 product documentation", "S10")

st.caption("Current Indian component listings vary. Example references: ESP32-S3 DevKitC N16R8 around ₹760 at one Indian retailer; INMP441 listings around ₹145–₹265 depending on supplier/quantity. These are prototype-price references, not manufacturing BOM guarantees.")
source_link("ESP32-S3 Indian price reference", "S14")
source_link("INMP441 Indian price reference", "S15")

# -----------------------------
# Metrics
# -----------------------------
st.header("7. SIH Validation Dashboard")
st.warning("Only numbers produced by VAANI's actual hardware/test logs should be labelled “VAANI MEASURED”. External benchmarks below are deliberately kept separate.")

metrics = pd.DataFrame({
    "Metric": ["RAM","Idle CPU","TPR / recall","False activations/hour","Miss rate","Inference latency","Wake-to-ASR latency","Power"],
    "SIH / engineering definition": [
        "<256 KB",
        "<10%",
        "High",
        "Near zero",
        "Low",
        "Low",
        "T3 − T0",
        "Low",
    ],
    "Measurement method": [
        "Peak runtime + inference arena/buffers",
        "Continuous idle listening over fixed window",
        "Correct wake detections / wake trials",
        "False wake events / hour",
        "Missed wake / wake trials",
        "Feature + inference timing",
        "Mean / median / P95",
        "Idle vs active current/energy",
    ],
})
st.dataframe(metrics, use_container_width=True, hide_index=True)

latency = """
digraph G {
rankdir=LR;
node [shape=box style="rounded,filled" fillcolor="#0D1B2A" fontcolor="white" color="#60A5FA"];
t0 [label="T0\\nKeyword ends"];
t1 [label="T1\\nLocal detection"];
t2 [label="T2\\nStream starts"];
t3 [label="T3\\nFirst packet received"];
t0->t1->t2->t3;
}
"""
st.graphviz_chart(latency, use_container_width=True)
st.caption("Primary SIH latency = T3 − T0. Also report T1−T0, T2−T1 and T3−T2; use mean, median and P95.")

# -----------------------------
# Market
# -----------------------------
st.header("8. India Market — TAM / SAM / SOM")
st.write(
    f"Primary TAM is the India speech and voice recognition market. The 2025 reported value is US$366.3M. "
    f"Using ₹{FX:.2f}/US$, that is approximately ₹{VOICE_2025_CR:,.0f} crore."
)

market_df = pd.DataFrame({
    "Layer": ["TAM","SAM","SOM"],
    "₹ crore": [VOICE_2025_CR, SAM_CR, SOM_CR],
})
st.bar_chart(market_df.set_index("Layer")["₹ crore"])

m1,m2,m3 = st.columns(3)
with m1:
    st.metric("TAM", f"₹{VOICE_2025_CR:,.0f} Cr", "Reported India voice/speech market, 2025")
with m2:
    st.metric("SAM", f"₹{SAM_CR:,.0f} Cr", "25% modelled edge/IoT subset")
with m3:
    st.metric("SOM", f"₹{SOM_CR:,.1f} Cr", "3% modelled share scenario")

st.markdown("""
**Calculation**
1. TAM = US$366.3M × ₹95.98/US$ ≈ ₹3,516 Cr.
2. SAM = TAM × 25% ≈ ₹879 Cr. **Modelled assumption**, not a published market number.
3. SOM = SAM × 3% ≈ ₹26.4 Cr/year. **Planning scenario**, not a forecast.
""")
source_link("India voice/speech market source", "S2")
st.caption("The broader India IoT market is ecosystem context, not additional TAM. It is reported at US$50.14B in 2025 and US$95.8B in 2030.")

# -----------------------------
# Business
# -----------------------------
st.header("9. Revenue / Business Model")
bm = pd.DataFrame({
    "Customer": ["IoT OEM","Industrial integrator","Enterprise fleet","Government/public-sector pilot","Reference-hardware buyer"],
    "Pays for": ["Custom KWS + firmware integration","Reference design + integration","Support + updates + monitoring","Project deployment","Hardware + integration/support"],
    "Revenue": ["Per-device / product-family license","Project contract","Annual support/SaaS","Tender/project contract","Hardware margin + services"],
})
st.dataframe(bm, use_container_width=True, hide_index=True)

business_flow = """
digraph G {
rankdir=LR;
node [shape=box style="rounded,filled" fillcolor="#0D1B2A" fontcolor="white" color="#22D3EE"];
tech [label="VAANI Reference\\nTechnology"];
pilot [label="Low-cost\\nPilot"];
custom [label="Custom KWS +\\nFirmware Integration"];
deploy [label="OEM / Enterprise\\nDeployment"];
support [label="Annual Support +\\nModel/Firmware Updates"];
fleet [label="Fleet Scale"];
tech->pilot->custom->deploy->support->fleet;
fleet->custom [label="new products"];
}
"""
st.graphviz_chart(business_flow, use_container_width=True)
st.caption("Illustrative commercial pricing bands should be treated as planning assumptions, not claimed market prices.")

# -----------------------------
# Scalability
# -----------------------------
st.header("10. Scalability — Pilot to Fleet")
scale = pd.DataFrame({
    "Stage":["Prototype","Pilot","Production","Large deployment"],
    "Scale":["1–10","10–100","100–10,000","10,000+"],
    "Infrastructure":["Device + test ASR","Provisioning + logs","Fleet management + monitoring","Regional backend + scalable ASR workers"],
    "Main focus":["Measurement","OTA/versioning","Reliability/support","Autoscaling/SLA/cost control"],
})
st.dataframe(scale, use_container_width=True, hide_index=True)

# -----------------------------
# Impact
# -----------------------------
st.header("11. Validation & User Impact")
impact = pd.DataFrame({
    "Outcome": [
        "Less unnecessary audio transfer",
        "Lower remote-ASR usage",
        "Local activation",
        "MCU-class deployment",
        "Better measurable reliability",
        "Deployment resilience",
    ],
    "How to prove it": [
        "Network packet log during idle listening",
        "ASR minutes before/after edge gating",
        "T0→T1 timing",
        "RAM/CPU/model-size logs",
        "TPR + false activations/hour",
        "Wake test with network unavailable",
    ],
})
st.dataframe(impact, use_container_width=True, hide_index=True)

st.markdown("""
<div class="warning">
<strong>Validation rule:</strong> external statistics prove that the problem exists and the technology class is feasible.
VAANI's own claims must come from reproducible hardware/test evidence.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Digital Twin
# -----------------------------
st.header("12. Interactive 3D Digital Twin")
st.write(
    "The digital twin should represent the physical edge architecture: microphone, MCU, local KWS, ring buffer, Wi-Fi, remote ASR and output. "
    "It is a software simulation of the physical architecture, not a claim of electrical-physics simulation."
)

twin_path = Path("assets/digital_twin/index.html")
if twin_path.exists():
    components.html(twin_path.read_text(encoding="utf-8"), height=720, scrolling=False)
else:
    st.info("Digital twin file not found in the current deployment. Add assets/digital_twin/index.html to the repository.")

# -----------------------------
# Roadmap
# -----------------------------
st.header("13. Deployment Roadmap")
roadmap = pd.DataFrame({
    "Phase":["Architecture","Dataset","TinyML","MCU","Handoff","Hardening","Demo","Product"],
    "Deliverable":[
        "PS traceability + architecture",
        "Custom keyword + negatives + noise",
        "Compact KWS + INT8",
        "Real-time microphone + local inference",
        "Ring buffer + post-wake streaming",
        "Noise/distance/unseen speaker testing",
        "Physical device + digital twin",
        "Pilot fleet + OTA + support",
    ]
})
st.dataframe(roadmap, use_container_width=True, hide_index=True)

# -----------------------------
# Sources
# -----------------------------
st.header("14. Research Sources")
source_names = {
"S1":"SIH26172 problem statement",
"S2":"MarketsandMarkets — India Speech & Voice Recognition",
"S3":"MarketsandMarkets — India IoT",
"S4":"Google Cloud — Speech-to-Text pricing",
"S5":"PoPETs — Smart-speaker misactivation research",
"S6":"PIB — India internet/rural subscribers and village connectivity",
"S7":"PIB — Smart Cities Mission",
"S8":"PIB / MeitY — Electronics production and jobs",
"S9":"Espressif — ESP32-S3 datasheet",
"S10":"Espressif — ESP32-S3 product documentation",
"S11":"Arm — Keyword spotting on Cortex-M",
"S12":"Google Research — Speech Commands Dataset",
"S13":"MeitY — DPDP Rules 2025",
"S14":"Wavtron India — ESP32-S3 DevKitC reference price",
"S15":"FindMyChips India — INMP441 reference prices",
"S16":"Electrobot India — INMP441 reference price",
}
for k,v in source_names.items():
    st.markdown(f"- **{k} — {v}:** {SOURCES[k]}")

st.divider()
st.caption(
    "VAANI SIH26172 · Evidence-led portfolio · Market figures are external estimates · "
    "TAM/SAM/SOM assumptions are modelled · Hardware performance must be measured on the target MCU before being labelled as VAANI results."
)
