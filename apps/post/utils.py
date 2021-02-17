from django.core.mail import send_mail


def send_activation_mail(email, text):
    print(text)
    subject = 'Your wishes'
    message = f"""Здравствуйте Уважаемый Пользователь.\n
     Спасибо за ваш отзыв!
     """

    from_ = 'test@gmail.com'
    emails = [email, ]

    send_mail(subject, message, from_, emails)