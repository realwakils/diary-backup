import pyAesCrypt, os

diary_pass = os.getenv('diary_pass')
if not diary_pass:
	print("No environment variable called 'diary_pass' was found. Exiting...")
	exit()

file_name = input("Please provide the file name of the diary backup you wish to decrypt: ")
if not os.path.isfile(file_name):
	print("Could not find backup file. Please make sure that the file is actually in this path.")
	exit()

new_file_name = file_name.replace('aes', '')
pyAesCrypt.decryptFile(file_name, new_file_name, diary_pass)
# os.remove(file_name)
print(f"Succesfully decrypted '{new_file_name}'.")