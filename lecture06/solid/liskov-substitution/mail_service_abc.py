from enum import Enum
from abc import ABC, abstractmethod


class IMail(ABC):
    pass


class TransmissionResult(Enum):
    SUCCESS = 1
    FAILURE = 2
    BOUNCED = 3


class IEmailTransmissionResult(ABC):
    @abstractmethod
    def result(self) -> TransmissionResult:
        pass

    @abstractmethod
    def message(self) -> str:
        pass


class IMailService(ABC):
    @abstractmethod
    def send_mail(self, email: IMail) -> IEmailTransmissionResult:
        # send email
        pass

