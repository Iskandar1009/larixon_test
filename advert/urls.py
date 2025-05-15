from django.urls import path
from .views import AdvertListView, AdvertDetailView

urlpatterns = [
    path('api/advert-list/', AdvertListView.as_view()),
    path('api/advert/<int:pk>/', AdvertDetailView.as_view()),
]
