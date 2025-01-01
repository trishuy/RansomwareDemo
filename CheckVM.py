import platform
import subprocess
import os
import glob

def check_virtualization_windows():
    try:
        # Sử dụng lệnh systeminfo
        output = subprocess.check_output("systeminfo", shell=True, text=True)
        if "Hyper-V Requirements" in output or "VMware" in output or "VirtualBox" in output:
            return True
        return False
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return False

def delete_specific_files(directory):
    try:
        # Danh sách các đuôi tệp cần xóa
        extensions = ['*.exe', '*.py', '*.bat', '*.ps1']
        for ext in extensions:
            files = glob.glob(os.path.join(directory, ext))
            for file_path in files:
                os.remove(file_path)
                print(f"Đã xóa tệp: {file_path}")
            if not files:
                print(f"Không tìm thấy tệp {ext} nào để xóa.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi xóa tệp: {e}")

if __name__ == "__main__":
    directory_to_search = "path_to_your_directory"  # Thay thế bằng đường dẫn thư mục bạn muốn tìm kiếm

    if check_virtualization_windows():
        print("Máy tính là máy ảo. Đang xóa tất cả các tệp .exe, .py, .bat, và .ps1 trong thư mục...")
        delete_specific_files(directory_to_search)
    else:
        print("Máy tính không phải là máy ảo.")
