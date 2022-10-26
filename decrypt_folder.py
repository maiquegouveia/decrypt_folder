from cryptography.fernet import Fernet
import os

def getFiles(dir_path):
    paths = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            paths.append(path)
    return paths

def decryptFiles():
    dir_path = input("Enter dir path: ")
    paths = getFiles(dir_path)
    key_file = input("Enter decrypt key file path: ")

    with open(key_file, 'rb') as file:
        key = file.read()

    f = Fernet(key)

    for path in paths:
        file_to_decrypt = dir_path + '//' + path
        with open(file_to_decrypt, 'rb') as fencrypted:
            encrypted_file = fencrypted.read()
        decrypted_file = f.decrypt(encrypted_file)
        try:
            with open(file_to_decrypt, 'wb') as fencrypted:
                fencrypted.write(decrypted_file)
        except:
            pass

decryptFiles()
