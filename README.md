# VAANI — Low Latency and Efficient Voice Activator for Edge Devices

### SIH26172 · ISRO · Smart India Hackathon 2026

VAANI is an **offline-first hybrid voice activation system** designed for low-power edge devices.

The core idea is simple:

> **Keep everyday voice activation and wake-word detection on the edge. Use the network and remote ASR only when the task requires it.**

---

## 1. Problem

Traditional cloud-first voice systems can continuously depend on network connectivity for voice processing.

This can introduce:

- Network dependency
- Additional latency
- Unnecessary audio transmission
- Higher bandwidth requirements
- Increased privacy exposure
- Reduced usability in low-connectivity environments

VAANI addresses this by moving the always-on wake detection stage to a low-resource edge device.

---

# 2. VAANI Architecture

```text
                    VAANI
                      │
                      ▼
              ┌───────────────┐
              │ I2S MEMS MIC  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │     ESP32     │
              │               │
              │ Audio Capture │
              │ MFCC / Log-Mel│
              │ TinyML KWS    │
              │ Decision Logic│
              └───────┬───────┘
                      │
                Wake detected?
                 /           \
               NO             YES
               │               │
               ▼               ▼
       Continue local      Audio Buffer
          listening             │
                               ▼
                             Wi-Fi
                               │
                               ▼
                          Remote ASR
                               │
                               ▼
                            Response
