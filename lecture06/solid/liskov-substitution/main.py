from email_services import *
from create_user_controller import CreateUserController

# entry point


def main():
    # 1. Three IMailService implementations:

    mail_gun_service = MailGunEmailService()
    mail_chimp_service = MailChimpEmailService()
    send_grid_service = SendGridEmailService()

    # 2. New User controller:
    create_user_controller = CreateUserController(send_grid_service)    # First Task

    # create_user_controller = CreateUserController(mail_chimp_service)  # Boss changed his mind
    # create_user_controller = CreateUserController(mail_gun_service)    # Another feature request

    # 3. Conclusion:
    # Because we can interchange which implementation of an IEmailService we pass in, we're adhering to LSP.


# python -m main.py
if __name__ == "__main__":
    main()