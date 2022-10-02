from django.db import models

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

CARD_TYPE=(
   ('General','General'),
   ('Coding','Coding')
)




class Deck(models.Model):

   user = models.ForeignKey(User,on_delete=models.CASCADE)
   topic = models.CharField(max_length=55,null=False,blank=False)
   description= models.CharField(max_length=300,null=True, blank=True)
   need_to_remember_cards = models.ManyToManyField('Deck',related_name='need_to_remember',through='NeedToRemember')
   pub_date=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.topic 

class Card(models.Model):
   deck= models.ForeignKey(Deck,on_delete=models.CASCADE)
   frontcard= models.CharField(max_length=250)
   # backcard = RichTextField(blank=True,null=True)
   backcard= RichTextUploadingField(blank=True,null=True ,extra_plugins=['resize','codesnippet'],external_plugin_resources=[(
   'resize',
   '/static/ckeditor_plugins/resize/',
   'plugin.js'
)])
   card_type = models.CharField(choices=CARD_TYPE,max_length=100)
   pub_date=models.DateTimeField(auto_now_add=True)

   def  __str__(self):
      return self.frontcard

class Note(models.Model):  
   """General Notes Model"""
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   title= models.CharField(max_length=100)
   content= models.TextField()
   pub_date=models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return self.title

# class NeedToRemember(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    cards= models.ManyToManyField("Card",blank=True, null=True,related_name='review_cards')

class NeedToRemember(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   card = models.ForeignKey(Card,on_delete=models.CASCADE)
   created_at = models.DateField(auto_now_add=True)

   class Meta:
      unique_together = [['card']]
