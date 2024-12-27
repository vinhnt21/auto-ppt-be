from ai.ai_models import *


def get_outline_from_content(content) -> str:
    prompt = """Dưới đây là nội dung bài giảng cần làm slide:

{{content}}

Nhiệm vụ: Tạo outline chính cho bài thuyết trình.

Yêu cầu:
1. Chỉ liệt kê các phần chính (khoảng 4-6 phần)
2. Mỗi phần là một ý độc lập, ngắn gọn (khoảng 5-10 từ)
3. Trả về theo định dạng markdown với dấu gạch đầu dòng (-)
4. Các phần phải theo thứ tự logic, dễ theo dõi
5. Chỉ trả về phần nội dung outline để tôi sử dụng luôn, không thêm dấu ``` 

Ví dụ outline cho bài giảng về "Cuộc đời bác Hồ":
- Tuổi thơ
- Học tập
- Hoạt động cách mạng
- Thành tựu

Gợi ý: Đọc nội dung và tìm ra các phần chính, sau đó tóm tắt thành các ý ngắn gọn.
""".replace(
        "{{content}}", content
    )
    return get_answer(prompt)


def get_content_of_slide(outline, content):
    prompt = """Dưới đây là nội dung bài giảng cần làm slide:

{{content}}

Dưới đây là outline của bài giảng:

{{outline}}


Nhiệm vụ: Tạo nội dung slide cho bài thuyết trình.

Yêu cầu:
1. Mỗi slide tuân theo format markdown gồm tiêu đề (h2) và các ý chính (bullet points), chú ý chỉ được sử dụng header 2 (##) và bullet points (-)
## Tiêu đề slide
- Ý chính 1
- Ý chính 2
- Ý chính 3
2. Mỗi slide không quá 3 ý chính, nếu dài hơn thì tách thành slide mới
3. Chỉ trả về phần nội dung slide để tôi sử dụng luôn, không thêm dấu ```
4. Các slide phải theo thứ tự logic, dễ theo dõi
""".replace(
        "{{content}}", content
    ).replace(
        "{{outline}}", outline
    )

    return get_answer(prompt)


def get_topic_of_docx_from_content(outline, content):
    prompt = """Dưới đây là nội dung của bài giảng:
    
    {{content}}
    
    Dưới đây là outline của bài giảng:
    
    {{outline}}
    
    Nhiệm vụ: Tạo tên chủ đề cho bài giảng và 1 câu mô tả ngắn gọn.
    
    Yêu cầu:
    1. Tên chủ đề phải phản ánh đúng nội dung của bài giảng
    2. Tên chủ đề không quá dài, không quá ngắn
    3. Câu mô tả phải ngắn gọn, dễ hiểu
    4. Trả về theo format markdown, không thêm dấu ```
    ## Tên chủ đề
    - Câu mô tả ngắn gọn
    """.replace(
        "{{content}}", content
    ).replace(
        "{{outline}}", outline
    )

    return get_answer(prompt)


def get_slide_content(docx_content):
    def get_outline_slide_content(outline_str):
        MAX_POINTS_PER_SLIDE = 3
        outline = outline_str.split("- ")[1:]
        cnt = 0
        outline_slide = "## Nội dung thuyết trình\n"
        for i in range(len(outline)):
            if cnt < MAX_POINTS_PER_SLIDE:
                outline_slide += f"- {outline[i]}\n"
                cnt += 1
            else:
                cnt = 0
                outline_slide += f"\n## Nội dung thuyết trình (tiếp theo)\n"
                outline_slide += f"- {outline[i]}\n"
        return outline_slide + "\n"

    outline = get_outline_from_content(docx_content)
    topic = get_topic_of_docx_from_content(outline, docx_content)
    slides_content = get_content_of_slide(outline, docx_content)
    thank_you_slide = """## Cảm ơn các bạn đã lắng nghe!\n"""
    return f"{topic}\n\n{get_outline_slide_content(outline)}\n{slides_content}\n{thank_you_slide}"


def get_slide_name(slide_content):
    prompt = """Dưới đây là nội dung của bài giảng:

{{slide_content}}

Nhiệm vụ: Đặt tên cho bài giảng.
Yêu cầu:
1. Tên bài giảng phải phản ánh đúng nội dung của bài giảng.
2. Tên bài giảng không quá dài (tối đa 10 từ).
3. Chỉ trả về tên bài giảng, không cần thêm dấu ```.
4. Tên bài giảng là tiếng Việt không dấu, không viết hoa, cách nhau bởi dấu gạch ngang (-).

Ví dụ: "cuoc-doi-bac-ho"
""".replace(
        "{{slide_content}}", slide_content
    )

    return get_answer(prompt)


def get_img_description_for_slide_url(slide, content):
    prompt = """Nội dung bài giảng:
{{content}}

---

Nhiệm vụ:
Viết prompt để cung cấp cho model DALL·E 3 để sinh hình ảnh phù hợp với slide sau:
{{slide}}

---

Yêu cầu:
1. Mô tả đầy đủ các yếu tố sau theo thứ tự:
   - [Phương tiện]: Xác định loại hình ảnh (ví dụ: digital illustration, 3D render, oil painting, photograph).
   - [Chủ thể]: Mô tả chi tiết nhân vật hoặc vật thể chính.
   - [Môi trường]: Bối cảnh hoặc không gian xung quanh.
   - [Bố cục]: Xác định cách bố trí hình ảnh (ví dụ: close-up, wide shot, centered).
   - [Ánh sáng]: Mô tả ánh sáng (nguồn sáng, kiểu ánh sáng, độ sáng).
   - [Màu sắc]: Bảng màu hoặc tông màu chủ đạo.
   - [Tâm trạng]: Cảm giác hoặc cảm xúc mà hình ảnh muốn truyền tải.
   - ([Phong cách, họa sĩ, kỹ thuật]): Phong cách nghệ thuật, tên họa sĩ hoặc kỹ thuật cụ thể (nếu cần).
2. Chỉ trả về câu prompt để gửi cho model, không cần thêm dấu ```.
3. Tối đa 4000 kí tự
""".replace(
        "{{content}}", content
    ).replace(
        "{{slide}}", slide
    )

    prompt = get_answer(prompt)  # Prompt for DALL-E 3
    print(prompt)
    return get_img_url(prompt)
