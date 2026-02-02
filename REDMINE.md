# REDMINE - Các bước triển khai và kiểm tra Lambda/DynamoDB local

1. Kiểm tra phiên bản AWS SAM CLI:

   ```
   sam --version
   ```

2. Tạo Python virtual environment:

   ```
   python -m venv .venv
   ```

   - Kích hoạt môi trường ảo:
     - Trên Linux/Mac:
       ```
       source .venv/bin/activate
       ```
     - Trên Windows (cmd):
       ```
       .venv\Scripts\activate
       ```
     - Trên Windows (PowerShell):
       ```
       .venv\Scripts\Activate.ps1
       ```
   - Cài đặt các package cần thiết:
     ```
     pip install -r requirements.txt
     ```

3. Khởi động DynamoDB local bằng Docker Compose:

   ```
   docker compose up -d
   ```

4. Tạo bảng DynamoDB local:

   ```
   aws dynamodb create-table --table-name users-local --attribute-definitions AttributeName=pk,AttributeType=S --key-schema AttributeName=pk,KeyType=HASH --billing-mode PAY_PER_REQUEST --endpoint-url http://localhost:8000
   ```

5. Kiểm tra table đã tồn tại:

   ```
   aws dynamodb list-tables --endpoint-url http://localhost:8000
   ```

   - Đảm bảo có table `users-local`.

6. Chạy SAM Local API Gateway với biến môi trường:

   ```
   sam local start-api --env-vars env/local.json
   ```

7. Kiểm tra API qua browser hoặc Postman:
   - Truy cập: `http://127.0.0.1:3000/users/1`

8. Nếu chưa có dữ liệu, tạo file thêm user mẫu:
   - File: `add_sample_user.py`
   - Chạy lệnh:
     ```
     python add_sample_user.py
     ```

9. Kiểm tra lại API, xác nhận user đã trả về đúng dữ liệu.

10. Nếu gặp lỗi timeout hoặc không kết nối được DynamoDB:

- Kiểm tra lại endpoint trong biến môi trường (`DYNAMODB_ENDPOINT` phải là `http://host.docker.internal:8000` khi chạy qua Docker/SAM Local).
- Sửa code lấy endpoint từ biến môi trường thay vì hardcode.

11. Kiểm tra log chi tiết khi invoke hoặc start-api để xác định lỗi.

---

Ghi chú:

- Đảm bảo các file cấu hình (`local.json`, `template.yaml`) và code đã đúng như hướng dẫn.
- Nếu cần thêm user hoặc custom dữ liệu, chỉnh sửa file `add_sample_user.py`.
