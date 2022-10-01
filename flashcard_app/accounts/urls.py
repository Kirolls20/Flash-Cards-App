from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   # Login And Logout Urls
   path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('signup/',views.CreateUserView.as_view(),name='signup')
]
