import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# =========================
# PHẦN 6: HỒI QUY TUYẾN TÍNH ĐA BIẾN
# =========================

# Lấy đường dẫn thư mục src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn dữ liệu
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "banana_quality_dataset.csv"
)

# =========================
# THƯ MỤC OUTPUT
# =========================
CSV_DIR = os.path.join(BASE_DIR, "..", "output", "csv")
PNG_DIR = os.path.join(BASE_DIR, "..", "output", "png")

os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)

# Đọc dữ liệu
df = pd.read_csv(DATA_PATH)

# =========================
# 6.1 Chọn biến độc lập & phụ thuộc
# =========================
features = [
    "sugar_content_brix",
    "firmness_kgf",
    "length_cm",
    "weight_g",
    "ripeness_index"
]

X = df[features]
y = df["quality_score"]

# =========================
# 6.2 Huấn luyện mô hình
# =========================
model = LinearRegression()
model.fit(X, y)

# =========================
# 6.3 Dự đoán
# =========================
y_pred = model.predict(X)

# =========================
# 6.4 Hệ số hồi quy
# =========================
coef_df = pd.DataFrame({
    "Biến": features,
    "Hệ số": model.coef_
})

print("\n=== HỒI QUY TUYẾN TÍNH ĐA BIẾN ===")
print("Intercept:", round(model.intercept_, 3))
print(coef_df)

# =========================
# 6.5 Đánh giá mô hình
# =========================
r2 = r2_score(y, y_pred)
print("Hệ số R² (đa biến):", round(r2, 3))

# Lưu hệ số hồi quy (CSV)
coef_df.to_csv(
    os.path.join(CSV_DIR, "he_so_hoi_quy_da_bien.csv"),
    index=False
)

# =========================
# 6.6 Predicted vs Actual
# =========================
plt.figure(figsize=(7, 7))
plt.scatter(y, y_pred, alpha=0.6)
plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    linestyle="--"
)

plt.xlabel("Giá trị thực tế (Actual)")
plt.ylabel("Giá trị dự đoán (Predicted)")
plt.title("Predicted vs Actual - Hồi quy tuyến tính đa biến")
plt.tight_layout()

plt.savefig(
    os.path.join(PNG_DIR, "predicted_vs_actual_multivariate.png")
)
plt.show()
