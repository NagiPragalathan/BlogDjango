from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
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
    L_id = models.IntegerField(null=True, blank=True)
    Reson = models.CharField(max_length = 200, null=True, blank=True)
    image = models.ImageField(upload_to='logo',default='images/user_image.png')
    class Meta:
          get_latest_by = ['image']

class Gallery(models.Model):
    L_id = models.IntegerField(null=True, blank=True)
    G_id = models.CharField(max_length = 200, null=True, blank=True)
    image = models.ImageField(upload_to='Gallery/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200, blank=True)

class OTPVerification(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    email = models.EmailField()
    otp_key = models.CharField(max_length=6)  # Adjust the max_length as needed
    updated_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OTPVerification(id={self.id}, otp_key={self.otp_key}, updated_time={self.updated_time})"

class SaveBlog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Post_id = models.UUIDField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # Connect to the User model
    updated_time = models.DateTimeField(default=timezone.now)
    
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    Post_id = models.UUIDField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    last_updated_date = models.DateTimeField(auto_now=True)
