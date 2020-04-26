from django.urls import path

from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path("profile", UserProfileListCreateView.as_view()),
    path("profile/<int:pk>", UserProfileDetailView.as_view())

]
