seed = 42

# Training Configuration
epochs = 100
model_type = 'yolov8s.pt'
imgsz = 640
optimizer = "auto"

# Dataset config
location = "../datasets/piano"
dataset_labels = ["Musical keyboard"]
annotation_format = "darknet"
test_size = 0.1
