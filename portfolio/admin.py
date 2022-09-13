from django.contrib import admin
from .models import About, Contact, Home, Resume, Service


class HomeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service',)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Contact)
