from mail_service_abc import *


class BaseController(ABC):
    pass
    # ... some interface here


class Mail(IMail):
    pass
    # ... implementation here


class CreateUserController(BaseController):
    def __init__(self, email_service: IMailService):     # Dependency Injection
        self.email_service = email_service  # MailChimp, MailGun, SendGrid ? Doesn't matter (LSP)

    def create(self) -> None:
        # new user request

        # create mail box, send greeting email
        mail = Mail()
        self.email_service.send_mail(mail)
