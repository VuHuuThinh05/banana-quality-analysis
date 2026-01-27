import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PHẦN 3: TRỰC QUAN HÓA DỮ LIỆU
# =========================

# Lấy đường dẫn thư mục src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn file dữ liệu
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "banana_quality_dataset.csv"
)

# =========================
# THƯ MỤC OUTPUT PNG
# =========================
PNG_DIR = os.path.join(BASE_DIR, "..", "output", "png")
os.makedirs(PNG_DIR, exist_ok=True)

# Đọc dữ liệu
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
