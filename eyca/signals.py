import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageOps
from resizeimage import resizeimage
from io import BytesIO
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Profile)
def resize_profile_pic(sender, instance, created, **kwargs):
    if created == False:
        return
    img = Image.open(instance.profile_pic)
    img = ImageOps.exif_transpose(img)

    img = resizeimage.resize_contain(img, [250, 250], bg_color=(255, 255, 255, 1))

    img_io = BytesIO()
    img = img.convert('RGB')
    img.save(img_io, format='JPEG')

    file_name = instance.user.username+"_profile_pic.jpg"

    img_file = InMemoryUploadedFile(img_io, None, file_name, 'image/jpeg', len(img_io.getvalue()), None)
    instance.profile_pic = img_file
    instance.save()


@receiver(post_delete, sender=Profile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Profile' object is deleted.
    """
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding 'Profile' object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).profile_pic
    except Profile.DoesNotExist:
        return False

    new_file = instance.profile_pic
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
