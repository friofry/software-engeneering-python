from file_processor import FileProcessor
from gcs_repo import GCSFileRepo

APPLICATION_CREDENTIALS_PATH = "./credentials.json"
BUCKET_NAME = "some_bucket"


def main():
    repo = GCSFileRepo(APPLICATION_CREDENTIALS_PATH, BUCKET_NAME)
    processor = FileProcessor(repo, "some/path")
    hashes = processor.run()
    # ...

if __name__ == "__main__":
    main()