# VAANI Model Training

This folder contains the training and evaluation workflow for the VAANI custom keyword spotting model.

## Objective

Train a lightweight keyword spotting model capable of detecting the VAANI custom wake keyword while remaining suitable for deployment on a resource-constrained edge device.

## Training Pipeline

```text
Dataset
   ↓
Audio Preprocessing
   ↓
Noise / Audio Augmentation
   ↓
MFCC / Log-Mel Features
   ↓
Train / Validation / Test Split
   ↓
Lightweight KWS Model
   ↓
Evaluation
   ↓
INT8 Quantization
   ↓
Edge Deployment
```

## Dataset Categories

The training data should contain:

### Positive

Recordings containing the selected custom wake keyword.

### Negative

Normal speech and non-keyword utterances.

### Background Noise

Environmental audio used to make the model more robust to real-world conditions.

## Data Augmentation

The training pipeline may use:

* Background noise mixing
* Volume variation
* Time shifting
* Small temporal variations
* Different recording environments

## Dataset Splitting

The dataset should be separated into:

```text
Training Set
     ↓
Validation Set
     ↓
Test Set
```

Speaker and environment separation should be considered to reduce data leakage and provide a more realistic evaluation.

## Model Development

The training process should prioritize:

* Small model size
* Low inference cost
* Low memory requirements
* Fast inference
* Robust keyword detection
* INT8 quantization compatibility

## Evaluation Metrics

The trained model should be evaluated using:

* True Positive Rate
* False Positive Rate
* False Activations per Hour
* Detection latency
* Model size
* Inference time

## Export

The final model is intended to be converted into an MCU-compatible format for deployment on the ESP32.

```text
Trained Model
     ↓
Quantization
     ↓
INT8 Model
     ↓
TensorFlow Lite Micro
     ↓
ESP32
```

## Current Status

🟡 Training pipeline under development.

Actual training scripts, model files and measured results will be added after the dataset and model implementation are finalized.
