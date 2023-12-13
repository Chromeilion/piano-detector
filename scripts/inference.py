from ultralytics import YOLO
from pathlib import Path
from PIL import Image
import argparse as ap


def inference():
    parser = ap.ArgumentParser()
    parser.add_argument('-m', '--model-location')
    parser.add_argument('-d', '--dataset-root')
    args = parser.parse_args()

    dataset = Path(args.dataset_root)
    model = YOLO(args.model_location)

    output_dir = Path("./preds")
    output_dir.mkdir(parents=True, exist_ok=True)

    all_vids = dataset.rglob("*.mp4")
    for video in all_vids:
        pred = model.predict(source=str(video), stream=True)
        r = next(pred)
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])
        im.save(f"./preds/{video.stem}.jpg")


if __name__ == '__main__':
    inference()
