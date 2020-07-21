from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    category = models.CharField(max_length=50,blank=True,null=True,unique=True)
    category_description = models.TextField(max_length=1024, blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.category = self.category.lower()
        return super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category


def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=200)
    title_description = models.TextField(max_length=1024, blank=True,null=True)
    category = models.ManyToManyField(Category,blank=True)
    tags = models.CharField(max_length=100, blank=True,null=True)
    content = RichTextUploadingField(blank=True,null=True)
    post_thumbnail = models.ImageField(upload_to='post_thumbnails',blank=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    slug = models.SlugField(max_length=200,unique=True)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Post, self.title)
        else:  # create
            self.slug = generate_unique_slug(Post, self.title)

        super(Post, self).save(*args, **kwargs)
        if self.post_thumbnail:
            img = Image.open(self.post_thumbnail.path)

            if img.height > 300 or img.width > 300:
                output_size = (500, 500)
                img.thumbnail(output_size)
                img.save(self.post_thumbnail.path)

        

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
#     comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
#     comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
#     comment_date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.comment_content
#     class Meta:
#         ordering = ['-comment_date']

