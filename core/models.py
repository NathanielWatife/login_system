from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    fname = models.CharField(max_length=255, null=True)
    sname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    dob = models.CharField(max_length=255, null=True)
    about = models.CharField(max_length=255, null=True)
    profileimg = models.ImageField(upload_to = "profile_images", default='blank.jpeg')
    location = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.username
    