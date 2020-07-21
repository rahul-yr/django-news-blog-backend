from django.contrib import admin
from .models import MainIndexPage
# Register your models here.

class MainIndexPageAdmin(admin.ModelAdmin):
    list_display = ('app_name','meta_title', 'index_main_header','created_on','updated_on')


admin.site.register(MainIndexPage, MainIndexPageAdmin)