from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
'''
Custom model manager
'''
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset().order_by('phone')
"""

Every time you make a new model
>>>python manage.py makemigrations
>>>python manage.py migrate

AND
Go to admin.py and add:
admin.site.register(<class name>)

"""
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None,null=True)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=256,default='')
    link=models.CharField(max_length=256,default='')
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to='profile_image',blank=True)
    file=models.FileField(upload_to='profile_image',blank=True)
    file_name=models.CharField(max_length=256)
    '''
    Now UsserProfileManager allows me to access queryset in a way i defined
    The variable name with which i define UserProfileManager can now be used to access the objects in shell 
    '''
    camera = UserProfileManager()
    '''
    camera can now be used in place of objects to access queryset
    '''
    def __str__(self):
        return str(self.user.username)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)