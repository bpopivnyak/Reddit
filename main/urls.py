from django.urls import path
from .views import PostView, PostDetail, PostCreate, PostDelete
from extra_pages.views import ProfileDetail

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
]