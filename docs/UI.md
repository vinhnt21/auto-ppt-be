## **1. Công nghệ**

1. **HTML, CSS, JS Basic**:

   - **HTML5**: Xây dựng cấu trúc trang.
   - **CSS3**: Sử dụng Flexbox và Grid Layout để tạo bố cục linh hoạt và responsive.
   - **JavaScript**: Quản lý logic phía client như dark/light mode, xử lý sự kiện, hiển thị modal loading, gửi yêu cầu API, và xử lý phản hồi từ backend.

2. **Bootstrap 5**:

   - Cung cấp các thành phần UI như grid, form, modal, buttons, và accordion.
   - Sử dụng class của Bootstrap để tạo giao diện responsive và đồng nhất.

3. **Font Awesome**:

   - Dùng biểu tượng cho nút bấm, liên kết, hoặc các mục trong nav bar và footer.

4. **Hover.css**:

   - Hiệu ứng hover mượt mà cho các nút bấm, liên kết, hoặc danh sách mục.

5. **Animate.css**:
   - Thêm animation khi các phần tử xuất hiện hoặc cuộn trên trang (sử dụng các hiệu ứng như `fadeIn`, `bounce`, `slideInUp`).

---

## **2. index.html**

### **Nav bar**

- **Cấu trúc:**

  - Logo nằm bên trái, liên kết về trang chủ.
  - Các mục menu (`Tạo Bài Giảng Ngay`, `Xem Bài Giảng Đã Tạo`, `Góp Ý Cải Thiện`) nằm bên phải, dùng `ul > li` với class `nav-item` của Bootstrap.
  - Thêm biểu tượng Font Awesome cho từng mục menu để tăng tính trực quan.

- **Tính năng:**
  - Hiệu ứng hover từ **Hover.css** (ví dụ: `hover-grow`, `hover-underline`).
  - Nav bar sẽ chuyển sang dạng hamburger trên thiết bị di động, sử dụng Bootstrap’s responsive nav bar.

### **Main content**

- **Giới thiệu về dự án:**
  - Nội dung giới thiệu được đặt trong một container Bootstrap với:
    - Một cột chứa văn bản (sử dụng hiệu ứng `fadeInUp` từ Animate.css).
    - Một cột chứa hình ảnh minh họa (sử dụng hiệu ứng `zoomIn`).

### **Footer**

- **Cấu trúc:**
  - Chia thành 3 cột:
    1. Thông tin liên hệ (icon + text).
    2. Liên kết nhanh (các mục điều hướng).
    3. Dòng chữ bản quyền (hiển thị năm hiện tại bằng JavaScript).

---

## **3. create-slide.html**

### **Nav bar**

- Giữ giao diện đồng nhất với index.html.

### **Main content**

- **Form upload file:**

  - Form bao gồm:
    - Input `type="file"` để nhận file `.docx`.
    - Nút submit có hiệu ứng hover từ Hover.css.

- **Modal loading:**

  - Khi nhấn nút submit:
    - Hiển thị modal loading (Bootstrap modal) với nội dung:
      - Spinner loading từ Bootstrap hoặc Font Awesome.
      - Thông báo: "Đang xử lý, vui lòng không tắt hoặc chuyển tab."
    - Modal **không thể bị đóng** khi đang xử lý.
  - Modal chỉ được ẩn khi:
    - Phản hồi từ API thành công (hiển thị danh sách slide).
    - Lỗi xảy ra (hiển thị thông báo lỗi và hướng dẫn).

- **Hiển thị nội dung slide:**

  - Khi nhận được `slides_content` từ API `/upload-docx`:
    - Hiển thị nội dung mỗi slide trong một accordion (Bootstrap), với tiêu đề là số thứ tự slide, bên cạnh tiêu đề là nút "Xóa slide" (icon `fa-trash`) để xóa slide đó khỏi danh sách.
    - Bên trong mỗi accordion có một `textarea` để chỉnh sửa nội dung slide.
    - Giữa các slide có nút "Thêm slide" để tạo slide mới (thêm phần tử vào danh sách)

- **Tạo bài giảng:**
  - Nút "Tạo bài giảng" nằm dưới danh sách slide.
  - Khi nhấn:
    - Gửi request tới API `/create-powerpoint` với nội dung slide.
    - Hiển thị modal loading trong khi xử lý.
    - Khi thành công, hiển thị nút "Download bài giảng" với link trả về từ API.
    - Lưu link vào local storage để tiện download sau này.

---

## **4. manage-slide.html**

### **Nav bar**

- Giao diện giống index.html.

### **Main content**

- **Copy toàn bộ link:**

  - JavaScript thu thập tất cả link download từ danh sách, sao chép vào clipboard.
  - Hiển thị thông báo "Copy thành công" bằng alert.

- **Danh sách bài giảng:**

  - Dữ liệu hiển thị dưới dạng bảng (Bootstrap table).
  - Cột gồm:
    1. Tên bài giảng.
    2. Ngày tạo.
    3. Button download (icon `fa-download`).
    4. Button delete (icon `fa-trash`, xác nhận trước khi xóa).
    5. Button copy link download.

- **Nút Copy toàn bộ:**

  - Nút "Copy toàn bộ" nằm dưới bảng.
  - Khi nhấn:
    - Copy toàn bộ link download vào clipboard.
    - Hiển thị thông báo "Copy thành công" bằng modal Bootstrap.

- **Responsive:**
  - Đảm bảo bảng hoạt động tốt trên thiết bị nhỏ.

---

## **5. feedback.html**

### **Nav bar**

- Giao diện giống index.html.

### **Main content**

- **Form góp ý:**

  - Bao gồm:
    - Input `type="text"` cho tên.
    - Input `type="email"` (kiểm tra định dạng email).
    - `textarea` giới hạn 500 ký tự.
    - Button submit với hiệu ứng hover từ Hover.css.

- **Modal loading:**
  - Khi nhấn submit:
    - Hiển thị modal loading với spinner và thông báo: "Đang gửi góp ý, vui lòng chờ..."
    - Gửi thông tin góp ý tới Google Sheet API.
    - Khi thành công hoặc thất bại, hiển thị thông báo tương ứng qua modal.

---

## **6. Dark/Light mode**

### **Cơ chế:**

- JavaScript quản lý trạng thái dark/light mode:
  - Thay đổi class `dark-mode` trên `body`.
  - CSS cung cấp các class riêng cho dark mode.
  - Lưu trạng thái vào `localStorage` và áp dụng khi tải lại trang.

---

## **7. Xử lý lỗi**

### **Toàn hệ thống:**

1. **API lỗi:**

   - Khi xảy ra lỗi, hiển thị thông báo bằng modal Bootstrap.

2. **Dữ liệu không hợp lệ:**

- Kiểm tra tính hợp lệ của dữ liệu trước khi gửi.

---

## **8. Tóm tắt hoạt động**

1. **Upload file:**

   - Gửi file `.docx` tới `/upload-docx`.
   - Hiển thị nội dung slide.

2. **Tạo bài giảng:**

   - Gửi nội dung slide tới `/create-powerpoint`.
   - Nhận link download và hiển thị.

3. **Quản lý bài giảng:**

   - Hiển thị danh sách bài giảng từ local storage.
   - Xóa hoặc copy link bài giảng.

4. **Góp ý:**
   - Gửi dữ liệu tới Google Sheet API.
   - Hiển thị phản hồi thành công hoặc lỗi.
