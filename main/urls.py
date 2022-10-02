from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
   path('',views.LandingPageView.as_view(),name='landing'),
   path('home',views.HomeDeckView.as_view(),name='home'),
   path('create/new/deck/',views.CreateNewDeckView.as_view(),name='new_deck'),
   path('deck/<int:pk>/',views.DeckInfoView.as_view(),name='deck_info'),
   path('create/card/<int:deck_id>/',views.CreateNewCardView.as_view(),name='create_card'),
   path('update/deck/<int:pk>/',views.UpdateDeckView.as_view(),name='update_deck'),
   path('detail/card/<int:pk>/',views.CardDetailView.as_view(),name='card_detail'),
   path('delete/deck/<int:pk>/',views.DeleteDeckView.as_view(),name='delete_deck'),
   path('update/card/<int:pk>/', views.UpdateCardView.as_view(), name='update_card'),
   path('delete/card/<int:pk>/',views.DeleteCardView.as_view(),name='delete_card'),
   path('get/random/card/<int:deck_id>/',views.GetRandomCard.as_view(),name='get_random'),
   path('need-to-remember/cards/',views.NeedToRememberListView.as_view(),name='need_to_remember'),
   path('save/unknowcard/<int:pk>/',views.SaveToUnknowView.as_view(),name='save_to_unknown'),
   path('delete/unknowcard/<int:pk>/',views.DeleteCardFromNeedToRememberLst.as_view(),name='delete_need_to_remember_card'),
   path('general/notes/',views.GeneralNotesView.as_view(),name='general_notes'),
   path('update/general/notes/<int:pk>/',views.UpdateNoteView.as_view(),name='update_note'),
   path('delete/note/<int:pk>/',views.DeleteNoteView.as_view(),name='delete_note'),


]