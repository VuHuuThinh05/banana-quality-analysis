import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "banana_quality_dataset.csv"
)
CSV_DIR = os.path.join(BASE_DIR, "..", "output", "csv")
PNG_DIR = os.path.join(BASE_DIR, "..", "output", "png")
os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)
df = pd.read_csv(DATA_PATH)
numeric_cols = [
    "sugar_content_brix",
    "quality_score",
    "firmness_kgf",
    "weight_g",
    "length_cm",
    "ripeness_index"
]

# =========================
# 4.1 Ma trận tương quan
# =========================
corr_matrix = df[numeric_cols].corr() 

print("\n=== MA TRẬN TƯƠNG QUAN ===")
print(corr_matrix)

# Lưu ma trận tương quan (CSV)
corr_matrix.to_csv(
    os.path.join(CSV_DIR, "ma_tran_tuong_quan.csv")
)

# =========================
# 4.2 Heatmap tương quan
# =========================
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Heatmap ma trận tương quan")
plt.tight_layout()
plt.savefig(
    os.path.join(PNG_DIR, "heatmap_tuong_quan.png")
)
plt.show()

# =========================
# 4.3 Phân tích riêng Sugar – Quality
# =========================
r = df["sugar_content_brix"].corr(df["quality_score"])
print(
    f"\nHệ số tương quan Pearson giữa độ ngọt và chất lượng: r = {r:.3f}"
)
# =========================
# 4.4 Phân tích Ripeness – Quality
# =========================
r_ripeness = df["ripeness_index"].corr(df["quality_score"])

print(
    f"Hệ số tương quan Pearson giữa độ chín và chất lượng: r = {r_ripeness:.3f}"
)