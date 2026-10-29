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
PNG_DIR = os.path.join(BASE_DIR, "..", "output", "png")
os.makedirs(PNG_DIR, exist_ok=True)
df = pd.read_csv(DATA_PATH)
# =========================
# 3.1 Phân bố độ ngọt
# =========================
plt.figure(figsize=(6, 4))
sns.histplot(df["sugar_content_brix"], kde=True)
plt.title("Phân bố độ ngọt (Sugar Content - Brix)")
plt.xlabel("Độ ngọt (Brix)")
plt.ylabel("Tần suất")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "hist_sugar_content.png"))
plt.show()
# =========================
# 3.2 Phân bố quality score
# =========================
plt.figure(figsize=(6, 4))
sns.histplot(df["quality_score"], kde=True)
plt.title("Phân bố điểm chất lượng chuối")
plt.xlabel("Quality Score")
plt.ylabel("Tần suất")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "hist_quality_score.png"))
plt.show()
# =========================
# 3.3 Scatter: Sugar vs Quality
# =========================
plt.figure(figsize=(6, 4))
sns.scatterplot(
    x="sugar_content_brix",
    y="quality_score",
    data=df
)
plt.title("Mối quan hệ giữa độ ngọt và chất lượng")
plt.xlabel("Độ ngọt (Brix)")
plt.ylabel("Quality Score")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "scatter_sugar_quality.png"))
plt.show()
# =========================
# 3.4 Scatter: Firmness vs Quality
# =========================
plt.figure(figsize=(6, 4))
sns.scatterplot(
    x="firmness_kgf",
    y="quality_score",
    data=df
)
plt.title("Firmness vs Quality")
plt.xlabel("Firmness (kgf)")
plt.ylabel("Quality Score")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "scatter_firmness_quality.png"))
plt.show()
# =========================
# 3.5 DASHBOARD: Weight - Length - Firmness
# ========================= 
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# Histogram Weight
sns.histplot(df["weight_g"], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Phân bố trọng lượng chuối")
axes[0, 0].set_xlabel("Weight (g)")
# Histogram Length
sns.histplot(df["length_cm"], kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Phân bố chiều dài chuối")
axes[0, 1].set_xlabel("Length (cm)")
# Histogram Firmness
sns.histplot(df["firmness_kgf"], kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Phân bố độ cứng chuối")
axes[1, 0].set_xlabel("Firmness (kgf)")
# Scatter Length vs Weight
sns.scatterplot(
    x="length_cm",
    y="weight_g",
    data=df,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Length vs Weight")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "dashboard_physical_features.png"))
plt.show()
# =========================
# 3.6 DASHBOARD RIPENESS INDEX
# =========================
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# Histogram Ripeness
sns.histplot(df["ripeness_index"], kde=True, ax=axes[0])
axes[0].set_title("Phân bố độ chín của chuối")
axes[0].set_xlabel("Ripeness Index")
axes[0].set_ylabel("Tần suất")
# Ripeness vs Quality
sns.scatterplot(
    x="ripeness_index",
    y="quality_score",
    data=df,
    ax=axes[1]
)
axes[1].set_title("Ripeness vs Quality Score")
axes[1].set_xlabel("Ripeness Index")
axes[1].set_ylabel("Quality Score")
plt.tight_layout()
plt.savefig(os.path.join(PNG_DIR, "dashboard_ripeness.png"))
plt.show()
# =========================
# 3.7 DASHBOARD: PHYSICAL FEATURES vs QUALITY
# =========================
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# Length vs Quality
sns.scatterplot(
    x="length_cm",
    y="quality_score",
    data=df,
    ax=axes[0]
)
axes[0].set_title("Length vs Quality Score")
axes[0].set_xlabel("Length (cm)")
axes[0].set_ylabel("Quality Score")
# Weight vs Quality
sns.scatterplot(
    x="weight_g",
    y="quality_score",
    data=df,
    ax=axes[1]
)
axes[1].set_title("Weight vs Quality Score")
axes[1].set_xlabel("Weight (g)")
axes[1].set_ylabel("Quality Score")
plt.tight_layout()
plt.savefig(
    os.path.join(PNG_DIR, "dashboard_physical_quality.png")
)
plt.show()