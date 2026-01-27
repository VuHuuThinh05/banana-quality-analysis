import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

# =========================
# PHẦN 7: VIF & TRAIN / TEST
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

# Thư mục output
CSV_DIR = os.path.join(BASE_DIR, "..", "output", "csv")
os.makedirs(CSV_DIR, exist_ok=True)

# Đọc dữ liệu
df = pd.read_csv(DATA_PATH)

# =========================
# 7.1 Chọn biến
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
# 7.2 KIỂM TRA ĐA CỘNG TUYẾN (VIF)
# =========================
vif_df = pd.DataFrame()
vif_df["Biến"] = X.columns
vif_df["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])
]

print("\n=== KIỂM TRA ĐA CỘNG TUYẾN (VIF) ===")
print(vif_df)

# Lưu VIF
vif_df.to_csv(
    os.path.join(CSV_DIR, "vif.csv"),
    index=False
)

# =========================
# 7.3 CHIA TRAIN / TEST
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Đánh giá
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)

print("\n=== ĐÁNH GIÁ TRAIN / TEST ===")
print("R² Train:", round(r2_train, 3))
print("R² Test :", round(r2_test, 3))
