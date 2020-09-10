from django.db import models
from django.db.models.signals import pre_save
import time

# Create your models here.


class Step1FormModel(models.Model):
    client_id = models.UUIDField(null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    bemovil_id = models.IntegerField(null=True)
    personal_id = models.TextField(max_length=100, null=True)
    expedition_date = models.DateField(null=True)
    expedition_place = models.CharField(max_length=100, null=True)
    mobile_phone = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    email = models.EmailField(max_length=255, null=True)

    # address = models.TextField(max_length=100, null=True)
    # city = models.CharField(max_length=100, null=True)
    # valley = models.CharField(max_length=100, null=True)
    # image1 = models.ImageField(upload_to='user_images/', null=True)
    # image2 = models.ImageField(upload_to='user_images/', null=True)
    # image3 = models.ImageField(upload_to='user_images/', null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)


class PhoneOTP(models.Model):
    # phone_regex = RegexValidator(regex=r'^\+?234?\d(9,14)$',
    #     message="Phone number must be entered in format of +2348044234244 up to 14 digits")
    # phone = models.CharField(validator=[phone_regex], max_length=15, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    initial = models.IntegerField(blank=True, null=True)
    last = models.IntegerField(blank=True, null=True)
    validated = models.BooleanField(default=False)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.phone_number} is sent {self.otp}'


def add_timer(sender, instance, *args, **kwargs):
    instance.initial = int(time.time())
    instance.last = instance.initial + 30


pre_save.connect(add_timer, sender=PhoneOTP)


class Step2FormModel(models.Model):
    address = models.TextField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    valley = models.CharField(max_length=100, null=True)


class Step3FormModel(models.Model):
    mobile_phone = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


class UserPictures(models.Model):
    '''
    Model to manage multiple pictures of the user
    '''
    #user_uuid = models.UUIDField(null=True)
    name = models.CharField(max_length=200, null=True)
    image1 = models.ImageField(upload_to='user_images/', null=True)
    image2 = models.ImageField(upload_to='user_images/', null=True)
    image3 = models.ImageField(upload_to='user_images/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class FileModel(models.Model):
    uploader = models.CharField(max_length=20)
    firstFile = models.FileField(upload_to='documents')
    secondFile = models.FileField(upload_to='documents')
    file = models.BinaryField(null=True, blank=False)

    def __str__(self):
        return self.uploader