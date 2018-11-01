from django.db import models

class Personal(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True, default='')
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    phone = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, blank=True, null=True, default='')
    language = models.CharField(max_length=100, blank=True, null=True, default='')
    # reg_second
    birth = models.CharField(max_length=100, blank=True, null=True, default='')
    vehicle = models.CharField(max_length=100, blank=True, null=True, default='')
    # reg_third
    car_manufactore = models.CharField(max_length=100, blank=True, null=True, default='')
    car_year = models.CharField(max_length=100, blank=True, null=True, default='')
    car_number = models.CharField(max_length=100, blank=True, null=True, default='')
    drive_licence = models.CharField(max_length=100, blank=True, null=True, default='')
    taxi_licence = models.CharField(max_length=100, blank=True, null=True, default='')
    # reg_fourth
    photo_user = models.ImageField(upload_to='img/user', blank=True,  default='')
    photo_passport = models.ImageField(upload_to='img/user', blank=True,  default='')
    photo_drive_licence = models.ImageField(upload_to='img/user', blank=True,  default='')
    photo_insurance = models.ImageField(upload_to='img/user', blank=True,  default='')
    exp_drive_licence = models.CharField(max_length=100, blank=True, null=True, default='')
    exp_insurance = models.CharField(max_length=100, blank=True, null=True, default='')
    # reg_fifth
    card_number = models.CharField(max_length=100, blank=True, null=True, default='')
    card_holder = models.CharField(max_length=100, blank=True, null=True, default='')
    user_moderate = models.BooleanField(default=False)
    user_create_data = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return (str(self.id) + '  ' + self.name)


class Links(models.Model):
    name = models.CharField(max_length=100)
    playMarket = models.CharField(max_length=100, blank=True, default='https://play.google.com/store?hl=ru')
    appStore = models.CharField(max_length=100, blank=True, default='https://www.apple.com/ru/ios/app-store/')

    def __str__(self):
        return self.name


class Host(models.Model):
    host = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email
