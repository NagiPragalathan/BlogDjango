from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class blog(models.Model):
    id              =  models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    title           = models.CharField(max_length = 200,default='UnTitled')
    description     = models.CharField(max_length = 200,default = "Author not provied any description")
    content         = models.CharField(max_length = 2000,default = "Author not provied any description")
    blog_profile_img = models.CharField(max_length = 2000,default = "https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X")
    categories = models.CharField(max_length = 200)
    updated_date    = models.DateField(default=timezone.now)
    
class logo(models.Model):
    L_id = models.IntegerField(primary_key=True)
    Reson = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='logo',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now)
    class Meta:
          get_latest_by = ['image']

class Gallery(models.Model):
    G_id = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Gallery/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now)
