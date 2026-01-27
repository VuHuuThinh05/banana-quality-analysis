import pandas as pd
import os

# =========================
# PHẦN 2: THỐNG KÊ MÔ TẢ
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

# Đọc dữ liệu
df = pd.read_csv(DATA_PATH)

# Chọn các biến số quan trọng
numeric_cols = [
    "sugar_content_brix",
    "quality_score",
    "firmness_kgf",
    "weight_g",
    "length_cm"
]

df_numeric = df[numeric_cols]

# Thống kê mô tả
desc = df_numeric.describe()

print("\n=== THỐNG KÊ MÔ TẢ ===")
print(desc)

# Lưu kết quả ra file(csv)
CSV_DIR = os.path.join(BASE_DIR, "..", "output", "csv")
os.makedirs(CSV_DIR, exist_ok=True)

OUTPUT_PATH = os.path.join(
    CSV_DIR,
    "thong_ke_mo_ta.csv"
)
desc.to_csv(OUTPUT_PATH)
print(f"\nĐã lưu thống kê mô tả tại: {OUTPUT_PATH}")
