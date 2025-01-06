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
      - outline: string

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
    - outline: string
    - subject: string

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
    - content: string
    - subject: string


```json
 {
    "light": {
        "title_style": {
            "font_name": "Helvetica",
            "font_size": 44,
            "font_color": (31, 73, 125)  # Navy Blue
        },
        "subtitle_style": {
            "font_name": "Helvetica",
            "font_size": 32,
            "font_color": (68, 114, 196)  # Light Blue
        },
        "content_style": {
            "font_name": "Arial",
            "font_size": 24,
            "font_color": (0, 0, 0)  # Black
        },
        "bg_color": (255, 255, 255)  # White
    },

    "dark": {
        "title_style": {
            "font_name": "Helvetica",
            "font_size": 44,
            "font_color": (255, 255, 255)  # White
        },
        "subtitle_style": {
            "font_name": "Helvetica",
            "font_size": 32,
            "font_color": (189, 215, 238)  # Light Blue
        },
        "content_style": {
            "font_name": "Arial",
            "font_size": 24,
            "font_color": (242, 242, 242)  # Light Gray
        },
        "bg_color": (44, 44, 44)  # Dark Gray
    },

    "monochrome": {
        "title_style": {
            "font_name": "Roboto",
            "font_size": 44,
            "font_color": (0, 0, 0)  # Black
        },
        "subtitle_style": {
            "font_name": "Roboto",
            "font_size": 32,
            "font_color": (64, 64, 64)  # Dark Gray
        },
        "content_style": {
            "font_name": "Roboto",
            "font_size": 24,
            "font_color": (89, 89, 89)  # Medium Gray
        },
        "bg_color": (242, 242, 242)  # Light Gray
    },

    "vibrant": {
        "title_style": {
            "font_name": "Impact",
            "font_size": 44,
            "font_color": (255, 89, 0)  # Orange
        },
        "subtitle_style": {
            "font_name": "Arial",
            "font_size": 32,
            "font_color": (0, 168, 133)  # Turquoise
        },
        "content_style": {
            "font_name": "Arial",
            "font_size": 24,
            "font_color": (64, 64, 64)  # Dark Gray
        },
        "bg_color": (255, 255, 240)  # Ivory
    },

    "elegant": {
        "title_style": {
            "font_name": "Garamond",
            "font_size": 44,
            "font_color": (128, 0, 32)  # Burgundy
        },
        "subtitle_style": {
            "font_name": "Garamond",
            "font_size": 32,
            "font_color": (112, 48, 48)  # Dark Red
        },
        "content_style": {
            "font_name": "Calibri",
            "font_size": 24,
            "font_color": (64, 64, 64)  # Dark Gray
        },
        "bg_color": (245, 245, 245)  # Off White
    }
}
```