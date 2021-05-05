from mail_service_abc import *

# LSP


class SendGridEmailService(IMailService):
    def send_mail(self, email: IMail) -> IEmailTransmissionResult:
        # use SendGrid API
        pass


class MailChimpEmailService(IMailService):
    def send_mail(self, email: IMail) -> IEmailTransmissionResult:
        # use MailChimp API
        pass


class MailGunEmailService(IMailService):
    def send_mail(self, email: IMail) -> IEmailTransmissionResult:
        # use MailGun API
        pass

