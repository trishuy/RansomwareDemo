from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os


#Version 1.0
#Made by NDX

# Step 1: Generate RSA key pair
def generate_rsa_key_pair(key_size=2048):
    private_key = RSA.generate(key_size)
    public_key = private_key.publickey()
    return private_key, public_key

# Step 2: Save the private key to a file
def save_private_key(private_key, filename):
    with open(filename, 'wb') as f:
        f.write(private_key.export_key())

# Step 3: Save the public key to a file
def save_public_key(public_key, filename):
    with open(filename, 'wb') as f:
        f.write(public_key.export_key())

# Step 4: Encrypt the AES key using the RSA public key
def encrypt_aes_key(public_key, aes_key_file, output_file):
    with open(aes_key_file, 'rb') as f:
        aes_key = f.read()  # Read the AES key from the file

    cipher = PKCS1_OAEP.new(public_key)  # Create a new cipher object
    encrypted_aes_key = cipher.encrypt(aes_key)  # Encrypt the AES key

    with open(output_file, 'wb') as f_out:
        f_out.write(encrypted_aes_key)  # Write the encrypted AES key to a file

    # Delete the AES key file after encryption
    os.remove(aes_key_file)  # This will delete the aes_key.txt file
    print(f"Deleted the AES key file '{aes_key_file}' after encryption.")

# Main execution
if __name__ == "__main__":
    # Generate RSA key pair
    private_key, public_key = generate_rsa_key_pair()

    # Save the keys to files
    save_private_key(private_key, 'private_key.pem')
    save_public_key(public_key, 'public_key.pem')

    print("RSA key pair generated and saved to 'private_key.pem' and 'public_key.pem'.")

    # Encrypt the AES key
    encrypt_aes_key(public_key, 'aes_key.txt', 'encrypted_aes_key.bin')

    print("AES key encrypted and saved to 'encrypted_aes_key.bin'.")
