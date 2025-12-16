import os

# 你的图片路径（修改为你的真实路径）
train_img_dir = r"D:/computer/ultralytics/Data_G/train/images"
val_img_dir = r"D:/computer/ultralytics/Data_G/val/images"

# 读取文件名（不包含扩展名）
train_imgs = {os.path.splitext(f)[0] for f in os.listdir(train_img_dir) if f.endswith((".jpg", ".png", ".jpeg"))}
val_imgs = {os.path.splitext(f)[0] for f in os.listdir(val_img_dir) if f.endswith((".jpg", ".png", ".jpeg"))}

# 查找重合项
overlap = train_imgs & val_imgs

# 输出结果
if overlap:
    print("❌ 以下图片在训练集和验证集中重复出现：")
    for name in sorted(overlap):
        print(f"- {name}")
    print(f"\n共重复 {len(overlap)} 张图像")
else:
    print("✅ 检查通过：训练集和验证集没有重叠！")
