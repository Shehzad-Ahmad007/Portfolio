from django.contrib import admin
from .models import About, Contact, Home


class HomeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact)
