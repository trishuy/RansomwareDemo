import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# Step 1: Load the AES key from the specified files
def load_aes_key(key_files):
    for key_file in key_files:
        if os.path.exists(key_file):
            with open(key_file, 'r') as f_key_in:
                key_hex = f_key_in.read()
                key = binascii.unhexlify(key_hex)  # Convert hex back to bytes
            print(f"AES key loaded from '{key_file}'.")
            return key
    raise FileNotFoundError("No valid AES key file found.")

# Step 2: Decrypt the file contents using the AES key
def aes_decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f_in:
        iv = f_in.read(16)  # Read the IV (first 16 bytes)
        ciphertext = f_in.read()  # Read the rest of the file (the ciphertext)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and unpad
    
    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_text)

# Directories to decrypt
directories_to_decrypt = [
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Downloads"),
    "D:\\",  # Additional drives, modify as needed
    "E:\\"
]

# Decrypt all encrypted files in a folder
def decrypt_all_files_in_folder(key, folder_path):
    # Traverse all files in the directory
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # Check if the file is encrypted (ends with .aes)
            if filename.lower().endswith('.aes'):
                input_file = os.path.join(root, filename)
                output_file = os.path.join(root, filename[:-4])  # Remove the .aes extension for the output file
                print(f"Decrypting '{input_file}'...")
                aes_decrypt_file(key, input_file, output_file)
                print(f"File '{input_file}' decrypted to '{output_file}'.")

# Example usage
if __name__ == "__main__":
    # Step 1: Load AES key from files
    key_files = ['decrypted_aes_key.txt', 'aes_key.txt']  # List of key files to check
    try:
        key = load_aes_key(key_files)

        # Step 2: Decrypt specified directories
        for directory in directories_to_decrypt:
            print(f"Decrypting files in '{directory}'...")
            decrypt_all_files_in_folder(key, directory)
        
        print("Decryption process completed.")
    except FileNotFoundError as e:
        print(e)
