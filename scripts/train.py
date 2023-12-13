from ultralytics import YOLO
from config import *


def train():
    # Load a new model
    model = YOLO(model_type)
    # Train the model
    model.train(
        data="dataset.yaml",
        epochs=epochs,
        imgsz=imgsz,
        seed=seed,
        pretrained=True,
        optimizer="auto"
    )


if __name__ == "__main__":
    train()
