from abc import ABC, abstractmethod
from io import BytesIO
from typing import Iterable


class FileRepoABC(ABC):
    @abstractmethod
    def get_files(self, path: str) -> Iterable[BytesIO]:
        pass
