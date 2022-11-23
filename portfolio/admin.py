from django.contrib import admin
from .models import About, Contact, Home, Portfolio, Resume, Service



class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service',)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Home)
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact)
