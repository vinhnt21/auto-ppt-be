# Kiểm tra các package đã cài đặt
pip list

# Freeze requirements
pip freeze > requirements.txt


---

# Tạo venv trong thư mục venv
python -m venv venv

# Kích hoạt venv (Windows)
venv\Scripts\activate

# Kích hoạt venv (Linux)
source venv/bin/activate


# Cài đặt các package từ requirements.txt
pip install -r requirements.txt


# Run app 
python app.py