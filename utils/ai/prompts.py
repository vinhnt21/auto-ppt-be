outline = """
<prompt>
    <role>
    Chuyên gia làm bài thuyết trình
    </role>

    <task>
    Tạo outline cho bài thuyết trình dựa trên nội dung bên dưới (content)
    </task>

    <content>
    {content}
    </content>

    <required>
    - Outline là phần tóm tắt ngắn gọn của bài thuyết trình, giúp người nghe hiểu được cấu trúc và nội dung chính của bài thuyết trình.
    - Outline bao gồm các phần chính của bài thuyết trình (từ 4 đến 6 phần, có thể nhiều hơn nếu cần) mỗi phần có một tiêu đề ngắn gọn (tối đa 15 từ).
    - Sử dụng ngôn ngữ thống nhất xuyên suốt bài thuyết trình, nếu content là tiếng Việt thì outline cũng phải là tiếng Việt, nếu có tiếng Anh thì cần chú thích trong ngoặcngoặc
    </required>

    <format>
    - Sử dụng định dạng markdown, mỗi ý là một gạch đầu dòng.
    - Nội dung trả về sẽ được sử dụng luôn, không cần có ``` ở đầu và cuối.
    </format>

    <example>
    - AI Agent là gì?
    - Ứng dụng của AI Agent trong thực tế
    - Các công nghệ AI Agent phổ biến
    - Tương lai của AI Agent
    </example> 
</prompt>
"""

content = """
<prompt>
    <role>
        Chuyên gia làm bài thuyết trình
    </role>
    <task>
        Tạo nội dung slide PowerPoint cho bài thuyết trình dựa trên outline và content dưới đây.
        Chỉ sử dụng các layout được liệt kê dưới.
    </task>
    <outline>
        {outline}
    </outline>
    <content>
        {content}
    </content>
    <layout>
        <layout_item>
            <type>Title Slide</type>
            <structure>
                <field name="title">Tiêu đề chính</field>
                <field name="subtitle">Phụ đề</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Title and Content</type>
            <structure>
                <field name="title">Tiêu đề</field>
                <field name="content">Nội dung chính</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Section Header</type>
            <structure>
                <field name="title">Tiêu đề phần</field>
                <field name="subtitle">Phụ đề phần</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Two Content</type>
            <structure>
                <field name="title">Tiêu đề</field>
                <field name="left_content">Nội dung bên trái (chỉ chứa text, không chứa thẻ con)</field>
                <field name="right_content">Nội dung bên phải (chỉ chứa text, không chứa thẻ con)</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Comparison</type>
            <structure>
                <field name="title">Tiêu đề so sánh</field>
                <field name="left_title">Tiêu đề bên trái</field>
                <field name="left_content">Nội dung bên trái (chỉ chứa text, không chứa thẻ con)</field>
                <field name="right_title">Tiêu đề bên phải</field>
                <field name="right_content">Nội dung bên phải (chỉ chứa text, không chứa thẻ con)</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Content with Caption</type>
            <structure>
                <field name="title">Tiêu đề</field>
                <field name="content">Nội dung chính</field>
                <field name="caption">Chú thích</field>
            </structure>
        </layout_item>
        <layout_item>
            <type>Picture with Caption</type>
            <structure>
                <field name="title">Tiêu đề</field>
                <field name="image_path">Mô tả hình ảnh cần chèn</field>
                <field name="caption">Chú thích</field>
            </structure>
        </layout_item>
    </layout>
    <required>
        <item>Chỉ sử dụng các layout được liệt kê ở trên.</item>
        <item>Nội dung cần đầy đủ và được trình bày một cách rõ ràng, dễ hiểu.</item>
        <item>Sử dụng linh hoạt các layout để trình bày nội dung một cách hợp lý và dễ hiểu.</item>
        <item>Đầu ra: Nội dung dạng XML, trình bày theo thứ tự các slide.</item>
        <item> Trả về nội dung dạng XML để tôi tạo file luôn, không thêm ``` ở đầu và cuối.</item>
        <item> Với phần file content trình bày nội dung theo gạch đầu dòng (-) và không có ý con. Mội slide có thể có từ 3 đến 6 gạch đầu dòng </item>
        <item> Thêm một vài slide có hình ảnh minh hoạ để tăng tính sinh động </item>
    </required>
    <format>
        <item>Nội dung xml chỉ bao gồm các thẻ slide, type, structure, field.</item>
        <item>Toàn bộ nội dung bọc trong thẻ <presentation></presentation>.</item>
        <item>Nội dung trả về phải tuân thủ chính xác cấu trúc đã định sẵn để sử dụng để convert qua slide luôn.</item>
        <item>Sử dụng các ký tự thay thế để tránh lỗi, bao gồm:</item>
        <subformat>
            <item>Ký tự nhỏ hơn `<` được thay bằng `&lt;`.</item>
            <item>Ký tự lớn hơn `>` được thay bằng `&gt;`.</item>
            <item>Ký tự `&` được thay bằng `&amp;`.</item>
        </subformat>
    </format>
    <example>
        <presentation>
            <slide>
                <type>Title Slide</type>
                <structure>
                    <field name="title">Tiêu đề chính</field>
                    <field name="subtitle">Phụ đề</field>
                </structure>
            </slide>
            <slide>
                <type>Title and Content</type>
                <structure>
                    <field name="title">Tiêu đề</field>
                    <field name="content">Nội dung chính</field>
                </structure>
            </slide>
            <slide>
                <type>Section Header</type>
                <structure>
                    <field name="title">Tiêu đề phần</field>
                    <field name="subtitle">Phụ đề phần</field>
                </structure>
            </slide>
        </presentation>
    </example>
</prompt>
"""

illustration = """
<prompt>
    <role>
        Chuyên gia viết prompt tạo ảnh 
    </role>
    <task>
        Tạo prompt dành cho DALL-E 3 để tạo hình ảnh minh họa cho slide PowerPoint này dựa trên slide_content và img_description  
    </task>
    <slide_content>
        {slide_content}
    </slide_content>
    <img_description>
        {img_description}
    </img_description>
    <format>
        <item>Chỉ cần trả về một prompt duy nhất để gửi cho DALL-E 3 tạo ảnh luôn</item>
        <item>Không cần dấu ``` ở đầu và cuối </item>
    </format>
    <example>
    A dramatic medium-wide shot shows a Vietnamese soldier marching through rugged terrain at dusk, with mist swirling around his boots. His determined stance and slightly raised rifle indicate readiness, while the backdrop reveals shadowy mountains fading into the twilight sky. Soft orange and purple hues blend as the sun sets, framing the soldier within an atmosphere of resilience and honor, capturing the essence of duty and courage.
    </example>
</prompt>
"""


file_name = """
<prompt>
    <task>
    Tạo tên file cho slide dựa trên nội dung bài giảng
    </task>

    <slide_content>
    {slide_content}
    </slide_content>

    <format>
    <item>Chỉ trả về trên file, không thêm ``` ở đầu và cuối</item>
    <item>Tên file là tiếng Việt không dấu, không chứa kí tự đặt biệt, dấu cách thay bằng dấu gạch dưới</item>
    <item>Chỉ chứa chữ cái, số và dấu gạch dưới</item>
    </format>

    <example>
    bai_7_gioi_thieu_ve_html
    </example>
</prompt>
"""
