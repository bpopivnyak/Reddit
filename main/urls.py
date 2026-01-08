from django.urls import path
from .views import PostView, PostDetail, PostCreate, PostDelete
from extra_pages.views import ProfileDetail, AboutYourself, NoteListView, NoteDetailView, NoteCreateView, NoteDeleteView, NoteEditView

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('about_us/', AboutYourself.as_view(), name='about_us'),
    path('notes/', NoteListView.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    path('notes/edit/<int:pk>/', NoteEditView.as_view(), name='note-edit'),

]