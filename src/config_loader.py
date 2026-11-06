import configparser
import os

class ConfigLoader:
    def __init__(self, config_path="configs/pc1.conf"):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.load()

    def load(self):
        if os.path.exists(self.config_path):
            self.config.read(self.config_path, encoding="utf-8")
        else:
            raise FileNotFoundError(f"Không tìm thấy file cấu hình tại: {self.config_path}")

    @property
    def host(self):
        return self.config.get("SERVER", "host", fallback="127.0.0.1")

    @property
    def port(self):
        return self.config.getint("SERVER", "port", fallback=8080)

    @property
    def document_root(self):
        return self.config.get("SERVER", "document_root", fallback="./public")