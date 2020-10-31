from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from eyca.models import Profile
from registration.models import Registration
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from PIL import Image
from resizeimage import resizeimage
from django.core.files.base import ContentFile

#
# @receiver(post_save, sender=Registration)
# def resize_profile_pic(sender, instance, created, **kwargs):
#     img = Image.open(settings.BASE_DIR + instance.profile_pic.url)
#     height, width = img.size
#     img = resizeimage.resize_contain(img, [250, 250], bg_color=(255, 255, 255, 1))
#     if width < height:
#         img = img.rotate(90)
#     instance.profile_pic.save(instance.name+"_profile_pic.jpeg", , save=False)
#     instance.save()


@receiver(post_save, sender=Registration)
def check_if_approved(sender, instance, created, **kwargs):
    user_username = instance.username
    user_name = instance.name
    user_email = instance.email

    staff_users = User.objects.filter(is_staff=True)
    staff_email_list = [staff_user.email for staff_user in staff_users]

    if created == True:
        print("NEW REGISTRATION")
        send_registration_submit_email(user_name, user_email, staff_email_list)

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
