from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
"""

Every time you make a new model
>>>python manage.py makemigrations
>>>python manage.py migrate

AND
Go to admin.py and add:
admin.site.register(<class name>)

"""
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=True)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=256,default='')
    link=models.CharField(max_length=256,default='')
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
        return str(self.user.username)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)