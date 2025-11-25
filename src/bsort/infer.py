from ultralytics import YOLO
from typing import Dict


def infer_image(cfg: Dict, image_path: str):
    model = YOLO(cfg["model_type"]) 

    # Run inference
    results = model.predict(image_path, imgsz=cfg.get("imgsz", 320))
    
    # Print results to console
    print(results)

    # Save annotated image
    results[0].save()
    print(f"Annotated image saved to {results[0].path}")
