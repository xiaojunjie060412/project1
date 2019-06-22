from django.contrib import admin
from .models import Classify, MyPicture, Photographer, Celebrity, Message

# Register your models here.

admin.site.register(Classify)
admin.site.register(Photographer)
admin.site.register(MyPicture)
admin.site.register(Celebrity)
admin.site.register(Message)
