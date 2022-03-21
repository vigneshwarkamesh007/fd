import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEM8TjK5SiDO1F-ml6MRaTocKpCb3Yld7Ay8KUolFIfM6J-W613QmbYGKRbPmji-YGw-lRsm1yXf7LFg4eHDzP_ugE0rryq0ad0dZi1vdJBZaU4DOVVN4oOCgQ-jkseuq8egxQQIWw7a'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to) 

if __name__ == '__main__':
    main()
