from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

#Version 1.0
#Made by NDX

# Step 1: Load the RSA private key from file
def load_private_key(filename):
    with open(filename, 'rb') as f:
        private_key = RSA.import_key(f.read())
    return private_key

# Step 2: Decrypt the AES key using the RSA private key
def decrypt_aes_key(private_key, encrypted_aes_key_file, output_file):
    with open(encrypted_aes_key_file, 'rb') as f:
        encrypted_aes_key = f.read()  # Read the encrypted AES key from the file

    cipher = PKCS1_OAEP.new(private_key)  # Create a new cipher object
    decrypted_aes_key = cipher.decrypt(encrypted_aes_key)  # Decrypt the AES key

    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_aes_key)  # Write the decrypted AES key to a file

    # Delete the encrypted AES key file after decryption
    os.remove(encrypted_aes_key_file)  # This will delete the encrypted_aes_key.bin file
    print(f"Deleted the encrypted AES key file '{encrypted_aes_key_file}' after decryption.")

# Step 3: Delete key files
def delete_key_files(private_key_file, public_key_file):
    os.remove(private_key_file)  # This will delete the private_key.pem file
    os.remove(public_key_file)    # This will delete the public_key.pem file
    print(f"Deleted key files '{private_key_file}' and '{public_key_file}' after decryption.")

# Main execution
if __name__ == "__main__":
    private_key_file = 'private_key.pem'
    public_key_file = 'public_key.pem'

    # Load the RSA private key
    private_key = load_private_key(private_key_file)

    # Decrypt the AES key
    decrypt_aes_key(private_key, 'encrypted_aes_key.bin', 'decrypted_aes_key.txt')

    # Delete key files after decryption
    delete_key_files(private_key_file, public_key_file)

    print("AES key decrypted and saved to 'decrypted_aes_key.txt'.")
