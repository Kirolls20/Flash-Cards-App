from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
   path('',views.HomeDeckView.as_view(),name='home'),
   path('create/new/deck/',views.CreateNewDeckView.as_view(),name='new_deck'),
   path('deck/<int:pk>/',views.DeckInfoView.as_view(),name='deck_info'),
   path('create/card/<int:deck_id>/',views.CreateNewCardView.as_view(),name='create_card'),
   path('update/deck/<int:pk>/',views.UpdateDeckView.as_view(),name='update_deck'),
   path('detail/card/<int:pk>/',views.CardDetailView.as_view(),name='card_detail'),
   path('delete/deck/<int:pk>/',views.DeleteDeckView.as_view(),name='delete_deck'),
   path('update/card/<int:pk>/', views.UpdateCardView.as_view(), name='update_card'),
   path('delete/card/<int:pk>/',views.DeleteCardView.as_view(),name='delete_card'),
   path('get/random/card/<int:deck_id>/',views.GetRandomCard.as_view(),name='get_random'),
   path('unknown/cards/',views.UnknowCardsView.as_view(),name='unknown_cards'),
   path('save/unknowcard/<int:pk>/',views.SaveToUnknowView.as_view(),name='save_to_unknown'),
   path('need_to_remember/review/cards/',views.ReviewUnknownCards.as_view(),name='review_unknown'),
   path('delete/unknowcard/<int:pk>/',views.DeleteCardFromNeedToRememberLst.as_view(),name='delete_unknown_card'),
   # Login And Logout Urls
   path('accounts/login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
   path('accounts/logout/',LogoutView.as_view(),name='logout'),

]