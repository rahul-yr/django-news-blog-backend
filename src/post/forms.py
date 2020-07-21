from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Post


class CustomPostCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Post
        fields = '__all__'


class CustomPostChangeForm(UserChangeForm):

    class Meta:
        model = Post
        fields = '__all__'
