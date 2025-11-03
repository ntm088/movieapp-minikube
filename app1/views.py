from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

# List all videos
def video_list(request):
    videos = Video.objects.all().order_by('MovieTitle')
    return render(request, 'app1/video_list.html', {'videos': videos})

# Create a new video
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'app1/video_form.html', {'form': form, 'title': 'Add Video'})

# Update an existing video
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'app1/video_form.html', {'form': form, 'title': 'Edit Video'})

# Delete a video
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'app1/video_confirm_delete.html', {'video': video})
