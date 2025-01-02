# Tôi cần deploy 1 web app lên vps

- Backend: Python Flask
  - 1 số API có thời gian xử lý lâu ~ 10 phút
  - khống có database
  - Tuy nhiên, không cần xử lý nhiều request cùng lúc tối đa 10 request
  - Repo: https://github.com/vinhnt21/auto-ppt-be.git (public)
- Frontend: HTML, CSS, JS Bootstrap
  - Call API từ backend
  - Repo: https://github.com/vinhnt21/auto-ppt-fe.git (public)
- Domain: aiquickerslides.com
- VPS:
  - IP: 103.82.196.220
  - 2 Core, 2GB RAM, 30GB SSD
  - OS: Debian 6.1.119
- Không cần backup

## Ngoài ra tôi cần deploy 1 web tĩnh trên cùng 1 VPS với web app trên

- Frontend: HTML, CSS, JS Bootstrap
- Domain: baotanglichsuvietnam.com
- Repo: https://github.com/noname14-2/lichsudaklak-main.git

## Yêu cầu

- Cài đặt web app trên VPS, sử dụng Nginx, Gunicorn
- Chưa cần SSL
- Log error cơ bản

# Nhiệm vụ

- Cung cấp cho tôi hướng dẫn chi tiết triển khai phù hợp với cấu hình VPS và yêu cầu

---

Tôi sẽ hướng dẫn bạn từng bước để deploy cả 2 website lên VPS. Hãy thực hiện theo thứ tự sau:

1. Chuẩn bị môi trường trên VPS

# Cập nhật hệ thống

sudo apt update
sudo apt upgrade -y

# Cài đặt các công cụ cần thiết

sudo apt install -y python3 python3-pip python3-venv git nginx

# Tạo thư mục cho các ứng dụng

sudo mkdir -p /var/www/aiquickerslides
sudo mkdir -p /var/www/baotanglichsuvietnam

2. Cài đặt Auto PPT Web App

# Clone repositories

cd /var/www/aiquickerslides
git clone https://github.com/vinhnt21/auto-ppt-be.git backend
git clone https://github.com/vinhnt21/auto-ppt-fe.git frontend

# Thiết lập môi trường cho backend

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Tạo file gunicorn config

sudo nano /etc/systemd/system/autoppt.service

Nội dung file autoppt.service:
[Unit]
Description=Auto PPT Gunicorn Service
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/aiquickerslides/backend
Environment="PATH=/var/www/aiquickerslides/backend/venv/bin"
ExecStart=/var/www/aiquickerslides/backend/venv/bin/gunicorn --workers 3 --timeout 600 --bind unix:autoppt.sock -m 007 app:app

[Install]
WantedBy=multi-user.target

3. Cài đặt Website Tĩnh

# Clone repository

cd /var/www/baotanglichsuvietnam
git clone https://github.com/noname14-2/lichsudaklak-main.git .

4. Cấu hình Nginx

# Tạo config cho Auto PPT

sudo nano /etc/nginx/sites-available/aiquickerslides

Nội dung file aiquickerslides:
server {
listen 80;
server_name aiquickerslides.com;

    # Frontend
    location / {
        root /var/www/aiquickerslides/frontend;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api {
        proxy_pass http://unix:/var/www/aiquickerslides/backend/autoppt.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_connect_timeout 600;
        proxy_send_timeout 600;
        proxy_read_timeout 600;
    }

    # Basic error logging
    error_log /var/log/nginx/aiquickerslides_error.log;
    access_log /var/log/nginx/aiquickerslides_access.log;

}

# Tạo config cho Website Tĩnh

sudo nano /etc/nginx/sites-available/baotanglichsuvietnam

Nội dung file baotanglichsuvietnam:
server {
listen 80;
server_name baotanglichsuvietnam.com;

    root /var/www/baotanglichsuvietnam;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Basic error logging
    error_log /var/log/nginx/baotanglichsuvietnam_error.log;
    access_log /var/log/nginx/baotanglichsuvietnam_access.log;

}

5. Kích hoạt các cấu hình

# Kích hoạt các site

sudo ln -s /etc/nginx/sites-available/aiquickerslides /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/baotanglichsuvietnam /etc/nginx/sites-enabled/

# Kiểm tra cấu hình Nginx

sudo nginx -t

# Khởi động các service

sudo systemctl start autoppt
sudo systemctl enable autoppt
sudo systemctl restart nginx

# Kiểm tra trạng thái

sudo systemctl status autoppt
sudo systemctl status nginx

6. Cấu hình DNS
   Trỏ các domain về IP của VPS (103.82.196.220):

aiquickerslides.com -> A record -> 103.82.196.220
baotanglichsuvietnam.com -> A record -> 103.82.196.220

Lưu ý quan trọng:

Gunicorn được cấu hình với:

3 workers phù hợp với 2 CPU cores
Timeout 600s (10 phút) cho các API xử lý lâu
Unix socket để giao tiếp với Nginx

Nginx được cấu hình với:

Timeout tương ứng cho các request dài
Log cơ bản được lưu tại /var/log/nginx/

Để theo dõi lỗi:

Backend: sudo journalctl -u autoppt
Nginx: /var/log/nginx/error.log

Nếu cần restart services:

sudo systemctl restart autoppt
sudo systemctl restart nginx

Bạn có thể kiểm tra các website bằng cách truy cập:

http://aiquickerslides.com
http://baotanglichsuvietnam.com
