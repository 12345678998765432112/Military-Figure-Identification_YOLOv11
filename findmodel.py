from ultralytics import YOLO

model = YOLO("yolo11n.pt")
print(model.model)  # 看看它的结构是不是标准 YOLOv8 的
