from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from eyca.models import Profile
from registration.models import Registration
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import os

@receiver(post_save, sender=Registration)
def send_email_on_new_registration(sender, instance, created, **kwargs):
    user_name = instance.name
    user_email = instance.email

    staff_users = User.objects.filter(is_staff=True)
    staff_email_list = [staff_user.email for staff_user in staff_users]

    if created == True:
        print("NEW REGISTRATION")
        instance.save()
        send_registration_submit_email(user_name, user_email, staff_email_list)


@receiver(post_save, sender=Registration)
def check_if_approved(sender, instance, created, **kwargs):
    user_username = instance.username
    user_name = instance.name
    user_email = instance.email

    staff_users = User.objects.filter(is_staff=True)
    staff_email_list = [staff_user.email for staff_user in staff_users]

    if instance.approve_registration == True:
        print("YOU ARE AN EYCA NOW")

        name = instance.name.split()
        new_user = User()
        new_user.email = instance.email
        new_user.username = instance.username
        new_user.first_name = name[0]
        new_user.last_name = name[-1]
        new_user.set_unusable_password()
        new_user.is_active = True
        new_user.save()

        new_user_profile = Profile()
        new_user_profile.user = new_user
        new_user_profile.profile_pic = instance.profile_pic
        new_user_profile.college = instance.college
        new_user_profile.course = instance.course
        new_user_profile.department = instance.department
        new_user_profile.year = instance.year
        new_user_profile.dob = instance.dob
        new_user_profile.phone_number = instance.phone_number
        new_user_profile.save()

        instance.delete()

        user_code = urlsafe_base64_encode(force_bytes(new_user.pk))
        user_token = default_token_generator.make_token(new_user)
        domain = Site.objects.get_current().domain

        set_password_link = domain + "/reset/" + user_code + "/" + user_token

        print(user_code)
        print(user_token)

        send_registration_approved_email(user_name, user_email, user_username, set_password_link, staff_email_list)

        print("SENT MAILS")


@receiver(post_delete, sender=Registration)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Registration' object is deleted.
    """
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)

    if instance.id_card_pic:
        if os.path.isfile(instance.id_card_pic.path):
            os.remove(instance.id_card_pic.path)


@receiver(pre_save, sender=Registration)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding 'Registration' object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_profile_pic = Registration.objects.get(pk=instance.pk).profile_pic
        old_id_card_pic = Registration.objects.get(pk=instance.pk).id_card_pic
    except Registration.DoesNotExist:
        return False

    new_profile_pic = instance.profile_pic
    new_id_card_pic = instance.id_card_pic

    if not old_profile_pic == new_profile_pic:
        if os.path.isfile(old_profile_pic.path):
            os.remove(old_profile_pic.path)

    if not old_id_card_pic == new_id_card_pic:
        if os.path.isfile(old_id_card_pic.path):
            os.remove(old_id_card_pic.path)


def send_registration_submit_email(user_name, user_email, staff_email_list):

    context = {
        'name': user_name
    }

    text_content = render_to_string('registration/email/registration_initiated.txt', context=context)
    html_content = render_to_string('registration/email/registration_initiated.html', context=context)
    user_new_registration = EmailMultiAlternatives(
        'eYCA Registration',
        text_content,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    user_new_registration.attach_alternative(html_content, "text/html")
    user_new_registration.send(fail_silently=False)

    staff_new_registration = EmailMessage(
        'eYCA Registration',
        'Recieved a new registration for eYCA. Check the admin panel for more details.',
        settings.EMAIL_HOST_USER,
        staff_email_list,
    )
    staff_new_registration.send(fail_silently=False)


def send_registration_approved_email(user_name, user_email, user_username, set_password_link, staff_email_list):
    context = {
        'name': user_name,
        'username': user_username,
        'set_password_link': set_password_link
    }

    text_content = render_to_string('registration/email/registration_approved.txt', context=context)
    html_content = render_to_string('registration/email/registration_approved.html', context=context)
    user_new_registration = EmailMultiAlternatives(
        'eYCA Registration',
        text_content,
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    user_new_registration.attach_alternative(html_content, "text/html")
    user_new_registration.send(fail_silently=False)

    staff_new_registration = EmailMessage(
        'eYCA Registration',
        'A new campus ambassador has been added',
        settings.EMAIL_HOST_USER,
        staff_email_list,
    )
    staff_new_registration.send(fail_silently=False)
