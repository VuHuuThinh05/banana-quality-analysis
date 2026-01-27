# 📊 PHÂN TÍCH MỐI QUAN HỆ GIỮA ĐỘ NGỌT VÀ CHẤT LƯỢNG CHUỐI

## 1. Mục tiêu đề tài
Đề tài nhằm phân tích mối quan hệ giữa **độ ngọt (Sugar Content – Brix)** và **chất lượng chuối (Quality Score)** dựa trên dữ liệu thực nghiệm, sử dụng các phương pháp:
- Thống kê mô tả
- Phân tích tương quan
- Hồi quy tuyến tính đơn biến
- Hồi quy tuyến tính đa biến
- Đánh giá mô hình bằng R² và kiểm tra đa cộng tuyến (VIF)

---

## 2. Dữ liệu sử dụng
- File dữ liệu: `banana_quality_dataset.csv`
- Số quan sát: 1000 mẫu
- Một số biến chính:
  - `sugar_content_brix`: Độ ngọt (Brix)
  - `quality_score`: Điểm chất lượng
  - `firmness_kgf`: Độ cứng
  - `length_cm`: Chiều dài
  - `weight_g`: Khối lượng
  - `ripeness_index`: Chỉ số độ chín

---

## 3. Các bước phân tích đã thực hiện

### Bước 1. Thống kê mô tả
- Tính các chỉ số: mean, std, min, max, quartile
- Lưu kết quả vào: `output/thong_ke_mo_ta.csv`

### Bước 2. Trực quan hóa phân bố
- Histogram độ ngọt
- Histogram điểm chất lượng
- Lưu các biểu đồ vào thư mục `output/`

### Bước 3. Phân tích tương quan
- Tính hệ số tương quan Pearson
- Vẽ heatmap ma trận tương quan
- Kết quả: độ ngọt có tương quan dương khá mạnh với chất lượng

### Bước 4. Hồi quy tuyến tính đơn biến
- Mô hình:  
  `quality_score = a * sugar_content_brix + b`
- Hệ số R² ≈ 0.36
- Vẽ biểu đồ Scatter + đường hồi quy

### Bước 5. Hồi quy tuyến tính đa biến
- Các biến độc lập:  
  `sugar_content_brix`, `firmness_kgf`, `length_cm`, `weight_g`, `ripeness_index`
- Hệ số R² (đa biến): **≈ 0.984**
- Vẽ biểu đồ **Predicted vs Actual**
- Lưu hệ số hồi quy: `output/he_so_hoi_quy_da_bien.csv`

### Bước 6. Đánh giá mô hình & đa cộng tuyến
- Chia tập **Train/Test**
- R² Train ≈ 0.984, R² Test ≈ 0.983 → mô hình không overfitting
- Kiểm tra VIF:
  - Một số biến có VIF > 5 → tồn tại đa cộng tuyến
  - Phù hợp với dữ liệu thực tế (các thuộc tính sinh học có liên quan nhau)

---

## 4. Kết luận
- Độ ngọt là yếu tố ảnh hưởng mạnh đến chất lượng chuối
- Hồi quy đa biến cho khả năng dự đoán rất tốt
- Mô hình phù hợp cho mục tiêu phân tích và minh họa kiến thức học phần

---

## 5. Công nghệ sử dụng
- Python 3.11
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- statsmodels
- Visual Studio Code

---

## 6. Cấu trúc thư mục
DoAn/
├── data/
│ └── banana_quality_dataset.csv
├── output/
│ ├── he_so_hoi_quy_da_bien.csv
│ ├── ma_tran_tuong_quan.csv
│ ├── thong_ke_mo_ta.csv
│ ├── vif.csv
│ ├── predicted_vs_actual_multivariate.png
│ ├── scatter_sugar_quality.png
│ ├── scatter_firmness_quality.png
│ ├── hist_quality_score.png
│ ├── hist_sugar_content.png
│ ├── heatmap_tuong_quan.png
│ └── hoi_quy_sugar_quality.png
├── src/
│ └── ktptdl.py
└── README.md