from ultralytics import YOLO
import os

def main():
    model = YOLO("runs1/yolov11_custom/weights/best.pt")

    # ✅ 改成你自己的图片目录
    source = "D:/computer/robocom2025/GSdata/bingren_photo"

    results = model.predict(
        source=source,
        imgsz=640,
        conf=0.25,
        save=True,
        save_txt=True,       # ✅ 生成 txt 标签文件（重点）
        save_crop=False,
        project="runs1",
        name="bingren_pred", # ✅ 输出文件夹
        exist_ok=True,
        show=False
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
