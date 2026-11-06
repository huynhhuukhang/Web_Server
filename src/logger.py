import datetime
import os

def log_request(client_address, path):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "access.log")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] - Client: {client_address[0]} - Requested: {path}\n"
    
    # Ghi log ra file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    print(log_entry.strip())