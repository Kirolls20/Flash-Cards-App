from django.forms import ModelForm
from .models import *


class CreateNewDeckForm(ModelForm):
   class Meta:
      model= Deck
      fields=['topic','description']

class AddNewCardForm(ModelForm):
   class Meta:
      model= Card
      fields=['frontcard','backcard','card_type']

   def __init__(self,*args,**kwargs):
      super(AddNewCardForm,self).__init__(*args,**kwargs)
      self.fields['frontcard'].label = 'Question'
      self.fields['backcard'].label= 'Answer'
      