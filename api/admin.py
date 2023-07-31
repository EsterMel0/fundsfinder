from django.contrib import admin
from .models import FundoImobiliario

# Register your models here.


class FundoAdmin(admin.ModelAdmin):
    ...


admin.site.register(FundoImobiliario, FundoAdmin)
