import os, json, shutil, pyAesCrypt, datetime

TEMP_PATH = 'temp/'
BACKUP_PATH = "diary_backup.json"
CURRENT_TIME = datetime.datetime.now().strftime('%Y_%m_%d')
diary_pass = os.getenv('diary_pass')

def prepare():
	if not os.path.isfile(BACKUP_PATH):
		print(f"'{BACKUP_PATH}' was not found.")
		exit()

	if not diary_pass:
		print("No environment variable called 'diary_pass' was found. Exiting...")
		exit()

	if os.path.isdir(TEMP_PATH):
		shutil.rmtree(TEMP_PATH, ignore_errors=True)

	os.mkdir(TEMP_PATH)

def create_entry(entry):
	FILE_NAME = "note_" + entry['date']
	f = open(TEMP_PATH + FILE_NAME + ".txt", "w+", encoding="utf-8")
	f.write(f"{entry['title']}\n{entry['date']}\n\n{entry['body']}")
	f.close()

def encrypt():
	shutil.make_archive("temp", 'zip', TEMP_PATH)
	pyAesCrypt.encryptFile("temp.zip", f"diary_backup_{CURRENT_TIME}.zip.aes", diary_pass)

def cleanup():
	os.remove("temp.zip")
	shutil.rmtree(TEMP_PATH, ignore_errors=True)

prepare()

f = open(BACKUP_PATH, encoding="utf-8")
diary = json.load(f)
print(f"Succesfully loaded {len(diary)} entries in diary backup taken at the following date: {CURRENT_TIME}")

for entry in diary:
	create_entry(entry)

f.close()
shutil.move(BACKUP_PATH, TEMP_PATH)

print("Encrypting all files now...")
encrypt()

cleanup()
print("Succesfully finished everything. Please refer to the instructions in 'README.md'.")