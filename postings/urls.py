from django.urls import path
from postings import views


urlpatterns = [
    path("postings/", views.PostingList.as_view(), name='posting-list'),
    path("postings/<int:pk>/", views.PostingDetail.as_view(), name='posting-detail'),

    path("users/", views.UserList.as_view(), name='user-list'),
    path("users/<int:pk>/", views.UserDetail.as_view(), name='user-detail'),
    path("", views.api_root),
]


