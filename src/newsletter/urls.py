from . import views
from django.urls import path,include

app_name = 'newsletter'
urlpatterns = [
    path('subscribe/', views.subscribe_to_newsletter,name='join_newsletter'),
    path('contactform/', views.submit_contact_form,name='contact_form'),

]
