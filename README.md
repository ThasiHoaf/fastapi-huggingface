# Phân loại hình ảnh với FastAPI và Vision Transformer (ViT)

## Thông tin sinh viên
- **Họ và tên:** Ngô Thái Hòa
- **MSSV:** 24120051
- **Môn học:** Tư duy tính toán - Khoa Công Nghệ Thông Tin - Trường Đại học Khoa Học Tự Nhiên TP.HCM.

## Thông tin mô hình
- **Tên mô hình:** `google/vit-base-patch16-224`
- **Chức năng:** Phân loại hình ảnh (Image Classification) thành 1 trong 1000 lớp của tập dữ liệu ImageNet.
- **Liên kết Hugging Face:** [https://huggingface.co/google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224)

## Hướng dẫn cài đặt
1. Clone repository này về máy:
   ```bash
   git clone [URL_GITHUB_CUA_BAN]
   cd fastapi-huggingface
   ```

2. Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

## Hướng dẫn chạy chương trình
1. Khởi chạy server FastAPI bằng Uvicorn:
    ``` bash
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

### Hướng dẫn gọi API
1. Sử dụng cURL, Postman hoặc chạy script client.py đã cung cấp sẵn.
    ```bash
        curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@test_images/dua.jpeg;type=image/jpeg"
    ```
Hoặc

2. Sử dụng Pinggy để tạo đường liên kết đến server để có thể chạy ở local nếu ứng dụng đang chạy ở máy khác
    ```bash
        !npm install -g localtunnel !lt --port 8000
    ```

### Video Huong dan
[Link](https://drive.google.com/file/d/1bNIiOO7xJ1Ecsi7rJO6gaznTYfaJ000H/view?usp=sharing)