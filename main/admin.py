from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Note)
admin.site.register(NeedToRemember)