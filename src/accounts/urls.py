from django.urls import path
from accounts.views import ProfilesListView, ProfileCreateView, ProfileDetailView, ProfileEditView, ProfileDeleteView

app_name = 'profiles'

urlpatterns = [
    path('', ProfilesListView.as_view(), name='list'),
    path('add/', ProfileCreateView.as_view(), name='add'),
    path('edit/<item_id>', ProfileEditView.as_view(), name='edit'),
    path('show/<item_id>', ProfileDetailView.as_view(), name='show'),
    path('delete/<item_id>', ProfileDeleteView.as_view(), name='delete'),
]
