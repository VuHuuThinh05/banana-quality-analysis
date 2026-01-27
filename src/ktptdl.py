import pandas as pd
import os

# Lấy đường dẫn thư mục src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Ghép đường dẫn tới file CSV
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "banana_quality_dataset.csv")

# Đọc dữ liệu
df = pd.read_csv(DATA_PATH)

print("So dong, so cot:", df.shape)
print("\n5 dong dau:")
print(df.head())

print("\nThong tin dataset:")
print(df.info())
# =========================
# BƯỚC 1: THỐNG KÊ MÔ TẢ
# =========================

# Chọn các biến số quan trọng
numeric_cols = [
    "sugar_content_brix",
    "quality_score",
    "firmness_kgf",
    "weight_g",
    "length_cm"
]

df_numeric = df[numeric_cols]

print("\n=== Thống kê mô tả các biến số ===")
print(df_numeric.describe())

# Lưu kết quả thống kê ra file CSV
df_numeric.describe().to_csv("output/thong_ke_mo_ta.csv")
# BƯỚC 2: Trực quan hóa:
import matplotlib.pyplot as plt
import seaborn as sns
# =========================
# BƯỚC 2.1: PHÂN BỐ DỮ LIỆU
# =========================

plt.figure(figsize=(6,4))
sns.histplot(df["sugar_content_brix"], kde=True)
plt.title("Phân bố độ ngọt (Sugar Content - Brix)")
plt.xlabel("Độ ngọt (Brix)")
plt.ylabel("Tần suất")
plt.tight_layout()
plt.savefig("output/hist_sugar_content.png")
plt.show()
#
# 2.2: phân bố quality score
#
plt.figure(figsize=(6,4))
sns.histplot(df["quality_score"], kde=True)
plt.title("Phân bố điểm chất lượng chuối")
plt.xlabel("Quality Score")
plt.ylabel("Tần suất")
plt.tight_layout()
plt.savefig("output/hist_quality_score.png")
plt.show()
#
#2.3: Vẽ biểu đồ quan hệ (Scatter plot)
#
plt.figure(figsize=(6,4))
sns.scatterplot(
    x="sugar_content_brix",
    y="quality_score",
    data=df
)
plt.title("Mối quan hệ giữa độ ngọt và chất lượng chuối")
plt.xlabel("Độ ngọt (Brix)")
plt.ylabel("Quality Score")
plt.tight_layout()
plt.savefig("output/scatter_sugar_quality.png")
plt.show()
#Frimness - Quality
plt.figure(figsize=(6,4))
sns.scatterplot(
    x="firmness_kgf",
    y="quality_score",
    data=df
)
plt.title("Firmness vs Quality")
plt.xlabel("Firmness (kgf)")
plt.ylabel("Quality Score")
plt.tight_layout()
plt.savefig("output/scatter_firmness_quality.png")
plt.show()
# =========================
# BƯỚC 3.1: MA TRẬN TƯƠNG QUAN
# =========================

corr_matrix = df[numeric_cols].corr()

print("\n=== Ma trận tương quan ===")
print(corr_matrix)

# Lưu ra file CSV
corr_matrix.to_csv("output/ma_tran_tuong_quan.csv")
#
#3.2: Heatmap tương quan
#
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Heatmap ma trận tương quan")
plt.tight_layout()
plt.savefig("output/heatmap_tuong_quan.png")
plt.show()
#Phân tích riêng Sweetness - Quality
r = df["sugar_content_brix"].corr(df["quality_score"])

print(f"\nHệ số tương quan Pearson giữa độ ngọt và chất lượng: r = {r:.3f}")

# ==============================
# BƯỚC 4: HỒI QUY TUYẾN TÍNH
# ==============================

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Chọn biến X và Y
X = df[["sugar_content_brix"]]   # biến độc lập (phải là DataFrame)
y = df["quality_score"]          # biến phụ thuộc
#
#4.2: Xây dựng mô hình hồi quy 
#
# Khởi tạo mô hình
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X, y)

# Dự đoán
y_pred = model.predict(X)
#
#4.3: Kết quả mô hình hòi quy
#
# Hệ số hồi quy
a = model.coef_[0]      # hệ số góc
b = model.intercept_   # hệ số chặn

# R^2
r2 = r2_score(y, y_pred)

print("\n=== KẾT QUẢ HỒI QUY TUYẾN TÍNH ===")
print(f"Phương trình: quality_score = {a:.3f} * sugar_content_brix + {b:.3f}")
print(f"Hệ số R^2 = {r2:.3f}")
#
#4.4: Vẽ đồ thị hồi quy
#
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(X, y, alpha=0.5, label="Dữ liệu thực tế")
plt.plot(X, y_pred, color="red", label="Đường hồi quy")

plt.xlabel("Sugar content (Brix)")
plt.ylabel("Quality score")
plt.title("Hồi quy tuyến tính giữa độ ngọt và chất lượng chuối")
plt.legend()
plt.grid(True)

plt.savefig("output/hoi_quy_sugar_quality.png")
plt.show()
# ===============================
# BƯỚC 5: HỒI QUY TUYẾN TÍNH ĐA BIẾN
# ===============================

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 5.1. Chọn biến độc lập (X) và biến phụ thuộc (y)
features = [
    "sugar_content_brix",
    "firmness_kgf",
    "length_cm",
    "weight_g",
    "ripeness_index"
]

X = df[features]
y = df["quality_score"]

# 5.2. Khởi tạo & huấn luyện mô hình
model_multi = LinearRegression()
model_multi.fit(X, y)

# 5.3. Dự đoán
y_pred = model_multi.predict(X)

# 5.4. Hệ số hồi quy
coeff_df = pd.DataFrame({
    "Biến": features,
    "Hệ số": model_multi.coef_
})

print("\n=== HỒI QUY TUYẾN TÍNH ĐA BIẾN ===")
print("Intercept:", round(model_multi.intercept_, 3))
print(coeff_df)

# 5.5. Đánh giá mô hình
r2_multi = r2_score(y, y_pred)
print("Hệ số R^2 (đa biến):", round(r2_multi, 3))

# 5.6. Lưu hệ số ra file
coeff_df.to_csv("output/he_so_hoi_quy_da_bien.csv", index=False)

# ===============================
# 5.7. Biểu đồ Predicted vs Actual
# ===============================
# Vẽ biểu đồ Predicted vs Actual
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

# Lưu hình
plt.savefig("output/predicted_vs_actual_multivariate.png")
plt.show()
# ===============================
# BƯỚC 6: KIỂM TRA ĐA CỘNG TUYẾN (VIF)
# ===============================

from statsmodels.stats.outliers_influence import variance_inflation_factor

# Tính VIF cho từng biến
vif_data = pd.DataFrame()
vif_data["Biến"] = X.columns
vif_data["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])
]

print("\n=== KIỂM TRA ĐA CỘNG TUYẾN (VIF) ===")
print(vif_data)

# Lưu kết quả
vif_data.to_csv("output/vif.csv", index=False)
# ===============================
# BƯỚC 7: CHIA TRAIN / TEST
# ===============================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_multi.fit(X_train, y_train)

y_train_pred = model_multi.predict(X_train)
y_test_pred = model_multi.predict(X_test)

r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

print("\n=== ĐÁNH GIÁ TRAIN / TEST ===")
print("R² Train:", round(r2_train, 3))
print("R² Test :", round(r2_test, 3))


