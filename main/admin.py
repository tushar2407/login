from django.contrib import admin
from main.models import *
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','city_delhi','phone', 'link')
    # the heading to be displayed at the userprofiles column should be given in place of "user_info"
    # to only use pass in the below function, make all the elements of tuple the same name as the ones specified in models.py 
    # If you want the heading to be something else then just give that name above and making a def for that return the value you want under it as city_delhi
    def user_info(self,obj):
         return obj.description
    def city_delhi(self,obj):
        return obj.city
    user_info.short_description='Info'
    # soring objects on your own will
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-phone','user')
        #now the objects  under userprofile will be arranged in decreasing order of phone numbers
        # removing (-) sign arranges in increasing order 
        # second param is the second preference for arranging the user objects
        return queryset

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
"""

Customising admin page of django
1. below method
2. making a template that extends admin/base.html

"""
admin.site.site_header='Administration'