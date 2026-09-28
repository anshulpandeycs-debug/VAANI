# VAANI Benchmarks

This folder contains the performance measurements and evaluation results for the VAANI edge voice activation system.

## Purpose

The benchmark results will verify whether the implemented system meets the engineering requirements of the SIH26172 problem statement.

All final performance values should come from actual testing.

---

## 1. Edge Resource Usage

The ESP32 implementation will be evaluated for:

| Metric         |      Target | Measured |
| -------------- | ----------: | -------: |
| RAM usage      |    < 256 KB |      TBD |
| Idle CPU usage |       < 10% |      TBD |
| Model size     | Lightweight |      TBD |
| Inference time | Low latency |      TBD |

`TBD` means the measurement has not yet been performed.

---

## 2. Keyword Detection

The keyword spotting model will be evaluated using:

| Metric                   | Result |
| ------------------------ | -----: |
| True Positive Rate       |    TBD |
| False Positive Rate      |    TBD |
| False Activations / Hour |    TBD |
| Detection Latency        |    TBD |

Testing should include different speakers, environments and background-noise conditions.

---

## 3. Wake-to-ASR Latency

The complete handoff pipeline will be measured using timestamps.

```text
T0
Keyword ends
   ↓
T1
Local wake detected
   ↓
T2
Audio streaming begins
   ↓
T3
First packet reaches ASR backend
```

### Primary Metric

```text
Wake-to-ASR Latency = T3 − T0
```

The final benchmark should report:

* Mean latency
* Median latency
* P95 latency

---

## 4. Network Usage

The project will measure the amount of audio/data transmitted after wake detection.

Important measurements include:

* Bytes transmitted per activation
* Audio duration transmitted
* Network setup time
* Total communication time

The objective is to avoid continuous transmission of microphone audio while the system is waiting for the wake keyword.

---

## 5. Test Conditions

Testing should include multiple environments.

### Quiet Environment

Low background noise and close microphone distance.

### Normal Environment

Typical room or indoor background noise.

### Noisy Environment

Environmental noise such as:

* Fans
* Traffic
* Conversations
* Keyboard sounds
* Other background activity

### Speaker Variation

Testing should include speakers that were not used during model training where possible.

---

## 6. Benchmark Recording Format

Final measurements may be stored in CSV format.

Example structure:

```text
test_id,environment,speaker,ram_kb,cpu_percent,inference_ms,latency_ms,result
```

Example:

```text
001,quiet,S01,TBD,TBD,TBD,TBD,TBD
```

Actual values will be added after hardware testing.

---

## 7. Reproducibility

Each benchmark should record:

* Hardware used
* Firmware version
* Model version
* Model quantization
* Dataset/model version
* Test environment
* Number of test samples
* Measurement method
* Date of test

This allows the results to be reproduced and compared across iterations.

---

## Current Status

🟡 Benchmarking pending physical hardware implementation.

No final performance numbers are claimed until the VAANI system has been measured on the target edge hardware.
