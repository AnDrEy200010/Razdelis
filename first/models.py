from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class ProfilePhysPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Person')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, unique=True, blank=True)
    phone = models.CharField(max_length=30, null=True)
    verify_email = models.BooleanField(default=False)
    verify_phone = models.BooleanField(default=False)
    address = models.TextField()
    city = models.CharField(max_length=40)
    data_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ProfileLegalPerson(models.Model):
    """
    Model for legal person
    """


class Chapter(models.Model):
    name_chapter = models.CharField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name_chapter


class Category(models.Model):
    name_category = models.CharField(max_length=255, blank=True)
    chapter_id = models.ForeignKey(Chapter, on_delete=models.SET_NULL, verbose_name='Chapter')

    def __str__(self):
        return self.name_category


class ImagesItem(models.Model):
    title_image = models.TextField()
    image = models.ImageField(upload_to='images/items', blank=True)


class Item(models.Model):
    name_item = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price_item = models.FloatField()
    image_id = models.ForeignKey(ImagesItem, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL)
    reservation_id = ''


class Reservation(models.Model):
    date_res = models.DateTimeField(auto_now_add=True)
    item_id = models.ForeignKey(Item, on_delete=models.SET_NULL)
    profile_id = models.ForeignKey(ProfilePhysPerson, on_delete=models.SET_NULL)


class Transaction(models.Model):
    """"""


# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver')
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.message


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        ProfilePhysPerson.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            ProfilePhysPerson.objects.create(user=instance)