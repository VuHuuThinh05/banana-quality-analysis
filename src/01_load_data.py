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