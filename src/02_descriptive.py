import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "banana_quality_dataset.csv"
)
df = pd.read_csv(DATA_PATH)
numeric_cols = [
    "sugar_content_brix",
    "quality_score",
    "firmness_kgf",
    "weight_g",
    "length_cm",
    "ripeness_index"
]
df_numeric = df[numeric_cols]
desc = df_numeric.describe()
print("\n=== THỐNG KÊ MÔ TẢ ===")
print(desc)
CSV_DIR = os.path.join(BASE_DIR, "..", "output", "csv")
os.makedirs(CSV_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(
    CSV_DIR,
    "thong_ke_mo_ta.csv"
)
desc.to_csv(OUTPUT_PATH)
print(f"\nĐã lưu thống kê mô tả tại: {OUTPUT_PATH}")
