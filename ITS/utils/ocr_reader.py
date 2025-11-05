import easyocr
# Khởi tạo trình đọc OCR cho tiếng Anh
reader = easyocr.Reader(['en']) 

# Sử dụng ảnh mẫu trực tuyến
sample_image = 'https://raw.githubusercontent.com/jaidedAI/EasyOCR/master/examples/english.png'

print("Đang nhận dạng...") 

results = reader.readtext(sample_image)

print("\n**Kết quả nhận dạng:**")
for (bbox, text, prob) in results:
    # Đã sửa lỗi cú pháp f-string
    print(f"{text} (độ chính xác: {prob:.2f})") 

print("\nChạy OCR thành công!")
