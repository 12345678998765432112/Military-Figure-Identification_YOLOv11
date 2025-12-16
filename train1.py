from ultralytics import YOLO

def main():  # ✅ 你缺了这个函数定义
    # ✅ 加载预训练模型（指定绝对路径）
    model = YOLO("yolo11s.pt")

    # ✅ 开始训练
    model.train(
        data="Data_G/data.yaml",   # 相对路径也可以
        epochs=250,
        imgsz=640,
        batch=8,
        workers=4,               # 读取数据的线程数
        patience=50,             # 若连续30次评估指标不提升，自动提前停止
        optimizer="SGD",         # 或者试试 AdamW，默认是 auto
        close_mosaic=10,         # 最后10轮关闭 mosaic 更利于模型稳定收敛
        degrees=5.0,             # 图像旋转角度范围（默认10）
        scale=0.5,               # 图像缩放（默认0.5，建议保留）
        hsv_h=0.015,             # 色调变换
        hsv_s=0.7,               # 饱和度变换
        hsv_v=0.4,               # 亮度变换
        project="runsG5",
        name="yolov11_custom",
        exist_ok=True
    )

if __name__ == "__main__":
    # ✅ 防止 Windows 多进程出错
    import multiprocessing
    multiprocessing.freeze_support()
    main()
