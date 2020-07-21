from . import views
from django.urls import path,include

app_name = 'post'
urlpatterns = [
    path('all/', views.get_all_posts,name='all_posts'),
    path('categories/', views.get_all_categories,name='all_categories'),
    path('categories/<str:category>', views.get_posts_byCategory,name='all_posts_by_category'),
    path('detail/<slug:slug>', views.get_detail_post_bySlug,name='detail_post_by_slug'),
    # path('detail/<int:pk>', views.get_detail_post_byID,name='detail_post_by_id'),

]
