from django.urls import path
from .views import UserProfileListCreateView, userProfileDetailView
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title="Swagger Docs")

urlpatterns = [
    # gets all user profiles and create a new profile
    path("profile/", UserProfileListCreateView.as_view(), name="allprofiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>/", userProfileDetailView.as_view(), name="profile"),
    # path('', schema_view),
]
