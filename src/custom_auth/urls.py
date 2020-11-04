from .views import UserAccountLoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
