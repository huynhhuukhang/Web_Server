import configparser
import os
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

def load_config(config_path="configs/pc1.conf"):
    config = configparser.ConfigParser()
    if os.path.exists(config_path):
        config.read(config_path, encoding="utf-8")
        host = config.get("SERVER", "host", fallback="127.0.0.1")
        port = config.getint("SERVER", "port", fallback=8080)
        doc_root = config.get("SERVER", "document_root", fallback="./public")
        return host, port, doc_root
    else:
        raise FileNotFoundError(f"Không tìm thấy file cấu hình: {config_path}")

def run():
    host, port, server_dir = load_config()
    
    # Đảm bảo thư mục web tồn tại
    os.makedirs(server_dir, exist_ok=True)

    class CustomHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=server_dir, **kwargs)

        def log_message(self, format, *args):
            # Tự động ghi log vào thư mục logs/access.log và hiển thị ra màn hình
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, "access.log")
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = format % args
            log_entry = f"[{timestamp}] - Client: {self.client_address[0]} - {message}\n"
            
            try:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)
            except Exception as e:
                print(f"Lỗi ghi log: {e}")
                
            # In ra terminal
            print(log_entry.strip())

    server_address = (host, port)
    httpd = HTTPServer(server_address, CustomHandler)
    
    print(f"Web Server đang chạy tại: http://{host}:{port}")
    print(f"Đang đọc dữ liệu từ thư mục: {server_dir}")
    print("Nhấn Ctrl + C để dừng server.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã tắt server.")
        httpd.server_close()

if __name__ == "__main__":
    run()