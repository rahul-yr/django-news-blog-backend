from django.contrib import admin
from .models import Post ,Category
# from .forms import CustomPostChangeForm,CustomPostCreationForm


class PostAdmin(admin.ModelAdmin):
    # model = Post
    # add_form = CustomPostCreationForm
    # form = CustomPostChangeForm
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status","category")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_on')
    list_filter = ("category",)
    search_fields = ['category', 'category_description']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
