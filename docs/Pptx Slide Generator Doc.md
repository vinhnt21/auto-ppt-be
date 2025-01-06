# Tài liệu mô tả và hướng dẫn sử dụng mã tạo slide PowerPoint

## **1. Tổng quan**

Mã Python này cung cấp các hàm tiện ích để tạo và định dạng các slide trong PowerPoint, sử dụng thư viện `python-pptx`.
Nó hỗ trợ tạo các layout slide khác nhau, áp dụng kiểu dáng, thay đổi nền và lưu file PowerPoint.

---

## **2. Layout được hỗ trợ**

Dưới đây là danh sách các layout được hỗ trợ:

- **Title Slide**: Slide với tiêu đề và phụ đề.
- **Title and Content**: Slide với tiêu đề và khung nội dung.
- **Section Header**: Slide tiêu đề phân chia phần.
- **Two Content**: Slide với tiêu đề và hai cột nội dung.
- **Comparison**: Slide so sánh với hai cột (mỗi cột có tiêu đề và nội dung).
- **Content with Caption**: Slide với tiêu đề, nội dung, và chú thích.
- **Picture with Caption**: Slide với tiêu đề, hình ảnh, và chú thích.

---

## **3. Hướng dẫn sử dụng**
```python
from utils.slides.slide_generator import *
```

### **3.1. Khởi tạo PowerPoint**

Sử dụng hàm `init_presentation` để khởi tạo:

```python
prs = init_presentation()
```

### **3.2. Tạo slide**

Sử dụng hàm `create_slide` để tạo slide dựa trên layout:

#### **Cách gọi:**

```python
create_slide(prs, layout_name, **kwargs)
```

#### **Tham số:**

- `prs`: Đối tượng `Presentation`.
- `layout_name`: Tên layout (phải khớp với key trong `LAYOUT`).
- `**kwargs`: Các tham số bổ sung phụ thuộc vào từng layout.

#### **Ví dụ:**

1. **Slide tiêu đề:**
   ```python
   create_slide(prs, 'Title Slide', title="Welcome", subtitle="Introduction to AI")
   ```

2. **Slide với nội dung:**
   ```python
   create_slide(prs, 'Title and Content', title="Overview", content="This is the content.")
   ```

3. **Slide với hai cột nội dung:**
   ```python
   create_slide(prs, 'Two Content', title="Comparison", left_content="Advantages", right_content="Disadvantages")
   ```

4. **Slide so sánh:**
   ```python
   create_slide(prs, 'Comparison', title="AI vs Human",
                left_title="AI", left_content="Fast, Logical",
                right_title="Human", right_content="Creative, Emotional")
   ```

5. **Slide với chú thích:**
   ```python
   create_slide(prs, 'Content with Caption', title="Key Points",
                content="AI is transforming industries", caption="Remember these key points.")
   ```

6. **Slide với hình ảnh:**
   ```python
   create_slide(prs, 'Picture with Caption', title="AI in Action",
                image_path="path/to/image.jpg", caption="AI automates tasks.")
   ```

---

### **3.3. Áp dụng kiểu dáng cho slide**

#### **Áp dụng kiểu dáng cho tất cả các slide:**

Sử dụng `apply_global_styles` để áp dụng kiểu dáng đồng loạt:

```python
apply_global_styles(
    prs,
    title_style=("Arial", 32, (0, 0, 0)),  # Font, size, màu cho tiêu đề
    subtitle_style=("Calibri", 28, (128, 128, 128)),  # Font, size, màu cho phụ đề
    content_style=("Calibri", 24, (51, 51, 51)),  # Font, size, màu cho nội dung
    bg_color=(240, 240, 240)  # Màu nền
)
```

#### **Cách tùy chỉnh:**

- `title_style`: Tuple gồm (font_name, font_size, font_color).
- `subtitle_style`: Tương tự `title_style`, nhưng áp dụng cho phụ đề.
- `content_style`: Tương tự `title_style`, nhưng áp dụng cho nội dung.
- `bg_color`: Màu nền dạng RGB (mặc định là trắng: `(255, 255, 255)`).

---

### **3.4. Lưu file PowerPoint**

Sau khi tạo xong slide, sử dụng hàm `save_presentation` để lưu:

```python
save_presentation(prs, "output.pptx")
```

---

## **4. Danh sách các hàm chính**

### **Khởi tạo và tạo slide:**

- `init_presentation(template_path=None)`: Khởi tạo một file PowerPoint mới hoặc từ template.
- `create_slide(prs, layout_name, **kwargs)`: Hàm điều phối để tạo slide.

### **Tạo từng loại slide:**

- `add_title_slide(prs, title, subtitle)`: Tạo slide tiêu đề.
- `add_title_and_content_slide(prs, title, content)`: Tạo slide với nội dung.
- `add_section_header_slide(prs, title, subtitle)`: Tạo slide chia phần.
- `add_two_content_slide(prs, title, left_content, right_content)`: Tạo slide với hai cột.
- `add_comparison_slide(prs, title, left_title, left_content, right_title, right_content)`: Tạo slide so sánh.
- `add_content_with_caption_slide(prs, title, content, caption)`: Tạo slide với chú thích.
- `add_picture_with_caption_slide(prs, title, image_path, caption)`: Tạo slide với hình ảnh và chú thích.

### **Áp dụng kiểu dáng và nền:**

- `apply_global_styles(prs, title_style, subtitle_style, content_style, bg_color)`: Áp dụng kiểu dáng và màu nền.
- `apply_style_to_all_slides(prs, title_style, subtitle_style, content_style)`: Áp dụng kiểu dáng đồng loạt.
- `set_background_for_all_slides(prs, bg_color)`: Thay đổi nền cho tất cả slide.

### **Lưu file:**

- `save_presentation(prs, output_path)`: Lưu file PowerPoint.

---

## **5. Ghi chú**

- Hãy đảm bảo các đường dẫn như `image_path` trỏ đến file hợp lệ.
- Có thể mở rộng các hàm nếu cần thêm layout hoặc chức năng khác.
- Để tối ưu trải nghiệm, kiểm tra nội dung đầu vào (`kwargs`) trước khi truyền vào các hàm.

