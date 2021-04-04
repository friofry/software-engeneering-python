from io import BytesIO
from hashlib import md5
from gcloud import storage
from typing import Iterable
from file_repo import FileRepoABC


class GCSFileRepo(FileRepoABC):
    def __init__(self, credentials_path: str, bucket_name: str) -> None:
        self.bucket_name = bucket_name
        self._client = storage.Client.from_service_account_json(json_credentials_file=credentials_path)
        self.bucket = self._client.get_bucket(self.bucket_name)

    def get_files(self, path: str) -> Iterable[BytesIO]:
        for blob in self.bucket.list_blobs():
            with BytesIO() as bio:
                blob.download_to_file(bio)
                yield bio
