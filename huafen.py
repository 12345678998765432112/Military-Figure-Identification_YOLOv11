import os
import shutil
import random

# 路径配置
new_images_dir = r"F:/new_picture"
new_labels_dir = r"F:/labels"

train_images_dir = r"D:/computer/ultralytics/Data_G/train/images"
train_labels_dir = r"D:/computer/ultralytics/Data_G/train/labels"
val_images_dir = r"D:/computer/ultralytics/Data_G/val/images"
val_labels_dir = r"D:/computer/ultralytics/Data_G/val/labels"

# 获取所有图片文件
images = [f for f in os.listdir(new_images_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
images.sort()

# 随机挑 2 张做 val
val_samples = set(random.sample(images, 2))

# 移动文件函数
def move_files(file_list, src_img_dir, src_lbl_dir, dst_img_dir, dst_lbl_dir):
    for img_file in file_list:
        label_file = os.path.splitext(img_file)[0] + '.txt'
        shutil.move(os.path.join(src_img_dir, img_file), os.path.join(dst_img_dir, img_file))
        shutil.move(os.path.join(src_lbl_dir, label_file), os.path.join(dst_lbl_dir, label_file))
        print(f"Moved: {img_file}, {label_file}")

# 移动到 val
move_files(val_samples, new_images_dir, new_labels_dir, val_images_dir, val_labels_dir)

# 剩下的进 train
train_samples = set(images) - val_samples
move_files(train_samples, new_images_dir, new_labels_dir, train_images_dir, train_labels_dir)

print("移动完成！请记得删除 Data_G 下的 labels.cache 文件。")
