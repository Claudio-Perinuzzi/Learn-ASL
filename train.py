from ultralytics import YOLO
from roboflow import Roboflow
from dotenv import load_dotenv
import os
import torch
load_dotenv()
api_key = os.getenv('ROBOFLOW_API_KEY')
rf = Roboflow(api_key)
project = rf.workspace("learnasl").project("ctp-fork-asl-av3mw")
version = project.version(3)
dataset = version.download("yolov11")

def main():
    torch.cuda.empty_cache()
    # load the model
    model = YOLO("yolo11n.pt")

    # training
    train_results = model.train(
        data=f"{dataset.location}/data.yaml",  # path to dataset YAML
        epochs=250,  # number of training epochs
        imgsz=512,  # training image size
        batch=2,
        device='cuda',  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
        workers=2
    )

    print("Model class names:", model.names)  # <- need this to know which numerical value corresponds to what letter


if __name__ == "__main__":
    main()