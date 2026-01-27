🍌 Banana Quality Analysis

Phân tích các yếu tố ảnh hưởng đến chất lượng chuối bằng hồi quy tuyến tính

1. Giới thiệu:

Dự án này được thực hiện trong khuôn khổ bài tập lớn môn Phân tích Dữ liệu, với mục tiêu phân tích mối quan hệ giữa các đặc trưng vật lý – hóa học của chuối và điểm chất lượng tổng thể (quality_score) dựa trên dữ liệu thực nghiệm.
Thông qua các phương pháp thống kê mô tả, trực quan hóa và hồi quy tuyến tính, dự án giúp sinh viên vận dụng kiến thức đã học vào một bài toán phân tích dữ liệu thực tế.

2. Dữ liệu:

- Nguồn dữ liệu: Kaggle – Banana Quality Dataset
- Số lượng biến chính:
+ sugar_content_brix: Độ ngọt
+ firmness_kgf: Độ cứng
+ length_cm: Chiều dài
+ weight_g: Khối lượng
+ ripeness_index: Chỉ số độ chín
+ quality_score: Điểm chất lượng (biến mục tiêu)
- Dữ liệu được lưu trong thư mục data/banana_quality_dataset.csv.

3. Nội dung phân tích:

Dự án được triển khai theo các bước sau:
🔹 Bước 1: Thống kê mô tả
Phân tích các đặc trưng thống kê cơ bản (mean, std, min, max…) của các biến số nhằm hiểu tổng quan về dữ liệu.
🔹 Bước 2: Trực quan hóa dữ liệu
Histogram phân bố độ ngọt và chất lượng
Scatter plot thể hiện mối quan hệ giữa các yếu tố và chất lượng chuối
🔹 Bước 3: Phân tích tương quan
Tính ma trận tương quan Pearson
Vẽ heatmap để đánh giá mức độ liên hệ giữa các biến
🔹 Bước 4: Hồi quy tuyến tính đơn
Xây dựng mô hình hồi quy giữa độ ngọt (sugar_content_brix) và quality_score để đánh giá ảnh hưởng trực tiếp của độ ngọt đến chất lượng.
🔹 Bước 5: Hồi quy tuyến tính đa biến
Xây dựng mô hình hồi quy đa biến với nhiều yếu tố đầu vào nhằm dự đoán chất lượng chuối chính xác hơn.
🔹 Bước 6: Kiểm tra đa cộng tuyến & đánh giá mô hình
Kiểm tra đa cộng tuyến (VIF) giữa các biến độc lập
Đánh giá mô hình bằng cách chia Train/Test và so sánh R²

4. Kết quả chính:

Mô hình hồi quy đa biến đạt R² cao (~0.98)
Kết quả Train/Test gần tương đương, cho thấy mô hình có khả năng tổng quát hóa tốt
Một số biến có VIF cao, phản ánh hiện tượng đa cộng tuyến – phù hợp với dữ liệu thực nghiệm

5. Công nghệ sử dụng:
- Python 3.11
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- statsmodels
- Visual Studio Code

6. Cấu trúc thư mục
banana-quality-analysis/
│
├── data/
│   └── banana_quality_dataset.csv
│
├── src/
│   ├── 01_load_data.py
│   ├── 02_descriptive_statistics.py
│   ├── 03_visualization.py
│   ├── 04_correlation_analysis.py
│   ├── 05_simple_regression.py
│   ├── 06_multivariate_regression.py
│   └── 07_vif_train_test.py
│
├── output/
│   ├── csv/
│   └── png/
│
└── README.md
7. Kết luận:

Dự án đã áp dụng thành công các kiến thức cơ bản của môn "Kỹ Thuật Phân tích Dữ liệu" để phân tích và dự đoán chất lượng chuối. Kết quả cho thấy các yếu tố như độ ngọt và độ chín có ảnh hưởng đáng kể đến chất lượng tổng thể.
Trong tương lai, mô hình có thể được mở rộng bằng cách áp dụng các phương pháp học máy nâng cao hơn để cải thiện độ chính xác dự đoán.