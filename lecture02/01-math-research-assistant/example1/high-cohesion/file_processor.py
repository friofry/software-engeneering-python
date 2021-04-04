from io import BytesIO
from hashlib import md5
from typing import List
from file_repo import FileRepoABC


class FileProcessor:
    def __init__(self, repo: FileRepoABC, path: str) -> None:
        self.repo = repo
        self.path = path

    def run(self) -> List[str]:
        return [self.process_file(file) for file in self.repo.get_files(self.path)]

    def process_file(self, fd: BytesIO) -> str:
        return md5(fd.getvalue()).hexdigest()
