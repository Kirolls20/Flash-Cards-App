from django.contrib import admin
from . models import *


admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(NeedToReview)