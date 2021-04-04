from io import BytesIO
from hashlib import md5
from gcloud import storage

APPLICATION_CREDENTIALS_PATH = './credentials.json'


class FileProcessor:
    def __init__(self, resource_path):
        self.resource_path = resource_path
        self.client = storage.Client.from_service_account_json(json_credentials_file=APPLICATION_CREDENTIALS_PATH)
        self.bucket = self.client.get_bucket(self.resource_path)

    def run(self):
        return [self.process_blob(blob) for blob in self.bucket.list_blobs()]

    def process_blob(self, blob):
        with BytesIO() as blob_contents:
            blob.download_to_file(blob_contents)
            return md5(blob_contents.getvalue()).hexdigest()
