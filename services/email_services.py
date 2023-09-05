import threading
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


def send_email_activate_otp(user, otp):
    subject = "Activate Email"
    data = {"otp": otp, "name": f"{user.first_name} {user.last_name}"}
    message = get_template("mail/send_email_activation_otp.html").render(data)

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
        reply_to=[settings.DEFAULT_FROM_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def send_email_forgot_password_otp(otp):
    subject = "Forgot Password Email"
    data = {"name": f'{otp.user.first_name} {otp.user.last_name}', "otp": otp.otp}
    message = get_template("mail/send_forgot_password_email.html").render(data)
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[otp.user.email],
        reply_to=[settings.DEFAULT_FROM_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def sender_to_admin(obj):
    data = {"obj": obj, "name": obj.name}
    message = get_template("mail/sender_to admin.html").render(data)
    subject = obj.subject
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=obj.email,
        to=[settings.ADMIN_SUPPORT_EMAIL],
        reply_to=[obj.email],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def admin_to_sender(obj):
    data = {"obj": obj, "name": obj.name}
    message = get_template("mail/admin_to_sender.html").render(data)

    mail = EmailMessage(
        subject="Thank You for Contacting Us!",
        body=message,
        from_email=settings.ADMIN_SUPPORT_EMAIL,
        to=[obj.email],
        reply_to=[settings.ADMIN_SUPPORT_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def payment_confirmation(user_obj, plan_obj, transaction_id):
    data = {
        "user_obj": user_obj,
        "name": f"{user_obj.user.first_name} {user_obj.user.last_name}",
        "plan_obj": plan_obj,
        "transaction_id":transaction_id
    }
    message = get_template("mail/plan_confirmation.html").render(data)

    mail = EmailMessage(
        subject="Purchase Plan Confirmation",
        body=message,
        from_email=settings.ADMIN_SUPPORT_EMAIL,
        to=[user_obj.user.email],
        reply_to=[settings.ADMIN_SUPPORT_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def cancel_subscription(user_obj ,plan_obj):
    data = {
        "user_obj": user_obj,
        "name": f"{user_obj.user.first_name} {user_obj.user.last_name}",
        "plan_obj": plan_obj,
    }
    message = get_template("mail/cancel_subscription.html").render(data)

    mail = EmailMessage(
        subject="Subscription Cancelled",
        body=message,
        from_email=settings.ADMIN_SUPPORT_EMAIL,
        to=[user_obj.user.email],
        reply_to=[settings.ADMIN_SUPPORT_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()


def payment_failed(user_obj, plan_obj):
    data = {
        "user_obj": user_obj,
        "name": f"{user_obj.user.first_name} {user_obj.user.last_name}",
        "plan_obj": plan_obj
    }
    message = get_template("mail/payment_failed.html").render(data)

    mail = EmailMessage(
        subject="Payment Failed for Subscription",
        body=message,
        from_email=settings.ADMIN_SUPPORT_EMAIL,
        to=[user_obj.user.email],
        reply_to=[settings.ADMIN_SUPPORT_EMAIL],
    )
    mail.content_subtype = "html"

    def send_email_thread(mail):
        mail.send()

    threading.Thread(target=send_email_thread, args=(mail,)).start()
