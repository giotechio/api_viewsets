from django.urls import path, include       # 'include' is needed to implment with routers
from rest_framework.routers import DefaultRouter   # needed to implment with routers
from postings import views

from postings.views import PostingViewSet, UserViewSet, api_root



# urlpatterns = [
#     path("postings/", views.PostingList.as_view(), name='posting-list'),
#     path("postings/<int:pk>/", views.PostingDetail.as_view(), name='posting-detail'),

#     path("users/", views.UserList.as_view(), name='user-list'),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name='user-detail'),
#     path("", views.api_root),
# ]



"""Using ViewSets"""

# posting_list = PostingViewSet.as_view(
#     {
#     'get': 'list',
#     'post': 'create'
# }
# )

# posting_detail = PostingViewSet.as_view(
#     {
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# }
# )
# user_list = UserViewSet.as_view(
#     {
#     'get': 'list'
# }
# )

# user_detail = UserViewSet.as_view(
#     {
#     'get': 'retrieve'
# }
# )
""" urlpatterns to implement with ViewSets"""
# urlpatterns = [
#     path("postings/", posting_list, name='posting-list'),
#     path("postings/<int:pk>/", posting_detail, name='posting-detail'),

#     path("users/", user_list, name='user-list'),
#     path("users/<int:pk>/", user_detail, name='user-detail'),
#     path("", api_root),
# ]


""" implementation with routers"""


router = DefaultRouter()
router.register(r'postings', views.PostingViewSet, basename="posting")
router.register(r'users', views.UserViewSet,basename="user")


urlpatterns = [
    path('', include(router.urls)),
]