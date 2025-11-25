# Bottle Caps Color Detection – Take Home Test - Muhammad Dajuma Fenori

This project implemented a lightweight ML pipeline for detecting bottle cap colors using a YOLO model.  
The focus of this submission is on:  
- clean project structure  
- reproducible environment via Docker  
- command-line inference workflow  
- configuration-based pipeline  
- experiment tracking using wandb.ai

## Features
- YOLO inference pipeline with configurable settings  
- Python CLI program `bsort` for model inference  
- Dockerized environment (Python 3.9 + OpenCV + Ultralytics)  
- wandb.ai for model tracking    
- Fully reproducible builds  

⚠ (Limitations)
– Model training performed only to baseline level (no hyperparameter tuning)  
– Docker image is inference-only (training kept outside container)  

## Installation Guide

1. Build Docker

```
docker build -t bsort .
```

2. Run Inference
```
docker run --rm ^ -v path\to\test_image:/app/images ^ -v path\to\models:/app/models ^ bsort infer --config settings.yaml --image path\to\test\images.jpg
```

3. CLI 
```
bsort infer --config settings.yaml --image <path_to_image>
```

## Model Training Summary

I trained several YOLO variants on the provided dataset (YOLOv8 and YOLO11).  
Due to the extremely small dataset (12 images total), model performance is limited and expected to generalize poorly. Training was performed locally using YOLO 8.3.231, and experiment tracking was logged to wandb.ai. No hyperparameter tuning was performed due to time constraints. I prioritized proper docker building and model inference using CLI over model tuning. I chose YOLO11s as main model in projects because of its better training performances over YOLO11n and YOLOv8.

## wandb model tracking:  
https://wandb.ai/dajumaf207-dajumaf/bottlecaps-color-detection

## Limitations & Technical Challenges

– Lacks of model literature and experiment due to time constraint 
– CLI + Docker integration required restructuring the project package  
– Model training and hyperparameter tuning were limited  
– Training was performed locally in Jupyter Notebook, Docker is only for inference.  
- wandb didnt track training metrics