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

class ContentClients(models.Model):

    LANGUAGE = (
        ('en',"English"),
        ('ru','Русский'),
        ('rtl','Arabian')
    )

    lang = models.CharField('language',max_length=100, choices=LANGUAGE, unique=True)

    main_title = models.CharField(max_length=50)
    main_descrription = models.TextField()

    food_delivery = models.CharField(max_length=100)
    food_delivery_description = models.TextField()

    track_order = models.CharField(max_length=100)
    track_order_description = models.TextField()

    mobile_app = models.CharField(max_length=100)
    mobile_app_description = models.TextField()

    range_title = models.CharField(max_length=100)

    pills = models.CharField(max_length=100)
    pills_description = models.TextField()

    clothes = models.CharField(max_length=100)
    clothes_description = models.TextField()

    food_box = models.CharField(max_length=100)
    food_box_description = models.TextField()

    dishes = models.CharField(max_length=100)
    dishes_description = models.TextField()

    taxi = models.CharField(max_length=100)
    taxi_description = models.TextField()

    download_app = models.CharField(max_length=100)
    download_app_description = models.TextField()

    about_first = models.CharField(max_length=100)
    about_first_description = models.TextField()

    about_second = models.CharField(max_length=100)
    about_second_description = models.TextField()

    about_third = models.CharField(max_length=100)
    about_third_description = models.TextField()

    about_four = models.CharField(max_length=100)
    about_four_description = models.TextField()

    about_five = models.CharField(max_length=100)
    about_five_description = models.TextField()

    about_six = models.CharField(max_length=100)
    about_six_description = models.TextField()

    def __str__(self):
        return self.get_lang_display()


class Footer(models.Model):
    pass



class ContentDrivers(models.Model):
    LANGUAGE = (
        ('en',"English"),
        ('ru','Русский'),
        ('rtl','Arabian')
    )

    lang = models.CharField('language',max_length=100, choices=LANGUAGE, unique=True)

    taxi_title = models.CharField(max_length=100, blank=True)
    taxi_description = models.TextField(blank=True)

    taxi_app_title = models.CharField(max_length=100,blank=True)
    taxi_app_description = models.TextField(blank=True)

    conditions_title = models.CharField(max_length=100,blank=True)
    conditions_descriptiom = models.TextField(blank=True)

    conditions_one_title = models.CharField(max_length=100,blank=True)
    conditions_one_description = models.TextField(blank=True)
    conditions_two_title = models.CharField(max_length=100,blank=True)
    conditions_two_description = models.TextField(blank=True)
    conditions_three_title = models.CharField(max_length=100,blank=True)
    conditions_three_description = models.TextField(blank=True)

    step_title = models.CharField(max_length=100,blank=True)
    step_one_title = models.CharField(max_length=100,blank=True)
    step_one_description = models.TextField(blank=True)
    step_two_title = models.CharField(max_length=100,blank=True)
    step_two_description = models.TextField(blank=True)
    step_three_title = models.CharField(max_length=100,blank=True)
    step_three_description = models.TextField(blank=True)

    download_title = models.CharField(max_length=100,blank=True)
    download_p = models.CharField(max_length=100,blank=True)
    download_description = models.TextField(blank=True)

    about_title = models.CharField(max_length=100,blank=True)
    about_p = models.CharField(max_length=100,blank=True)

    about_one_title = models.CharField(max_length=100,blank=True)
    about_one_description = models.TextField(blank=True)

    about_two_title = models.CharField(max_length=100,blank=True)
    about_two_description = models.TextField(blank=True)

    about_three_title = models.CharField(max_length=100,blank=True)
    about_three_description = models.TextField(blank=True)

    button_one = models.CharField(max_length=100,blank=True)
    button_two = models.CharField(max_length=100,blank=True)
    header = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.get_lang_display()


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
