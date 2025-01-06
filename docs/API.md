# Các bước xử lý

## 1. Lấy mục lục bài giảng

### Mô tả:

- Người dùng tải lên file docx hoặc pdf, hoặc nhập nội dung bài giảng vào ô input
- Nhận về một mục lục bài giảng

### API: `/api/slides/get-outline`

- Method: POST
- Request:
    - body (form-data):
        - file: docx or pdf file
        - user_input: string
        - subject: string
- phải có ít nhất 1 trường files hoặc user_input

- Response:

    - Suscess: 200

        - body:
            - outline: [string] (Array nhiều string, hiển thị vào các ô input cho người dùng chỉnh sửa)
            - content: string (Nội dung input của người dùng)
    - Error: 400
        - body:
            - message: string

---

## 2. Tạo nội dung từng slide tương ứng với mục lục, hiển thị trên trình duyệt trước

### Mô tả:

- Người dùng bấm nút tạo nội dung
- Nhận về nội dung từng slide tương ứng với mục lục

### API:

#### `/api/slides/get-content`

- Method: POST
- Request:

    - body (json):
        - outline: [string] (Array nhiều string mà người dùng vừa chỉnh sửa)
        - subject: string
        - content: string
- Response:

    - Suscess: 200

        - body:
            - content: string

    - Error: 400
        - body:
            - message: string

---

## 3. Tạo file slide

### Mô tả:

- Người dùng bấm nút tạo file slide
- Nhận về file slide

#### `/api/slides/create-slide`

- Method: POST
- Request:
    - body (json):
        - slide-content: string
        - subject: string
        - template_name: string

- Response:
    - Suscess: 200
        - body:
            - file_name: string (link download file slide, hiển thị thành 1 nút khi bấm vào thì tải file về)