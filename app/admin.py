from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Personal, Links, Host, ContentClients, ContentDrivers


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Personal)
admin.site.register(Links)
admin.site.register(Host)
admin.site.register(ContentClients, SomeModelAdmin)
admin.site.register(ContentDrivers, SomeModelAdmin)
