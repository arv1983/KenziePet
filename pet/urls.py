from django.urls import path
from .views import GroupView

urlpatterns = [
    path('animals/', GroupView.as_view()),
    path('animals/<int:animal_id>/', GroupView.as_view())
]