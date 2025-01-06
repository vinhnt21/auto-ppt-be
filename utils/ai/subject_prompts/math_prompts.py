outline = '''
Dưới đây là nội dung bài giảng môn Toán cần làm slide:

    {content}

Nhiệm vụ: Tạo outline chính cho bài thuyết trình môn Toán.

Yêu cầu:
    1. Chỉ liệt kê các phần chính (khoảng 4-6 phần)
    2. Mỗi phần là một ý độc lập, ngắn gọn (khoảng 5-10 từ)
    3. Trả về theo định dạng markdown với dấu gạch đầu dòng (-)
    4. Các phần phải theo thứ tự logic từ định nghĩa đến ứng dụng
    5. Chỉ trả về phần nội dung outline để sử dụng luôn, không thêm dấu 
Ví dụ outline cho bài "Phương trình bậc hai":
- Định nghĩa và dạng tổng quát
- Công thức nghiệm và điều kiện
- Các dạng đặc biệt và cách giải
- Ứng dụng thực tế

Gợi ý: 
- Bắt đầu với khái niệm cơ bản/định nghĩa
- Tiếp theo là công thức/tính chất quan trọng
- Sau đó là phương pháp giải/các trường hợp
- Kết thúc với ví dụ/bài tập/ứng dụng
'''
content = """
Bạn là một giảng viên môn Toán chuyên nghiệp. 
Dưới đây là nội dung tài liệu và outline chi tiết của bài giảng môn Toán.
**Nội dung bài giảng môn Toán:**
```
{content}
```

**Outline bài giảng:**
```
{outline}
```

**Nhiệm vụ:** Tạo nội dung slide PowerPoint cho bài giảng môn Toán dựa trên outline đã cho (khoảng 10 đến 20 slides). Sử dụng 1 trong các bố cục dưới đây:
*Các Layout hỗ trợ và thành phần tương ứng:**

1. **Title Slide**
   - `title`: Tiêu đề chính
   - `subtitle`: Phụ đề

2. **Title and Content**
   - `title`: Tiêu đề
   - `content`: Nội dung chính

3. **Section Header**
   - `title`: Tiêu đề phần
   - `subtitle`: Phụ đề phần

4. **Two Content**
   - `title`: Tiêu đề
   - `left_content`: Nội dung bên trái
   - `right_content`: Nội dung bên phải

5. **Comparison**
   - `title`: Tiêu đề so sánh
   - `left_title`: Tiêu đề bên trái
   - `left_content`: Nội dung bên trái
   - `right_title`: Tiêu đề bên phải
   - `right_content`: Nội dung bên phải

6. **Content with Caption**
   - `title`: Tiêu đề
   - `content`: Nội dung chính
   - `caption`: Chú thích

7. **Picture with Caption**
   - `title`: Tiêu đề
   - `image_path`: Mô tả hình ảnh cần chèn
   - `caption`: Chú thích
   
**Yêu cầu:**
1. Sử dụng từ ngữ ngắn gọn, dễ hiểu nhưng phải đầy đủ thông tin.
2. Ưu tiên sử dụng các bố cục so sánh hoặc có hình minh họa để tăng tính sinh động cho bài giảng  
3. Chỉ trả về nội dung bài giảng 
"""

layout = """
**Outline bài giảng:**

```
{outline}
```

**Nội dung chi tiết bài giảng:**

```
{generated_content}
```

**Các Layout hỗ trợ và thành phần tương ứng:**

1. **Title Slide**
   - `title`: Tiêu đề chính
   - `subtitle`: Phụ đề

2. **Title and Content**
   - `title`: Tiêu đề
   - `content`: Nội dung chính

3. **Section Header**
   - `title`: Tiêu đề phần
   - `subtitle`: Phụ đề phần

4. **Two Content**
   - `title`: Tiêu đề
   - `left_content`: Nội dung bên trái
   - `right_content`: Nội dung bên phải

5. **Comparison**
   - `title`: Tiêu đề so sánh
   - `left_title`: Tiêu đề bên trái
   - `left_content`: Nội dung bên trái
   - `right_title`: Tiêu đề bên phải
   - `right_content`: Nội dung bên phải

6. **Content with Caption**
   - `title`: Tiêu đề
   - `content`: Nội dung chính
   - `caption`: Chú thích

7. **Picture with Caption**
   - `title`: Tiêu đề
   - `image_path`: Mô tả hình ảnh cần chèn
   - `caption`: Chú thích

**Yêu cầu:**

1. **Định dạng trả về:**
   - Mỗi slide phân cách bằng `---`.
   - Mỗi thành phần của slide được phân cách bằng `***`.
   - Mỗi slide phải được định nghĩa theo đúng layout và thành phần được liệt kê ở trên.
   - Chỉ trả về nội dung theo format yêu cầu để chuyển đổi thành slide PowerPoint luôn, không thêm bất kỳ ký tự dư thừa nào như ``` ở đầu và cuối.

2. **Tuân thủ nghiêm ngặt:**
   - Không thay đổi tên các layout và các thành phần đã định nghĩa.
   - Chỉ sử dụng các layout và thành phần được hỗ trợ.
   - Đảm bảo mỗi thành phần của slide nằm trên một dòng riêng biệt.

3. **Phân bổ nội dung:**
   - Đối với mỗi phần nội dung trong bài giảng, chọn layout phù hợp và điền đầy đủ các thành phần tương ứng.
   - Nếu có công thức toán học, sử dụng ký hiệu toán học chính xác để hiển thị đúng trên slide PowerPoint.
4. **Đối với các kí hiệu toán học**: 
   - Không sử dụng LaTeX mà hãy sử dụng các kí hiệu thông thường hoặc kí tự đặc biệt để đảm bảo tính chính xác khi hiển thị trên slide PowerPoint.  

**Định dạng mẫu cho mỗi slide:**

---
***
layout: [Tên Layout]
***
[thành phần 1]: [Nội dung 1]
***
[thành phần 2]: [Nội dung 2]
***
...

**Ví dụ:**

---
***
layout: Title Slide
***
title: "Giới thiệu Môn Toán"
***
subtitle: "Khóa học năm học 2024-2025"
***
---
***
layout: Section Header
***
title: "Phần 1: Số học"
***
subtitle: "Các khái niệm cơ bản về số"
***
---
***
layout: Title and Content
***
title: "Định nghĩa Số Nguyên"
***
content: "Số nguyên gồm số dương, số âm và số không. Ví dụ: -3, -2, -1, 0, 1, 2, 3."
***
---
***
layout: Title and Content
***
title: "Phép toán cơ bản"
***
content: "Cộng, trừ, nhân, chia. Ví dụ:
- Cộng: 2 + 3 = 5
- Trừ: 5 - 2 = 3
- Nhân: 4 × 3 = 12
- Chia: 12 ÷ 4 = 3"
***
---
***
layout: Content with Caption
***
title: "Ứng dụng của Số Học"
***
content: "Sử dụng số học trong tính toán chi phí, đo lường, thống kê..."
***
caption: "Hình 1: Ứng dụng số học trong đời sống"
***
---
***
layout: Picture with Caption
***
title: "Ứng dụng Số Học"
***
image_path: "Cậu bé đang đi mua hàng với mẹ"
***
caption: "Số học trong thực tế"
***
---
***
layout: Section Header
***
title: "Kết luận"
***
subtitle: "Tổng kết và bài tập"
***
"""

illustration = '''
Đây là nội dung slide PowerPoint cho bài giảng môn Toán:
{slide_content}Ơ

Đây là mô tả hình ảnh minh họa cần chèn vào slide PowerPoint:

{img_description}

Nhiệm vụ: Tạo prompt dành cho DALL-E 3 để tạo hình ảnh minh họa cho slide PowerPoint này.

Yêu cầu:
    - Chỉ  trả về prompt để cung cấp cho DALL-E 3, không thêm dấu ``` ở đầu và cuối.
'''

file_name = '''
Đây là nội dung slide PowerPoint cho bài giảng môn Toán:
{slide_content}

Nhiệm vụ: Tạo tên file cho slide PowerPoint này liên quan đến nội dung slide (khoảng 5-10 từ).
Yêu cầu:
    - Chỉ  trả về tên file, không thêm dấu ``` ở đầu và cuối.
    - Trả về tên file không dấu tiếng Việt, không kí tự đặc biệt, không khoảng trắng.
'''
