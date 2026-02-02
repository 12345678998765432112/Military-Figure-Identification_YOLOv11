from ultralytics import YOLO


def main():
    # 加载你刚刚训练好的 best.pt 权重
    model = YOLO("runsG5/yolov11_custom/weights/best.pt")

    # 替换为你要测试的图片路径，可以是单张，也可以是文件夹
    source = "D:/computer/ultralytics/Data_G/test/images"  # 也可以换成 test.jpg
    # source = "D:/computer/robocom_data/images1"

    # 执行预测
    model.predict(
        source=source,
        imgsz=640,
        conf=0.25,  # 置信度阈值（默认0.25）
        save=True,  # 保存结果图像
        save_txt=False,  # 是否保存为 txt 坐标
        save_crop=False,  # 是否裁剪出框中物体
        project="runsG5",
        name="predict_results1",  # 输出目录 runs/predict_results/
        exist_ok=True,  # 如果文件夹已存在则覆盖
        show=False,  # 是否实时显示（调试用）
    )


if __name__ == "__main__":
    import multiprocessing

    multiprocessing.freeze_support()
    main()
