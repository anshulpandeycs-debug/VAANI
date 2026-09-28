# VAANI Backend

This folder contains the optional remote-processing backend for VAANI.

The backend is used **only after the edge device confirms the custom wake keyword**.

## Architecture

```text
ESP32
  ↓
Local TinyML Wake Detection
  ↓
Wake Confirmed
  ↓
Wi-Fi
  ↓
VAANI Backend
  ↓
Remote ASR
  ↓
Recognized Text
  ↓
Response
  ↓
ESP32 / Local Device
```

## Responsibilities

The backend may handle:

* Receiving post-wake audio
* Managing the ASR request
* Returning recognized text
* Returning command results
* Measuring network latency
* Logging request information
* Providing an interface between the edge device and ASR service

## Important Design Rule

The backend should **not** receive continuous microphone audio while VAANI is waiting for the wake keyword.

The intended behavior is:

```text
Listening
   ↓
Local KWS
   ↓
No Wake → Continue Local Processing

Wake Detected
   ↓
Start Network Handoff
   ↓
Send Required Audio
   ↓
ASR
   ↓
Response
   ↓
Return to Local Listening
```

## Latency Measurement

The backend will participate in measuring the wake-to-ASR pipeline.

Important timestamps include:

```text
T0 = Keyword ending
T1 = Local wake detection
T2 = Streaming begins
T3 = First audio packet reaches backend
```

Primary latency:

```text
T3 − T0
```

Final measurements should include:

* Mean
* Median
* P95

## Security and Privacy

The backend should follow the project's privacy-first architecture.

Only audio required after wake detection should be transmitted.

Any stored audio, logs or user data should be minimized and handled according to the final deployment requirements.

## Technology

The backend is planned around lightweight open-source technologies.

Potential components include:

* Python
* HTTP / WebSocket communication
* Open-source or approved ASR
* JSON-based communication
* Performance logging

The exact ASR implementation will be added after the edge-to-server communication protocol is finalized.

## Current Status

🟡 Backend implementation pending.

The current repository contains the architecture documentation. Actual server code will be added after the ESP32 wake-detection and audio-handoff pipeline is implemented.
