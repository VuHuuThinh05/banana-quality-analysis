"""Multicollinearity diagnostics and out-of-sample regression evaluation."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from statsmodels.api import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

from common import FEATURES, TARGET, OUTPUT_DIR, load_dataset

df = load_dataset()
X = df[FEATURES]
y = df[TARGET]

# Include an intercept in the auxiliary VIF regressions.
X_with_constant = add_constant(X, has_constant="add")
vif_df = pd.DataFrame({
    "Biến": FEATURES,
    "VIF": [
        variance_inflation_factor(X_with_constant.values, i + 1)
        for i in range(len(FEATURES))
    ],
})
csv_dir = OUTPUT_DIR / "csv"
csv_dir.mkdir(parents=True, exist_ok=True)
vif_df.to_csv(csv_dir / "vif.csv", index=False)

print("\n=== KIỂM TRA ĐA CỘNG TUYẾN (VIF, có intercept) ===")
print(vif_df)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

print("\n=== ĐÁNH GIÁ TRAIN / TEST ===")
for label, y_true, y_pred in (
    ("Train", y_train, model.predict(X_train)),
    ("Test", y_test, model.predict(X_test)),
):
    print(
        f"{label}: R²={r2_score(y_true, y_pred):.4f}, "
        f"MAE={mean_absolute_error(y_true, y_pred):.4f}, "
        f"RMSE={np.sqrt(mean_squared_error(y_true, y_pred)):.4f}"
    )
