import dropbox

class TransferData:
        def __init__(self,access_token):
            self.access_token = access_token

        def upload_file(self,file_from,file_to):
            dbx = dropbox.Dropbox(self.access_token)
        
def main():
    access_token = 'sl.BQZvTkzBJ3UuRnHAtFmKzupHOKI0t4lhGhzhZZ-p_IF7Jz0bySRzbTAMnOeQ2x7ZJqZ5sY8PkGZYsOkLZpL5nBvCkyDl_tWIg4bwrjxtKYRq1BKJsKLgPgsd8JVZ7i5DdmdYAnI'
    transferData = TransferData(access_token)

    file_from = input("C:/Users/vedhe/OneDrive/Desktop/whjpro/demo.txt")
    file_to = input("/demo/demo.txt")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()