from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from eyca.models import Profile
from registration.models import Registration
from django.contrib.sites.shortcuts import get_current_site


from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


@receiver(post_save, sender=Registration)
def check_if_approved(sender, instance, created, **kwargs):

    staff_users = User.objects.filter(is_staff=True)
    staff_email_list = [staff_user.email for staff_user in staff_users]

    if created == True:
        print("NEW REGISTRATION AT SIGNAL")

        send_mail(
            'New registration',
            'Recieved a new registration for eYCA. Check the admin panel for more details.',
            settings.EMAIL_HOST_USER,
            staff_email_list,
            fail_silently=False
        )

        send_mail(
            'eYCA',
            'Thank you for showing interest in eYCA. We have received your request and we will get in touch with you shortly.',
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False
        )


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

        staff_users = User.objects.filter(is_staff=True)
        staff_email_list = [staff_user.email for staff_user in staff_users]

        send_mail(
            'eYCA Added',
            'A new campus ambassador has been added',
            settings.EMAIL_HOST_USER,
            staff_email_list,
            fail_silently=False
        )

        user_code = urlsafe_base64_encode(force_bytes(new_user.pk))
        user_token = default_token_generator.make_token(new_user)
        # domain = Site.objects.get_current().domain

        print(user_code)
        print(user_token)

        send_mail(
            'eYCA',
            'Your application to be an eYCA has been approved - ' + user_code + '- ' + user_token,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False
        )

        instance.delete()

        print("SENT MAILS")
