from django.contrib import admin
from django.contrib.auth.models import User, Group
from infoschoolpupil.models import PupilMoney


admin.site.unregister([Group])
admin.site.register([PupilMoney])   # register qilish
