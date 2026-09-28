# VAANI TinyML Model

This folder contains the keyword spotting model and related model-development files for VAANI.

## Model Objective

The model is designed to detect a **custom VAANI wake keyword locally on an edge device**.

The model must be lightweight enough for deployment on a low-power MCU while maintaining reliable wake-word detection.

## Model Pipeline

```text
Audio
  ↓
Preprocessing
  ↓
MFCC / Log-Mel Features
  ↓
Lightweight Neural Network
  ↓
INT8 Quantization
  ↓
TinyML Model
  ↓
ESP32 Inference
```

## Model Requirements

The final model should be evaluated against the SIH engineering requirements:

| Requirement  |   Target |
| ------------ | -------: |
| Edge RAM     | < 256 KB |
| Idle CPU     |    < 10% |
| Quantization |     INT8 |
| Keyword      |   Custom |
| Deployment   | Edge MCU |

These are project targets. They are not claimed as measured results until physical testing is completed.

## Dataset

The training dataset should contain:

### Positive Samples

Audio containing the selected VAANI wake keyword.

### Negative Samples

Normal speech and words that should not activate the system.

### Background Noise

Environmental sounds such as:

* Fan noise
* Traffic
* Keyboard sounds
* Room noise
* Conversations
* Other everyday sounds

## Training Considerations

The model-development process should include:

* Speaker diversity
* Environmental diversity
* Noise augmentation
* Volume variation
* Time shifting
* Train/validation/test separation
* Unseen-speaker evaluation
* Unseen-environment evaluation

Data leakage should be avoided when creating the dataset splits.

## Evaluation

The final model should be evaluated using:

* True Positive Rate
* False Positive Rate
* False Activations per Hour
* Detection latency
* Model size
* RAM usage
* CPU usage
* Inference time

## Deployment

After training and evaluation, the model is intended to be converted into an MCU-compatible format such as an INT8 TensorFlow Lite Micro model.

The final deployment process will connect:

```text
TinyML Model
     ↓
ESP32 Firmware
     ↓
I2S Microphone
     ↓
Real-Time Keyword Detection
```

## Current Status

🟡 Model development pending

The final model file and benchmark results will be added after training and physical ESP32 validation.
