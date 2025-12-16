import os

# 设置原始文件夹路径
folder = r"F:\new_picture"

# 英文前缀
prefix = "soldier_"

# 获取文件夹中的所有文件
files = os.listdir(folder)

# 遍历所有文件
count = 1
for file in files:
    # 检查是否为图片文件
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        # 构造新文件名
        ext = os.path.splitext(file)[1]
        new_name = f"{prefix}{count}{ext}"
        # 完整路径
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, new_name)
        # 重命名
        os.rename(old_path, new_path)
        print(f"Renamed: {file} → {new_name}")
        count += 1
