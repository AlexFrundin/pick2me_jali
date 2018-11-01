from django.shortcuts import render, redirect
from .models import Personal, Links, Host
from django.core.mail import send_mail


def send_email(user):
    host = Host.objects.get(id=1)
    text = f"""
    Был зарегистрированый новый пользователь.
    Имя: {user.name}
    Email: {user.email}
    Номер телефона: {user.phone}
    Город: {user.city}
    Язык: {user.language}
    День рождения: {user.birth}
    """
    if user.vehicle == '':
        text += f"""
        У нового курьера есть автомобиль {user.car_manufactore}, {user.car_year} года выпуска, с номером {user.car_number}.
        Номер водительского удостоверения: {user.drive_licence}
        """
        if user.taxi_licence != '':
            text += f"""Номер лицензии таксиста: {user.taxi_licence}
                       Фотография водительского удостоверения: {host.host}{user.photo_drive_licence}
                       Дата окончания водитеского удостоверения: {user.exp_drive_licence}
                       Фотография страховки: {host.host}{user.photo_insurance}
                       Дата окончания страховки:{user.exp_insurance}
                       """
    else:
        text += f"У нового курьера нет автомобиля. Крьер выбрал доставку на {user.vehicle}"
    text += f"""
    Фотография курьера: {host.host}{user.photo_user}
    Паспорт курьера: {host.host}{user.photo_passport}
    Номер карты: {user.card_number}
    Владелец карты: {user.card_holder}
    """

    send_mail('New personal', text, "pick2mesender", [host.email,], fail_silently=False)
    return True



def main(request):
    return redirect("clients")


def drivers(request):
    return render(request, "drivers.html", {"link" : Links.objects.get(name="driver")})


def drivers_rtl(request):
    return render(request, "drivers-rtl.html", {"link" : Links.objects.get(name="driver")})


def drivers_ru(request):
    return render(request, "drivers-ru.html", {"link" : Links.objects.get(name="driver")})


def client(request):
    return render(request, "clients.html", {"link" : Links.objects.get(name="client")})


def client_rtl(request):
    return render(request, "clients-rtl.html", {"link" : Links.objects.get(name="client")})


def client_ru(request):
    return render(request, "clients-ru.html", {"link" : Links.objects.get(name="client")})


def reg_first(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'Empty')
        name = request.POST.get('name', 'Empty')
        phone = request.POST.get('phone', 'Empty')
        city = request.POST.get('city', 'Empty')
        language = request.POST.get('language', 'Empty')
        have = request.POST.get('have')
        new = Personal(email=email, name=name, phone=phone, city=city, language=language)
        new.save()
        if have == "have":
            return render(request, "registration/third-step.html", {'id': new.id})
        return render(request, "registration/second-step.html", {'id': new.id})
    return render(request, "registration/first-step.html")


def reg_first_rtl(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'Empty')
        name = request.POST.get('name', 'Empty')
        phone = request.POST.get('phone', 'Empty')
        city = request.POST.get('city', 'Empty')
        language = request.POST.get('language', 'Empty')
        have = request.POST.get('have')
        new = Personal(email=email, name=name, phone=phone, city=city, language=language)
        new.save()
        if have == "have":
            return render(request, "registration/third-step-rtl.html", {'id': new.id})
        return render(request, "registration/second-step-rtl.html", {'id': new.id})
    return render(request, "registration/first-step-rtl.html")


def reg_first_ru(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'Empty')
        name = request.POST.get('name', 'Empty')
        phone = request.POST.get('phone', 'Empty')
        city = request.POST.get('city', 'Empty')
        language = request.POST.get('language', 'Empty')
        have = request.POST.get('have')
        new = Personal(email=email, name=name, phone=phone, city=city, language=language)
        new.save()
        if have == "have":
            return render(request, "registration/third-step-ru.html", {'id': new.id})
        return render(request, "registration/second-step-ru.html", {'id': new.id})
    return render(request, "registration/first-step-ru.html")


def reg_second(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        local = request.POST.get('local')
        new = Personal.objects.get(id=id)
        new.birth = request.POST.get('birth', 'Empty')
        new.vehicle = request.POST.get('vehicle', 'Empty')
        new.save()
        if local == 'eng':
            return render(request, "registration/fourth-new.html", {'id': new.id})
        elif local == 'ru':
            return render(request, "registration/fourth-new-ru.html", {'id': new.id})
        elif local == 'rtl':
            return render(request, "registration/fourth-new-rtl.html", {'id': new.id})
    return redirect("/driver.html")


def reg_third(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        local = request.POST.get('local')
        new = Personal.objects.get(id=id)
        new.birth = request.POST.get('birth', 'Empty')
        new.car_manufactore = request.POST.get('car-manufactore', 'Empty')
        new.car_year = request.POST.get('car-year', 'Empty')
        new.car_number = request.POST.get('car-number', 'Empty')
        new.drive_licence = request.POST.get('drive-license', 'Empty')
        new.taxi_licence = request.POST.get('taxi-license', 'Empty')
        new.save()
        if local == 'eng':
            return render(request, "registration/fourth-step.html", {'id': new.id})
        elif local == 'ru':
            return render(request, "registration/fourth-step-ru.html", {'id': new.id})
        elif local == 'rtl':
            return render(request, "registration/fourth-step-rtl.html", {'id': new.id})
    return redirect("/driver.html")


def reg_fourth_new(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        local = request.POST.get('local')
        new = Personal.objects.get(id=id)
        new.photo_user = request.FILES['photo']
        new.photo_passport = request.FILES['passport']
        new.save()
        if local == 'eng':
            return render(request, "registration/fifth-step.html", {'id': new.id})
        elif local == 'ru':
            return render(request, "registration/fifth-step-ru.html", {'id': new.id})
        elif local == 'rtl':
            return render(request, "registration/fifth-step-rtl.html", {'id': new.id})
    return redirect("/driver.html")


def reg_fourth_car(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        local = request.POST.get('local')
        new = Personal.objects.get(id=id)
        new.photo_user = request.FILES['photo']
        new.photo_passport = request.FILES['passport']
        new.photo_drive_licence = request.FILES['driver-license']
        new.photo_insurance = request.FILES['insurance']
        l_year = request.POST.get('l_year', 'year')
        l_month = request.POST.get('l_month', 'month')
        l_day = request.POST.get('l_day', 'day')
        new.exp_drive_licence = '{}-{}-{}'.format(l_year, l_month, l_day)
        i_year = request.POST.get('i_year', 'year')
        i_month = request.POST.get('i_month', 'month')
        i_day = request.POST.get('i_day', 'day')
        new.exp_insurance = '{}-{}-{}'.format(i_year, i_month, i_day)
        new.save()
        if local == 'eng':
            return render(request, "registration/fifth-step.html", {'id': new.id})
        elif local == 'ru':
            return render(request, "registration/fifth-step-ru.html", {'id': new.id})
        elif local == 'rtl':
            return render(request, "registration/fifth-step-rtl.html", {'id': new.id})
    return redirect("/driver.html")


def reg_fifth(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        local = request.POST.get('local')
        new = Personal.objects.get(id=id)
        new.card_number = request.POST.get('card-number', 'Empty')
        new.card_holder = request.POST.get('card-holder', 'Empty')
        new.save()
        send_email(new)
        if local == 'eng':
            return render(request, "registration/congratulations.html")
        elif local == 'ru':
            return render(request, "registration/congratulations-ru.html", {'local': '-ru'})
        elif local == 'rtl':
            return render(request, "registration/congratulations-rtl.html", {'local': '-rtl'})
    return redirect("/driver.html")
