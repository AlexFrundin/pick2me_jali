from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', views.main),
    # path('drivers-rtl', views.drivers_rtl, name='drivers-rtl'),
    # path('drivers-ru', views.drivers_ru, name='drivers-ru'),
    path('drivers/<str:lang>', views.drivers, name="drivers"),
    # path('clients-rtl', views.client_rtl, name='clients-rtl'),
    # path('clients-ru', views.client_ru, name='clients-ru'),
    path('clients/<str:lang>', views.clients, name='clients'),

    path('registration/first-step-rtl', views.reg_first_rtl),
    path('registration/first-step-ru', views.reg_first_ru),
    path('registration/first-step', views.reg_first),

    path('registration/second-step', views.reg_second),
    path('registration/third-step', views.reg_third),

    path('registration/fourth-new', views.reg_fourth_new),
    path('registration/fourth-step', views.reg_fourth_car),

    path('registration/fifth-step', views.reg_fifth),

    # path('registration/congratulations, views.reg_finish),

    # path('registration/third-step-rtl', views.reg_third),
    # path('registration/fifth-step-rtl', views.reg_fifth),
    # path('registration/first-step-rtl', views.reg_first),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
