from django.contrib import admin


# Register your models here.


#import all of our models
from book_catalog_app.models import *


#now we're going to register the models, we're not really doing anything with them
#we're registering models we want available in the Django Admin


class ProfileAdmin(admin.ModelAdmin):
   pass


admin.site.register(Profile, ProfileAdmin)