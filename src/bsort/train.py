import yaml
from ultralytics import YOLO

def train_model(config_path: str):
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    model = YOLO(cfg["model_checkpoint"])

    model.train(
        data=cfg["dataset_yaml"],
        epochs=cfg["epochs"],
        imgsz=cfg["imgsz"],
        batch=cfg["batch"],
        name=cfg["exp_name"],
        project="runs/train",
    )
