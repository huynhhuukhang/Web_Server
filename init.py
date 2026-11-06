import os

def check_environment():
    print("Đang kiểm tra môi trường hệ thống...")
    
    # Kiểm tra thư mục configs và file cấu hình
    if not os.path.exists("configs/pc1.conf"):
        print("Tạo thư mục configs và file pc1.conf mẫu...")
        os.makedirs("configs", exist_ok=True)
        with open("configs/pc1.conf", "w", encoding="utf-8") as f:
            f.write("[SERVER]\nhost = 127.0.0.1\nport = 8080\ndocument_root = ./public\n")
            
    # Kiểm tra thư mục public và file index.html
    if not os.path.exists("public"):
        print("Tạo thư mục public và trang index.html mẫu...")
        os.makedirs("public", exist_ok=True)
        with open("public/index.html", "w", encoding="utf-8") as f:
            f.write("<h1>Chào mừng bạn đến với Web Server thuần Python!</h1>")
            
    print("Môi trường đã sẵn sàng!")

if __name__ == "__main__":
    check_environment()