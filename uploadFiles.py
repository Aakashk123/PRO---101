import os
import dropbox 
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
#
    def upload_file(self, file_form, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'urYwtkP6GMQAAAAAAAAAAVSmpXsSTR5P5QKwBuOpPkn5F7i10ZUSTCYuUQ7H-pnU'
    transferData = TransferData(access_token)

    file_form = str(input("Enter The Folder Path To Transfer: "))
    file_to = input("Enter The Full Path To Upload To Dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved !!!")

main()    
             