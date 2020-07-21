from django.contrib import admin
from .models import Newsletter,ContactForm

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')
    search_fields = ['interests', 'location']


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('contact_email', 'title','created_on','location')

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(ContactForm, ContactFormAdmin)