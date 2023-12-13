from openimages.download import download_dataset
from sklearn.model_selection import train_test_split
import config
import shutil
from pathlib import Path
import tempfile


def download_data():
    with tempfile.TemporaryDirectory(dir=".") as tempdir:
        tempdir = Path(tempdir)
        data = download_dataset(
            dest_dir=str(tempdir),
            class_labels=config.dataset_labels,
            annotation_format=config.annotation_format
        )
        images_path = Path(data[config.dataset_labels[0].lower()]["images_dir"])
        labels_path = Path(data[config.dataset_labels[0].lower()]["annotations_dir"])
        images = sorted(images_path.glob("*.jpg"))
        labels = sorted(labels_path.glob("*.txt"))
        dataset = list(zip(images, labels))
        train, val = train_test_split(
            dataset,
            test_size=config.test_size,
            random_state=config.seed
        )

        out_location = Path(config.location)
        images_dir = out_location/"images"
        labels_dir = out_location/"labels"
        images_train_dir = images_dir/"train"
        images_val_dir = images_dir/"val"
        labels_train_dir = labels_dir/"train"
        labels_val_dir = labels_dir/"val"
        images_train_dir.mkdir(parents=True, exist_ok=True)
        images_val_dir.mkdir(parents=True, exist_ok=True)
        labels_train_dir.mkdir(parents=True, exist_ok=True)
        labels_val_dir.mkdir(parents=True, exist_ok=True)

        for im, lab in train:
            im = Path(im)
            lab = Path(lab)
            shutil.move(im, images_train_dir/im.name)
            shutil.move(lab, labels_train_dir/lab.name)
        for im, lab in val:
            im = Path(im)
            lab = Path(lab)
            shutil.move(im, images_val_dir/im.name)
            shutil.move(lab, labels_val_dir/lab.name)


if __name__ == "__main__":
    download_data()
