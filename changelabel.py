import os

# 设置标签文件夹路径
label_dir = r"D:/computer/robocom2025/GSdata/bingren_photo_labels"  # 你的标签文件夹路径

# 标签类号映射，替换原有的类号
# class_mapping = {'enemy': 0, 'hostage': 1, 'friendly': 2}
class_mapping = {15: 0, 16: 1, 17: 2}

# 遍历标签文件夹中的每个标签文件
for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        label_path = os.path.join(label_dir, label_file)

        # 读取标签文件
        with open(label_path, "r") as f:
            lines = f.readlines()

        # 更新标签文件中的类号
        with open(label_path, "w") as f:
            for line in lines:
                parts = line.strip().split()
                class_id = int(parts[0])

                # 如果类号在映射字典中，进行替换
                if class_id in class_mapping:
                    parts[0] = str(class_mapping[class_id])

                # 写入修改后的行
                f.write(" ".join(parts) + "\n")

print("✅ 标签类号更新完成！")
