# from PIL import Image
# import os

# input_dir = 'data/hotcrush/images'
# output_dir = 'data/hotcrush/resized_images'
# os.makedirs(output_dir, exist_ok=True)

# target_size = (800, 600)

# if hasattr(Image, 'Resampling'):
#     resample_mode = Image.Resampling.LANCZOS
# else:
#     resample_mode = Image.ANTIALIAS

# for filename in os.listdir(input_dir):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#         img = Image.open(os.path.join(input_dir, filename))
#         img_resized = img.resize(target_size, resample_mode)
#         img_resized.save(os.path.join(output_dir, filename))
#         print(f'Resized {filename} to {target_size}')


# import json
# import random
# import os

# input_path = './data/hotcrush/transforms.json'
# output_dir = './data/hotcrush'
# train_ratio = 0.8  # 80%训练，20%测试

# with open(input_path, 'r') as f:
#     data = json.load(f)

# frames = data['frames']
# random.shuffle(frames)

# n_train = int(len(frames) * train_ratio)
# train_frames = frames[:n_train]
# test_frames = frames[n_train:]

# data_train = data.copy()
# data_train['frames'] = train_frames

# data_test = data.copy()
# data_test['frames'] = test_frames

# with open(os.path.join(output_dir, 'transforms_train.json'), 'w') as f:
#     json.dump(data_train, f, indent=4)

# with open(os.path.join(output_dir, 'transforms_test.json'), 'w') as f:
#     json.dump(data_test, f, indent=4)

# print(f"生成完成！训练集：{len(train_frames)} 张，测试集：{len(test_frames)} 张。")



import json
import os

def fix_transforms(path):
    with open(path, 'r') as f:
        meta = json.load(f)

    for frame in meta['frames']:
        file_path = frame['file_path']
        file_path = os.path.basename(file_path)      # 只保留文件名
        file_path = os.path.splitext(file_path)[0]   # 去除扩展名
        frame['file_path'] = f"images/{file_path}"   # 添加前缀但不加后缀

    with open(path, 'w') as f:
        json.dump(meta, f, indent=4)
    print(f"✔ 修复完成：{path}")

fix_transforms('data/hotcrush/transforms_train.json')
fix_transforms('data/hotcrush/transforms_test.json')  # 如果存在
