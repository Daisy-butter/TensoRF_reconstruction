import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置目录
csv_dir = 'RESULT_FIGURE/csv'
fig_dir = 'RESULT_FIGURE/figures'

# 创建图像输出目录
os.makedirs(fig_dir, exist_ok=True)

# 定义要绘图的指标文件
metrics = {
    'train_mse.csv': {
        'ylabel': 'MSE Loss',
        'title': 'TensoRF Training MSE Loss',
        'output': 'mse_curve.png'
    },
    'train_PSNR.csv': {
        'ylabel': 'PSNR',
        'title': 'TensoRF Training PSNR',
        'output': 'psnr_curve.png'
    },
    'train_reg_tv_density.csv': {
        'ylabel': 'TV Density Loss',
        'title': 'TensoRF TV Regularization (Density)',
        'output': 'tv_density_curve.png'
    },
    'train_reg_tv_app.csv': {
        'ylabel': 'TV Appearance Loss',
        'title': 'TensoRF TV Regularization (Appearance)',
        'output': 'tv_app_curve.png'
    }
}

# 遍历绘制所有图像
for filename, info in metrics.items():
    path = os.path.join(csv_dir, filename)
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        continue

    df = pd.read_csv(path)
    plt.figure(figsize=(8, 5))
    plt.plot(df['Step'], df['Value'], label=info['ylabel'])
    plt.xlabel('Iteration')
    plt.ylabel(info['ylabel'])
    plt.title(info['title'])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    save_path = os.path.join(fig_dir, info['output'])
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"✅ Saved: {save_path}")

print("🎉 All plots completed.")
