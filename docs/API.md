# Luồng xử lý điển hình:

- Upload DOCX → Nhận nội dung slides
- Tạo PowerPoint → Nhận link download
- Download file PPTX đã tạo

---

# Upload DOCX API

- Endpoint: /upload-docx
- Method: POST
- Content-Type: multipart/form-data

- Chức năng: Upload và xử lý file DOCX
- Input: File DOCX (max 5MB)
- Output:

  - Success: {"slides_content": [...]} (200)
  - Error: {"error": "error message"} (400/500)

- Xử lý:
  - Kiểm tra file hợp lệ
  - Lưu file vào thư mục uploads
  - Trích xuất nội dung từ DOCX
  - Chuyển đổi thành định dạng slides

---

# Create PowerPoint API

- Endpoint: /create-powerpoint
- Method: POST
- Content-Type: application/json

- Chức năng: Tạo file PowerPoint từ nội dung slides
- Input Body:

  ```json
  {
  "slides_content": ["nội dung slide"],
  "slide_with_img": boolean
  }
  ```

- Output:

  - Success: {"link_to_download": "/download/filename.pptx"} (200)
  - Error: {"error": "error message"} (400/500)

- Xử lý:

  - Tạo nội dung markdown
  - Thêm hình ảnh nếu cần
  - Tạo file MD và PPTX
  - Trả về link download

---

# Download File API

- Endpoint: /download/<filename>
- Method: GET

- Chức năng: Download file PowerPoint đã tạo
- Input: Tên file trong URL
- Output:

  - Success: File PPTX
  - Error: {"error": "error message"} (500)

- Xử lý:

- Tìm file trong thư mục slides
- Gửi file cho client download

---

# Các tính năng chung:

- Xử lý lỗi toàn diện với try-catch
- Logging chi tiết
- Tự động tạo thư mục cần thiết
- Giới hạn kích thước file upload (5MB)
- Hỗ trợ CORS
- Chỉ chấp nhận file .docx
