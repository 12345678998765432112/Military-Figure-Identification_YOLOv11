import os
import shutil

# 设置你的根目录路径
root_dir = r"D:\computer\ultralytics\runs1\bingren_pred"
image_dir = os.path.join(root_dir, "images")

# 创建 images 目录（如果没有）
os.makedirs(image_dir, exist_ok=True)

# 遍历根目录中的文件
for file in os.listdir(root_dir):
    if file.lower().endswith(".jpg"):
        src_path = os.path.join(root_dir, file)
        dst_path = os.path.join(image_dir, file)
        print(f"Moving: {file}")
        shutil.move(src_path, dst_path)

print("✅ 所有图片已移动到 images/ 文件夹。")
