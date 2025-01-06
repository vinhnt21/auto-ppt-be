
# Dự án Flask - Cấu trúc File và Tác Dụng Từng File
```
│
├── app.py                 # File chính, định nghĩa routes và API endpoints
├── env_config.py          # Quản lý biến môi trường
├── gunicorn_config.py     
├── requirements.txt       
├── .env                   
├── .gitignore            
│
├── services/              
│   ├── __init__.py
│   ├── slides_service.py  # Logic chung cho việc tạo slides
│   └── subject_handlers/  # Xử lý riêng cho từng môn học
│       ├── __init__.py
│       ├── base_handler.py    # Class cơ sở cho các handler
│       ├── math_handler.py    
│       ├── literature_handler.py
│       └── civics_handler.py
│
├── utils/                 
│   ├── ai/               
│   │   ├── __init__.py
│   │   ├── models.py     
│   │   ├── base_prompts.py    # Prompts cơ bản
│   │   └── subject_prompts/    # Tách prompts theo môn
│   │       ├── __init__.py
│   │       ├── math_prompts.py
│   │       ├── literature_prompts.py
│   │       └── civics_prompts.py
│   │
│   ├── file_handlers/     
│   │   ├── __init__.py
│   │   ├── docx_handler.py       
│   │   └── pdf_handler.py        
│   │
│   └── slides/           
│       ├── __init__.py
│       ├── slide_generator.py  # Logic tạo slides
│
└── uploads/             # Thư mục lưu file upload
```