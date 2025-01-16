# Tài liệu API: Hỗ trợ tạo nội dung slide

## 1. Lấy mục lục 

### Mô tả

- Người dùng có thể tải lên file docx hoặc pdf, hoặc nhập nội dung bài giảng trực tiếp vào ô input.
- Hệ thống sẽ trả về mục lục bài giảng.

### API: `/api/slides/get-outline`

- **Phương thức**: `POST`
- **Yêu cầu**:
  - **Body** (form-data):
    - `file`: Tệp docx hoặc pdf
    - `user_input`: Chuỗi nội dung do người dùng nhập
  - **Lưu ý**: Phải có ít nhất một trong hai trường `file` hoặc `user_input`.

- **Phản hồi**:
  - **Thành công**: `200`
    - **Body**:
      - `outline`: `[string]` (Mảng các chuỗi hiển thị mục lục, để người dùng chỉnh sửa)
      - `content`: `string` (Nội dung bài giảng của người dùng)
  - **Lỗi**: `400`
    - **Body**:
      - `message`: `string` (Thông báo lỗi)

---

## 2. Tạo nội dung từng slide tương ứng với mục lục

### Mô tả

- Sau khi người dùng bấm nút tạo nội dung, hệ thống sẽ tạo nội dung từng slide dựa trên mục lục đã chỉnh sửa.

### API: `/api/slides/get-content`

- **Phương thức**: `POST`
- **Yêu cầu**:
  - **Body** (json):
    - `outline`: `[string]` (Mảng các chuỗi mục lục đã chỉnh sửa bởi người dùng)
    - `content`: `string` (Nội dung bài giảng gốc)

- **Phản hồi**:
  - **Thành công**: `200`
    - **Body**:
      - `content`: `string` (Nội dung của từng slide)
  - **Lỗi**: `400`
    - **Body**:
      - `message`: `string` (Thông báo lỗi)

---

## 3. Tạo file slide

### Mô tả

- Sau khi người dùng bấm nút tạo file slide, hệ thống sẽ tạo và cung cấp file slide để tải về.

### API: `/api/slides/create-slide`

- **Phương thức**: `POST`
- **Yêu cầu**:
  - **Body** (json):
    - `slide`: `string` (Nội dung slide)
    - `template_name`: `string` (Tên mẫu giao diện slide)

- **Phản hồi**:
  - **Thành công**: `200`
    - **Body**:
      - `file_name`: `string` (Liên kết tải file slide, hiển thị dưới dạng nút tải về)
  - **Lỗi**: `400`
    - **Body**:
      - `message`: `string` (Thông báo lỗi)


---

## 4. Download

### Mô tả

- Người dùng có thể tải file slide đã tạo về máy.

### API: `/api/slides/download/{file_name}`
- **Phương thức**: `GET`
- **Yêu cầu**:
  - **Params**:
    - `file_name`: `string` (Tên file slide)

