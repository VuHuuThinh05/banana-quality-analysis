import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# =========================
# PHẦN 5: HỒI QUY TUYẾN TÍNH ĐƠN
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
# THƯ MỤC OUTPUT (PNG)
# =========================
PNG_DIR = os.path.join(BASE_DIR, "..", "output", "png")
os.makedirs(PNG_DIR, exist_ok=True)

# Đọc dữ liệu
df = pd.read_csv(DATA_PATH)

# =========================
# 5.1 Chọn biến
# =========================
X = df[["sugar_content_brix"]]   # biến độc lập
y = df["quality_score"]          # biến phụ thuộc

# =========================
# 5.2 Huấn luyện mô hình
# =========================
model = LinearRegression()
model.fit(X, y)

# =========================
# 5.3 Dự đoán
# =========================
y_pred = model.predict(X)

# =========================
# 5.4 Kết quả mô hình
# =========================
a = model.coef_[0]
b = model.intercept_
r2 = r2_score(y, y_pred)

print("\n=== HỒI QUY TUYẾN TÍNH ĐƠN ===")
print(f"Phương trình: quality_score = {a:.3f} * sugar_content_brix + {b:.3f}")
print(f"Hệ số R² = {r2:.3f}")

# =========================
# 5.5 Vẽ đồ thị hồi quy
# =========================
plt.figure(figsize=(8, 6))
plt.scatter(X, y, alpha=0.5, label="Dữ liệu thực tế")
plt.plot(X, y_pred, color="red", label="Đường hồi quy")

plt.xlabel("Sugar content (Brix)")
plt.ylabel("Quality score")
plt.title("Hồi quy tuyến tính giữa độ ngọt và chất lượng chuối")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(PNG_DIR, "hoi_quy_sugar_quality.png")
)
plt.show()
# =========================
# 5.6 HỒI QUY: RIPENESS vs QUALITY
# =========================

X2 = df[["ripeness_index"]]
y2 = df["quality_score"]

model2 = LinearRegression()
model2.fit(X2, y2)

y2_pred = model2.predict(X2)

a2 = model2.coef_[0]
b2 = model2.intercept_

r2_2 = r2_score(y2, y2_pred)

print("\n=== HỒI QUY RIPENESS → QUALITY ===")
print(f"Phương trình: quality_score = {a2:.3f} * ripeness_index + {b2:.3f}")
print(f"Hệ số R² = {r2_2:.3f}")

plt.figure(figsize=(8,6))
plt.scatter(X2, y2, alpha=0.5)
plt.plot(X2, y2_pred, color="red")

plt.xlabel("Ripeness Index")
plt.ylabel("Quality Score")
plt.title("Hồi quy tuyến tính giữa độ chín và chất lượng chuối")

plt.tight_layout()

plt.savefig(
    os.path.join(PNG_DIR, "hoi_quy_ripeness_quality.png")
)

plt.show()
