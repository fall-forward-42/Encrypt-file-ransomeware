import os
from cryptography.fernet import Fernet


# Directory paths
encrypted_folder = "encrypted"
decrypted_folder = "decrypted"

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def decrypt_folder():
    # Read the secret key from the file
    key_file = "Secret.key"
    if not os.path.exists(key_file):
        print("[ERROR] File 'secret.key' does not exist.")
        return
    with open(key_file, 'rb') as f:
        key = f.read()
    if key is None or len(key)==0:
        print("[ERROR] File 'Secret.key' is empty or contains null.")
        return

    print("[TODO] Handling decrypt all of files...")
    # Create the "decrypted" folder if it doesn't exist
    if not os.path.exists(decrypted_folder):
        os.makedirs(decrypted_folder)

    # Decrypt files in the "encrypted" folder and save them in the "decrypted" folder
    for root, dirs, files in os.walk(encrypted_folder):
        for file in files:
            file_path = os.path.join(root, file)
            decrypted_data = decrypt_file(file_path, key)

            if ".lihitiEncrypted" in file:
                new_file_name = file.replace(".lihitiEncrypted", ".lihitiDecrypted")
            decrypted_file_path = os.path.join(decrypted_folder, new_file_name)
            
            with open(decrypted_file_path, 'wb') as f:
                f.write(decrypted_data)
    print("[COMPLETED] Decryption of files completed successfully, please check in decrypted folder !")

decrypt_folder()