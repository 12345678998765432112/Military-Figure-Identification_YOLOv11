from ultralytics import YOLO

def main():
    model = YOLO("yolo11s.pt")  # 载入旧模型权重

    model.train(
        data="Data_G/data.yaml",
        epochs=250,              # 微调不需要太久
        imgsz=640,
        batch=8,
        lr0=0.001, lrf=0.05,    # 小学习率防止破坏原特征
        workers=4,
        patience=20,
        optimizer="SGD",
        cos_lr=True,
        freeze=10,              # 冻结前10层（保留backbone特征）
        mosaic=0.3,
        mixup=0.0,
        close_mosaic=15,
        degrees=3.0,
        scale=0.5,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        save_period=10,
        project="runsG4",
        name="yolov11_custom_ft",
        exist_ok=True
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()