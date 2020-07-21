from django.db import models

# Create your models here.
class MainIndexPage(models.Model):
    app_name = models.CharField(max_length=255,blank=True,null=True,unique=True)

    index_main_header = models.CharField(max_length=255,blank=True,null=True)
    index_main_sub_header = models.CharField(max_length=255,blank=True,null=True)
    
    meta_title = models.CharField(max_length=255,blank=True,null=True)
    meta_title_description = models.TextField(max_length=1024, blank=True,null=True)
    meta_tags = models.TextField(max_length=1024, blank=True,null=True)

    index_main_footer_content_title = models.CharField(max_length=255,blank=True,null=True)
    index_main_footer_content = models.CharField(max_length=255,blank=True,null=True)
    index_main_footer_copyright = models.CharField(max_length=255,blank=True,null=True)
    index_main_footer_poweredby = models.CharField(max_length=255,blank=True,null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = "Main Index Page"
        verbose_name_plural = "Main Index Pages"
    
    def __str__(self):
        return self.app_name