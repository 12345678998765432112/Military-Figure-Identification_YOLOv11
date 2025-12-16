import os
import shutil
import random

# 原始路径
img_src = r"D:/computer/robocom2025/full_data/images"
label_src = r"D:/computer/robocom2025/full_data/labels"

# 目标路径
base_out = r"D:/computer/ultralytics/Data_G"
train_img_dst = os.path.join(base_out, "train", "images")
train_label_dst = os.path.join(base_out, "train", "labels")
val_img_dst = os.path.join(base_out, "val", "images")
val_label_dst = os.path.join(base_out, "val", "labels")
test_img_dst = os.path.join(base_out, "test", "images")
test_label_dst = os.path.join(base_out, "test", "labels")

# 创建目标目录
for path in [train_img_dst, train_label_dst, val_img_dst, val_label_dst, test_img_dst, test_label_dst]:
    os.makedirs(path, exist_ok=True)

# 获取所有图片文件（支持 .jpg .png .jpeg 大小写）
img_exts = [".jpg", ".png", ".jpeg"]
all_imgs = [f for f in os.listdir(img_src) if os.path.splitext(f)[1].lower() in img_exts]

# 打乱顺序
random.shuffle(all_imgs)

# 按比例划分数据集（8:1:1）
total = len(all_imgs)
train_end = int(0.7 * total)
val_end = int(0.85 * total)

train_imgs = all_imgs[:train_end]
val_imgs = all_imgs[train_end:val_end]
test_imgs = all_imgs[val_end:]

def copy_files(img_list, img_dst, label_dst):
    for img_name in img_list:
        img_path = os.path.join(img_src, img_name)
        label_name = os.path.splitext(img_name)[0] + ".txt"
        label_path = os.path.join(label_src, label_name)

        # 复制图片
        shutil.copy(img_path, os.path.join(img_dst, img_name))

        # 复制标签（如果存在）
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(label_dst, label_name))
        else:
            print(f"⚠️ Warning: Label not found for image {img_name}")

# 执行复制
copy_files(train_imgs, train_img_dst, train_label_dst)
copy_files(val_imgs, val_img_dst, val_label_dst)
copy_files(test_imgs, test_img_dst, test_label_dst)

# 输出信息
print("✅ 数据划分完成。")
print(f"训练集数量: {len(train_imgs)} 张")
print(f"验证集数量: {len(val_imgs)} 张")
print(f"测试集数量: {len(test_imgs)} 张")
