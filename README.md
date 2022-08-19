# diary-backup is a backup solution for WriteDiary
The purpose of this project is to backup any diary from WriteDiary.com, encrypt it and then put it somewhere safe.

First a 'diary_pass' environment variable should be set. You should store this somewhere else safe. Personally I store mine in my preferred locked password manager 1Password.

Whenever you wish to take a backup (should be about every 6 months), follow these steps:

1. Login to writediary.com, and paste the script in 'script.js' into the web developer console.
2. Move the 'diary_backup.json' generated in download folder into this project. Make sure to delete the 'diary_backup'.json from your download folder.
3. Run 'encrypt.py' and when finished, put the newly generated encrypted file somewhere safe. Personally I use Google Drive (however since a diary is so personal, these extra encryption steps are taken)
DISCLAIMER: Make sure that the folder is actually able to be decrypted, and that the text itself is intact.

In the rare scenario that you would wish to decrypt your diary backup, please put the '.aes' backup in this path and run 'decrypt.py' and provide the file name of the desired backup.

## Prerequisites
* Python 3
* pyAesCrypt

Finally, the WriteDiary infrastructure is subject to change, or anything else could happen. I can't guarantee that this project will always work.

by wakils