# project-team-AI
Dự án về nhận diện biển số xe
LicensePlateRecognition/
│
├── app.py                     # File chính chạy
├── run.ipynb                  # Notebook để chạy trực tiếp
│
├── model/
│   └── best.pt                # Mô hình YOLO
│
├── utils/
│   ├── detector.py            # Nhận diện bằng YOLO
│   ├── ocr_reader.py          # Đọc chữ (EasyOCR)
│   └── file_utils.py          # Xử lý file & lưu ảnh
│
└── static/
    ├── outputs/               # Video + ảnh sau xử lý
    └── plates/                # Ảnh riêng phần biển số
