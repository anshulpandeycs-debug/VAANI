# VAANI ESP32 Firmware

This folder contains the firmware for the VAANI edge device.

## Planned Responsibilities

The ESP32 firmware will handle:

* I2S microphone initialization
* Continuous audio capture
* Audio buffering
* Feature extraction
* TinyML keyword spotting
* Wake-word decision logic
* Wi-Fi activation after wake detection
* Audio handoff to the remote ASR service
* Local device control
* Status indication

## Planned Hardware

* ESP32 development board
* I2S MEMS microphone
* Status LED
* Push button
* USB connection
* Wi-Fi

## Firmware Flow

```text
I2S Microphone
      ↓
Audio Capture
      ↓
Feature Extraction
      ↓
TinyML KWS
      ↓
Wake Detected?
   ↓       ↓
  NO      YES
   ↓       ↓
Listen    Buffer
Again       ↓
          Wi-Fi
            ↓
        Remote ASR
            ↓
         Response
            ↓
      Local Control
            ↓
      Offline Listening
```

## Status

Firmware implementation is currently under development.

Final RAM, CPU, inference-time and latency measurements will be added after physical ESP32 testing.
