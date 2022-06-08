from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.urls import reverse,reverse_lazy

from django.core.paginator import Paginator  # Import Pagination Stuff
# Gerneric views classes  Imports
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic import DetailView
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *
from .forms import *
import random

class HomeDeckView(LoginRequiredMixin,TemplateView):
   """Render the home page with a list of all decks."""

   template_name='base/home.html'
   def get_context_data(self, **kwargs):
      context= super(HomeDeckView,self).get_context_data(**kwargs)
      context['decks'] = Deck.objects.filter(user=self.request.user)
      context['count']= Card.objects.all()
      return context 


class  CreateNewDeckView(LoginRequiredMixin,CreateView):
   """
      Render A Form To Create a new deck. With Name of The Deck and Description.
   """
   template_name='base/create_Deck.html'
   form_class= CreateNewDeckForm

   def form_valid(self,form):
      form = form.save(commit=False)
      form.user =self.request.user
      form.save()
      return redirect( reverse_lazy('home'))


class UpdateDeckView(LoginRequiredMixin,UpdateView):
   """
      Render A Form To Update a deck. With Name of The Deck and Description.
   """
   template_name= 'base/update_deck.html'
   form_class = CreateNewDeckForm
   model= Deck
   def get_success_url(self):
      return reverse_lazy('home')

class DeleteDeckView(LoginRequiredMixin,DeleteView):
   """
      Render A Form To Delete a deck.
   """
   template_name='base/delete_deck.html'
   model= Deck
   def get_success_url(self):
      return reverse_lazy('home')


# https://stackoverflow.com/questions/58679944/how-to-get-an-object-id-in-form-valid
class CreateNewCardView(LoginRequiredMixin,FormView):
   """
      Render A Form To Create a new card. With Question, Answer and Card Type.
      The Question is the Front Card and the Answer is the Back Card.
   """

   template_name='base/create_card.html'
   form_class= AddNewCardForm
   def form_valid(self,form,*args,**kwargs):
      form.instance.deck_id = self.kwargs['deck_id']
      form.save()
      return super(CreateNewCardView,self).form_valid(form)

   def get_success_url(self):
      pk = self.kwargs['deck_id']
      return reverse('deck_info',kwargs={"pk":pk})

class DeckInfoView(LoginRequiredMixin,TemplateView):
   """
   Render A page To View All Cards Related To Specific Deck With Deck id 
   ,edit and delete buttons,and also Button To Add New Card 
   & Review Cards.
   """
   template_name='base/deck_ifo.html'
   context_object_name= 'card'
   def get_context_data(self,pk, **kwargs):
      deck_id= Deck.objects.get(id=pk)
      context= super(DeckInfoView,self).get_context_data(**kwargs)
      context['deck']=deck_id
      context['Decks'] = Deck.objects.filter(id=pk)
      context['cards'] = Card.objects.filter(deck=deck_id)
      context['count'] = Card.objects.filter(deck=deck_id).count()
      #context['deck_name'] Deck.objects.all
      return context



class UpdateCardView(LoginRequiredMixin,UpdateView):
   """Render A Form To Update a card with Question, Answer and Card Type. """

   template_name='base/update_card.html'
   model=Card
   form_class = AddNewCardForm

   def get_success_url(self):
      # THIS FUNCTION NEED TO BE FIXED
      return reverse_lazy('home')


class CardDetailView(LoginRequiredMixin,DetailView):
   """Render A Page To View A Card Details. """

   template_name='base/card_detail.html'
   model= Card
   context_object_name= 'card'



class DeleteCardView(LoginRequiredMixin,DeleteView):

   """Render A Form To Delete a card From A given Deck."""

   template_name='base/delete_card.html'
   model=Card

   def get_success_url(self):
      # THIS FUNCTION NEED TO BE FIXED
      return reverse_lazy('home')


class GetRandomCard(LoginRequiredMixin,TemplateView):
   """
      Function To Render  Review Cards Page will Generate Cards  randomly With Paginator System.
   """

   template_name='base/get_random_card.html'

   def get_context_data(self,deck_id,**kwargs):
      pk = self.kwargs['deck_id']
      deck_id= Deck.objects.get(id=pk)
      context= super(GetRandomCard,self).get_context_data(**kwargs)
      context['pk'] = deck_id
      context['deck_cards'] = Card.objects.filter(deck=pk).all().order_by('?')
      context['cards_number'] = Card.objects.filter(deck=pk).count()
      # random_number= random.randint(0,context['cards_number'] -1) # Get Random Number 
      # context['random_card'] = Card.objects.all()[random_number]
      # set Up paginator 
      p = Paginator(context['deck_cards'],1)
      page = self.request.GET.get("page")
      context['cards'] = p.get_page(page)
      return context
# how to save many to many field from another model  in django views  
# https://stackoverflow.com/questions/56905871/how-to-save-many-to-many-field-from-another-model-in-django-views 
class SaveToUnknowView(LoginRequiredMixin,TemplateView):
   """
      Button its function  TO Save A Card To Unknow Cards List That  you Need to Review It later. 
   """
   template_name='base/deck_ifo.html'
   def post(self,request,pk):
      card_id= Card.objects.get(id=pk)
      deck_id= deck_id= Deck.objects.get(id=card_id.deck_id)
      if request.method == 'POST':
         saved_card=NeedToReview.objects.get(user=self.request.user).cards.add(card_id)
         if  saved_card:
            return redirect(reverse_lazy('home'))
            messages.error(self.request,'Card Already  Saved')
         else:
            return redirect(reverse_lazy('home'))  
      return render(request,self.template_name)


class UnknowCardsView(LoginRequiredMixin,TemplateView):
   """ Render A Page Contain  All Unknown  Cards That You Need To Review them ."""
   template_name='base/unknowncards.html'

   def get_context_data(self,**kwargs):
      context= super(UnknowCardsView,self).get_context_data(**kwargs)
      context['cards'] = NeedToReview.objects.get(user=self.request.user).cards.all()
      return context

class DeleteCardFromNeedToRememberLst(LoginRequiredMixin,TemplateView):
   """Button its function  TO Delete A Card From Need To Review Card List."""

   template_name='base/del_unknowncard.html'
   def post(self,request,pk):
      card_id= Card.objects.get(id=pk)
      if request.method == 'POST':
         saved_card=NeedToReview.objects.get(user=self.request.user).cards.remove(card_id)
         messages.success(self.request,'Card Deleted From Need To Review List')
         return redirect(reverse_lazy('unknown_cards'))
      return render(request,self.template_name)



class ReviewUnknownCards(LoginRequiredMixin,TemplateView):

   """ReView A Card From Need To Review List With Paginator System. """
   
   template_name='base/review_unknown_cards.html'
   def  get_context_data(self, **kwargs):
      context = super(ReviewUnknownCards,self).get_context_data(**kwargs)
      context["cards"] = NeedToReview.objects.get(user=self.request.user).cards.all() 
      p= Paginator(context["cards"],1)
      page = self.request.GET.get("page")
      context["cards"] = p.get_page(page)
      return context


