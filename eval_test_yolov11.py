from ultralytics import YOLO


def main():
    # 加载训练好的 best 权重
    model = YOLO("runsG3/yolov11_custom/weights/best.pt")

    # 使用 test 集进行正式验证评估
    results = model.val(
        data="D:/computer/ultralytics/Data_G/data.yaml",  # 确保 data.yaml 里写了 test 路径
        split="test",  # 显式使用 test 数据
        save_json=True,  # 可选：保存 COCO 格式结果
        save_hybrid=True,  # 可选：保存混合推理结果
    )

    # 打印主要指标
    print("✅ 测试集评估完成：")
    print(f"mAP50: {results.box.map50:.3f}")
    print(f"mAP50-95: {results.box.map:.3f}")
    print(f"Precision: {results.box.mp:.3f}")
    print(f"Recall: {results.box.mr:.3f}")


if __name__ == "__main__":
    main()
