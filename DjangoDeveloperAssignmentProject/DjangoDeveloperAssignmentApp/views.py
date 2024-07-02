from django.shortcuts import render
from .forms import *
from django.contrib.auth import  login,logout
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('video_list') #need to replace this html
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def video_list(request):
    username = request.user.username 
    return render(request, 'video_list.html', {'username': username})


def logout_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None  # Handle non-authenticated user case if needed
    logout(request)
    return render(request, 'logout_success.html', {'username': username})

def logout_success(request):
    return render(request, 'logout_success.html')

def home(request):
    print('home view is called')
    return render(request, 'home.html')

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')  # Redirect to a video list view
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoUploadForm
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def view_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'view_video.html', {'video': video})

def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'confirm_delete.html', {'video': video})

#live stream
def live_stream(request):
    return render(request, 'live_stream.htmls')

def add_live_stream(request):
    if request.method == 'POST':
        form = LiveStreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_live_streams')
    else:
        form = LiveStreamForm()
    return render(request, 'add_live_stream.html', {'form': form})

def list_live_streams(request):
    live_streams = LiveStream.objects.all()
    return render(request, 'list_live_streams.html', {'live_streams': live_streams})

def view_live_stream(request, id):
    live_stream = get_object_or_404(LiveStream, id=id)
    return render(request, 'live_streams.html', {'stream_url': live_stream.stream_url})

def delete_live_stream(request, id):
    live_stream = get_object_or_404(LiveStream, id=id)
    live_stream.delete()
    return redirect('list_live_streams')