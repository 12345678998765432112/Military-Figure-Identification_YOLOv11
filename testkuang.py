import os

import cv2

from ultralytics import YOLO

# ✅ 类别名称必须写在函数外，或者全局变量
names = ["enemy", "friendly", "hostage"]

# 加载模型
model = YOLO("runsG3/yolov11_custom/weights/best.pt")

# 图片 & 标签路径
image_dir = "D:/computer/ultralytics/Data_G/test/images"
label_dir = "D:/computer/ultralytics/Data_G/test/labels"

# 保存路径
save_dir = "D:/computer/ultralytics/visual_compare"
os.makedirs(save_dir, exist_ok=True)

# 遍历所有图片
for img_file in os.listdir(image_dir):
    if not img_file.endswith((".jpg", ".png", ".jpeg")):
        continue

    img_path = os.path.join(image_dir, img_file)
    label_path = os.path.join(label_dir, os.path.splitext(img_file)[0] + ".txt")
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # ✅ 显示 GT（绿色）
    if os.path.exists(label_path):
        with open(label_path) as f:
            for line in f:
                cls_id, x, y, bw, bh = map(float, line.strip().split())
                x1 = int((x - bw / 2) * w)
                y1 = int((y - bh / 2) * h)
                x2 = int((x + bw / 2) * w)
                y2 = int((y + bh / 2) * h)
                label = names[int(cls_id)]
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f"GT: {label}", (x1, y1 - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # ✅ 显示 Pred（红色）
    results = model.predict(img_path, conf=0.25, verbose=False)[0]
    for box in results.boxes:
        cls = int(box.cls.item())
        conf = box.conf.item()
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = names[cls]
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(img, f"Pred: {label} ({conf:.2f})", (x1, y2 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # 保存结果图
    out_path = os.path.join(save_dir, img_file)
    cv2.imwrite(out_path, img)

print(f"✅ 可视化完成！图片保存到：{save_dir}")
