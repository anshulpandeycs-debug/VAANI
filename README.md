# VAANI — Low-Latency & Efficient Voice Activator for Edge Devices

### Smart India Hackathon 2026 — SIH26172

**Organization:** ISRO / Department of Space
**Category:** Hardware
**Theme:** Smart Automation
**Project:** VAANI — Edge AI Voice Activation System

---

## 🚀 Project Overview

**VAANI** is an offline-first, low-latency voice activation system designed for **low-power edge devices**.

The system detects a **custom wake word locally on the edge device** using a lightweight TinyML model. It does not continuously send microphone audio to the cloud.

Only after the wake word is detected does VAANI optionally activate Wi-Fi communication and send the following speech to a remote Automatic Speech Recognition (ASR) service.

This architecture reduces unnecessary network usage, improves privacy, and minimizes activation latency while keeping the edge AI system lightweight.

---

## 🎯 SIH Problem Statement

Cloud-based voice-controlled IoT systems can introduce:

* Network latency
* Continuous data transmission
* Higher bandwidth consumption
* Privacy concerns
* Dependence on internet connectivity
* Higher computational and operational costs

VAANI addresses this problem by moving the **wake-word detection stage to the edge device**.

### Core Concept

```text
                 ┌──────────────────────┐
                 │   I2S MEMS Microphone│
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │     ESP32 / MCU      │
                 │   Local Processing   │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ MFCC / Log-Mel       │
                 │ Feature Extraction   │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ TinyML Keyword       │
                 │ Spotting Model       │
                 └──────────┬───────────┘
                            ↓
                    ┌───────┴───────┐
                    │               │
                  NO │               │ YES
                    ↓               ↓
              Keep Listening   Wake Detected
                                    ↓
                              Audio Buffer
                                    ↓
                                  Wi-Fi
                                    ↓
                              Remote ASR
                                    ↓
                               Response
                                    ↓
                              Back to Edge
```

---

# 🧠 VAANI Architecture

VAANI follows an **offline-first hybrid architecture**.

### Offline Mode — Default

The device continuously listens locally for the custom keyword.

```text
Microphone
    ↓
Audio Capture
    ↓
Feature Extraction
    ↓
TinyML KWS
    ↓
Decision
    ↓
Keep Listening
```

No continuous cloud audio transmission is required.

### Online Mode — Only After Wake Detection

When the custom keyword is detected:

```text
Wake Word
    ↓
Audio Buffer / Pre-roll
    ↓
Wi-Fi Activation
    ↓
Audio Streaming
    ↓
Remote ASR
    ↓
Recognized Command
    ↓
Response
    ↓
Return to Offline Listening
```

This makes the network path **event-driven instead of continuous**.

---

# ⚡ Why VAANI?

| Challenge                              | Conventional Cloud Voice System | VAANI               |
| -------------------------------------- | ------------------------------- | ------------------- |
| Wake-word detection                    | Cloud / network dependent       | Local edge          |
| Continuous audio transmission          | Possible                        | Avoided             |
| Internet dependency for wake detection | High                            | No                  |
| Privacy exposure                       | Higher                          | Reduced             |
| Edge computation                       | Low                             | Lightweight TinyML  |
| Network activation                     | Continuous / frequent           | Only after wake     |
| Low-power operation                    | Challenging                     | Primary design goal |
| Custom keyword                         | Depends on system               | Yes                 |
| Physical MCU deployment                | Not necessarily                 | Required            |

---

# 🎯 Project Objectives

VAANI is designed around the following objectives:

1. Develop a custom keyword spotting system.
2. Run wake-word detection directly on an edge MCU.
3. Keep the edge model lightweight.
4. Minimize RAM and Flash requirements.
5. Keep idle CPU usage low.
6. Reduce unnecessary audio transmission.
7. Minimize wake-to-ASR latency.
8. Support physical hardware validation.
9. Use open-source technologies.
10. Provide measurable and reproducible benchmarks.

---

# 📌 SIH Engineering Targets

The project architecture is designed around the following SIH requirements:

| Parameter               |             Target |
| ----------------------- | -----------------: |
| Edge RAM usage          |       **< 256 KB** |
| Idle CPU usage          |          **< 10%** |
| Keyword                 | **Custom keyword** |
| Model type              | Lightweight TinyML |
| Quantization            |               INT8 |
| Wake detection          |              Local |
| Continuous cloud audio  |                 No |
| Physical validation     |           Required |
| Heavy Transformer model |           Not used |

> These are engineering targets. Final measured values will be reported after physical hardware benchmarking.

---

# 🤖 TinyML Keyword Spotting

The core AI component of VAANI is a lightweight **Keyword Spotting (KWS)** model.

### Processing Pipeline

```text
Raw Audio
    ↓
Preprocessing
    ↓
MFCC / Log-Mel Features
    ↓
Lightweight Neural Network
    ↓
INT8 Quantization
    ↓
Keyword Probability
    ↓
Temporal Decision Logic
    ↓
Wake / No Wake
```

The model is intended to run locally on the edge MCU rather than requiring a large cloud-based neural network.

---

# 🔊 Audio Capture

VAANI uses an **I2S MEMS microphone** for digital audio capture.

### Audio path

```text
I2S MEMS Microphone
          ↓
       ESP32
          ↓
   Audio Buffer
          ↓
 Feature Extraction
```

The microphone continuously provides audio to the local processing pipeline.

The audio is processed locally until the keyword spotting model detects the custom activation keyword.

---

# 🧩 Wake Detection

VAANI does not activate the network merely because sound is present.

The activation sequence is:

```text
Audio
 ↓
Feature Extraction
 ↓
KWS Model
 ↓
Confidence Evaluation
 ↓
Temporal Smoothing
 ↓
Wake Confirmation
```

This helps reduce false activations caused by short noise events or isolated predictions.

---

# 📡 Low-Latency Audio Handoff

Once the keyword is confirmed, VAANI transitions from local listening to the network processing stage.

```text
T0 = Keyword ends
        ↓
T1 = Local detection
        ↓
T2 = Streaming starts
        ↓
T3 = First audio packet reaches server
```

### Primary latency metric

```text
Wake-to-ASR Latency = T3 − T0
```

The final system will report:

* Mean latency
* Median latency
* P95 latency

This provides a more useful picture of real-world performance than reporting only a single best-case latency.

---

# 💾 Edge Resource Optimization

VAANI is designed for resource-constrained hardware.

Optimization techniques include:

* Lightweight neural network architecture
* INT8 quantization
* Compact feature representation
* Efficient audio buffering
* Local wake detection
* Event-driven networking
* Reduced memory allocation
* Low idle processing requirements

The objective is to keep the always-listening portion of the system within the SIH resource constraints.

---

# 🔐 Privacy-First Architecture

VAANI follows an **offline-first** philosophy.

The microphone does not need to continuously transmit raw audio to a remote server.

Instead:

```text
             LOCAL EDGE
                 │
        ┌────────▼────────┐
        │ Microphone      │
        │ Feature Extract │
        │ TinyML KWS      │
        └────────┬────────┘
                 │
          Wake detected?
             /       \
           NO         YES
           │           │
           ↓           ↓
      Stay Offline    Wi-Fi
                       │
                       ↓
                    Remote ASR
```

This reduces unnecessary transmission of ambient audio.

---

# 🌐 Hybrid Edge + Cloud Architecture

VAANI is **not designed as a cloud-dependent voice assistant**.

Instead, it divides the workload:

### Edge

Responsible for:

* Continuous listening
* Audio capture
* Feature extraction
* Wake-word detection
* Local decision making

### Remote Processing

Used only after activation for:

* Speech recognition
* Complex voice command processing
* Optional remote services

This allows the system to remain lightweight on the edge while still supporting more computationally expensive speech processing when required.

---

# 🖥️ Interactive 3D Digital Twin

The project includes an interactive **3D digital twin of the VAANI system architecture**.

The digital twin represents the intended physical hardware flow:

```text
┌───────────────┐
│ I2S MEMS Mic  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     ESP32     │
│   TinyML KWS  │
└───────┬───────┘
        │
        ▼
   Wake Detected
        │
        ▼
┌───────────────┐
│      Wi-Fi    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Remote ASR    │
│    Server     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Response    │
└───────────────┘
```

### Digital Twin Features

* Interactive system visualization
* Hardware component representation
* Signal-flow animation
* Offline/online mode
* Wake detection simulation
* Audio streaming simulation
* Remote ASR simulation
* Component information panels
* Reset and demo controls

> The current digital twin is a **software visualization of the physical architecture**, not a claim of electrical-physics simulation.

---

# 🔧 Planned Physical Hardware

The physical prototype is planned around:

```text
I2S MEMS Microphone
        ↓
      ESP32
        ↓
   TinyML KWS
        ↓
      Wi-Fi
        ↓
   Remote ASR
        ↓
     Output
```

### Main Hardware

* ESP32 development board
* I2S MEMS microphone
* Status LED
* Push button
* USB power/data connection
* Wi-Fi connectivity

Additional components may be added during hardware validation.

---

# 📊 Testing & Benchmarking

VAANI will be evaluated using measurable engineering metrics.

## 1. Accuracy

Metrics include:

* True Positive Rate
* False Positive Rate
* False Activations per Hour
* Detection Accuracy

Testing should include:

* Different speakers
* Different environments
* Background noise
* Different distances
* Different speaking conditions

---

## 2. Resource Usage

The edge implementation will measure:

* RAM usage
* Flash/model size
* CPU usage
* Idle processing load
* Inference time

---

## 3. Latency

The complete wake-to-ASR path will be measured.

```text
Keyword End
     ↓
Local Detection
     ↓
Network Start
     ↓
First Packet Received
```

Primary measurement:

```text
Latency = T3 − T0
```

Results will be reported using:

* Mean
* Median
* P95

---

# 🧪 Dataset Strategy

The KWS dataset will contain multiple categories:

### Positive Samples

Recordings containing the custom wake keyword.

### Negative Samples

Normal speech that should not activate VAANI.

### Background / Noise Samples

Examples including:

* Room noise
* Fans
* Traffic
* Keyboard sounds
* Conversations
* Other environmental noise

### Data Augmentation

Potential augmentation techniques include:

* Background noise mixing
* Volume variation
* Time shifting
* Small temporal variation
* Environmental variation

Speaker and environment separation will be considered during dataset splitting to reduce data leakage.

---

# 🛠️ Technology Stack

### Edge

* ESP32
* C/C++
* Arduino-compatible / vendor SDK environment
* TensorFlow Lite for Microcontrollers or equivalent TinyML framework
* DSP
* MFCC / Log-Mel features

### AI

* Python
* TensorFlow
* Lightweight CNN / DS-CNN style architecture
* INT8 quantization

### Backend

* Python
* Remote ASR interface
* Lightweight API / communication layer

### Website

* Streamlit
* HTML
* CSS
* JavaScript
* Interactive digital twin

### Development

* GitHub
* VS Code
* Arduino IDE
* Python environment

---

# 📁 Repository Structure

```text
VAANI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── digital_twin/
│       └── index.html
│
├── firmware/
│   └── (ESP32 firmware)
│
├── model/
│   └── (TinyML model files)
│
├── training/
│   └── (training scripts)
│
├── backend/
│   └── (remote ASR backend)
│
├── benchmarks/
│   └── (performance measurements)
│
└── docs/
    └── (project documentation)
```

---

# 📈 Business & Deployment Potential

VAANI can be adapted for applications where continuous cloud-based voice processing is undesirable or inefficient.

Potential application areas include:

* Smart home devices
* Industrial IoT
* Hands-free control systems
* Smart appliances
* Low-connectivity environments
* Privacy-sensitive voice interfaces
* Battery-powered edge devices
* Embedded automation systems
* Remote monitoring systems

The business model can evolve around:

```text
Hardware Integration
        ↓
Edge AI Software
        ↓
Custom Keyword Deployment
        ↓
Device / OEM Integration
        ↓
Optional Cloud / ASR Services
```

The commercial model will depend on actual hardware cost, deployment scale, ASR usage, and integration requirements.

---

# 🗺️ Development Roadmap

## Phase 1 — Software Architecture

* [x] Define SIH requirements
* [x] Design offline-first architecture
* [x] Create system flow
* [x] Create project website
* [x] Create interactive digital twin

## Phase 2 — Dataset & Model

* [ ] Build keyword dataset
* [ ] Add negative samples
* [ ] Add noise samples
* [ ] Train lightweight KWS model
* [ ] Evaluate accuracy
* [ ] Quantize model

## Phase 3 — ESP32 Deployment

* [ ] Configure I2S microphone
* [ ] Implement audio capture
* [ ] Deploy TinyML model
* [ ] Measure RAM
* [ ] Measure CPU
* [ ] Measure inference time

## Phase 4 — Wake-to-ASR Pipeline

* [ ] Implement wake detection
* [ ] Implement audio buffering
* [ ] Implement Wi-Fi handoff
* [ ] Implement remote ASR
* [ ] Measure latency

## Phase 5 — Physical Validation

* [ ] Assemble hardware
* [ ] Test different environments
* [ ] Measure false activations
* [ ] Measure latency
* [ ] Validate resource limits

## Phase 6 — Final Demonstration

* [ ] Connect physical hardware
* [ ] Synchronize digital twin
* [ ] Generate benchmark graphs
* [ ] Prepare final SIH presentation
* [ ] Demonstrate complete system

---

# 📊 Final Evaluation Metrics

The final project evaluation will focus on:

| Metric              | Measurement  |
| ------------------- | ------------ |
| RAM                 | KB           |
| Flash               | KB / MB      |
| Idle CPU            | %            |
| Inference Time      | ms           |
| True Positive Rate  | %            |
| False Activations   | /hour        |
| Wake-to-ASR Latency | ms           |
| Median Latency      | ms           |
| P95 Latency         | ms           |
| Network Usage       | KB / session |

All final performance numbers should be based on actual measurements from the implemented system.

---

# 🔬 Engineering Philosophy

VAANI follows five core principles:

### 1. Edge First

The first decision should happen locally.

### 2. Lightweight AI

The always-listening model should be small enough for constrained hardware.

### 3. Event-Driven Networking

Network processing starts only when required.

### 4. Measurable Performance

RAM, CPU, accuracy and latency must be measured rather than assumed.

### 5. Open Technology

The implementation should rely on open-source technologies and comply with the SIH restrictions.

---

# 🌍 Future Vision

The long-term vision for VAANI is to create a reusable **edge voice activation platform** that can operate across different low-power devices.

Future versions can include:

* Multiple custom keywords
* Multilingual keyword detection
* Better noise robustness
* Lower-power operation
* Fully local command recognition
* Hardware telemetry
* Real-time digital twin synchronization
* More advanced edge AI
* Device-to-device communication
* Offline command execution

The digital twin can eventually receive live telemetry from the physical ESP32 and mirror:

```text
Microphone Status
       ↓
KWS State
       ↓
Wake Detection
       ↓
Wi-Fi State
       ↓
ASR State
       ↓
Response State
```

---

# 👥 Target Users

VAANI can be useful for:

* Embedded-system developers
* IoT developers
* Edge-AI developers
* Smart-device manufacturers
* Industrial automation developers
* Hardware startups
* Privacy-focused product developers
* Low-connectivity system designers

---

# 🏆 Smart India Hackathon 2026

**Problem Statement:** SIH26172

**Project:** VAANI — Low-Latency and Efficient Voice Activator for Edge Devices

**Organization:** ISRO / Department of Space

**Category:** Hardware

**Theme:** Smart Automation

VAANI is designed around the SIH requirement of creating a lightweight custom keyword spotting system that operates locally on a low-power device and efficiently hands off audio to remote speech recognition only after activation.

---

# 📜 Project Status

### Current Status

🟢 Architecture Designed
🟢 Offline-first system defined
🟢 Website development started
🟢 Interactive digital twin created
🟢 GitHub repository created
🟡 TinyML model development
🟡 ESP32 hardware implementation
🟡 Remote ASR integration
🟡 Physical benchmarking

---

# 👨‍💻 Project Repository

This repository contains the development files for the VAANI project, including:

* Web interface
* Digital twin
* System architecture
* TinyML development
* ESP32 firmware
* Backend
* Benchmarking
* Documentation

---

# ⭐ VAANI

> **Listen locally. Wake instantly. Process efficiently.**

**VAANI — Bringing intelligent voice activation closer to the edge.**

---

## ⚠️ Important Note

VAANI is a research and prototype project developed for **Smart India Hackathon 2026**.

Performance figures should only be reported as final results after physical testing and measurement on the target hardware.

The system architecture and digital twin represent the intended implementation and should not be interpreted as evidence of completed hardware validation until those tests are performed.
