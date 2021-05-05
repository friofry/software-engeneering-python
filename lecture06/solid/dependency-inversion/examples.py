# try not to do this:
class EmailWithAttachment:
    pass
    # implementation


class EmailWithAttachmentTransmissionResult:
    pass
    # some details


# Tight coupling. Dependency inversion violation. Not abstract :( Is this an interface at all?
class IMailService:
    def send_mail(self, email: EmailWithAttachment) -> EmailWithAttachmentTransmissionResult:
        # send email
        pass


# Instead, do this


# Low coupling: because IMail, IEmailTransmissionResult are abstract
class SendGridEmailService(IMailService):
    def send_mail(self, email: IMail) -> IEmailTransmissionResult:
        # concrete class relies on abstractions
        pass

