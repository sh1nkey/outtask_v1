from allauth.account.adapter import DefaultAccountAdapter

class CustomEmailConfirmationAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation):
        # Ваш код для изменения сообщения отправляемого на почту
        # Можете использовать emailconfirmation.email_address.user и emailconfirmation.key для доступа к информации об адресе электронной почты и ключу подтверждения

        # Пример:
        subject = "Подтверждение адреса электронной почты"
        message = f"Пожалуйста, подтвердите ваш адрес электронной почты. Ссылка для подтверждения: {emailconfirmation.confirmation_url(request)}"
        self.send_mail(subject, message, emailconfirmation.email_address.email)