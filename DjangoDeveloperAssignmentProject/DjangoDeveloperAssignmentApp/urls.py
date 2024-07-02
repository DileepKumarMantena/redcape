from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('', register, name='register'),
    path('video_list/',video_list, name='video_list'),
    path('logout/', logout_view, name='logout'),
    path('logout_success/', logout_success, name='logout_success'),
    path('', home, name='home'),
    path('videos/', video_list, name='video_list'),
    path('upload/', upload_video, name='upload_video'),
    path('upload/',upload_video, name='upload_video'),
    path('view/<int:video_id>/', view_video, name='view_video'),
    path('delete/<int:video_id>/',delete_video, name='delete_video'),

    #live stream
    path('live_stream/', live_stream, name='live_stream'),
    path('add_live_stream/', add_live_stream, name='add_live_stream'),
    path('live_streams/', list_live_streams, name='list_live_streams'),
    path('view_live_stream/<int:id>/', view_live_stream, name='view_live_stream'),
    path('delete_live_stream/<int:id>/', delete_live_stream, name='delete_live_stream'),


]
