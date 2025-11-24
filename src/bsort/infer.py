"""
Inference logic for YOLO bottle cap detection
"""
from ultralytics import YOLO
from typing import Dict


def infer_image(cfg: Dict, image_path: str):
    """Run inference on a single image and save annotated results."""
    model = YOLO(cfg["model_type"])  # load YOLO model

    # Run inference
    results = model.predict(image_path, imgsz=cfg.get("imgsz", 320))
    
    # Print results to console
    print(results)

    # Save annotated image
    results[0].save()
    print(f"Annotated image saved to {results[0].path}")
