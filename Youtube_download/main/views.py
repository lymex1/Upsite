from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkForm
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def up_text(request):
    error = ''
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
        else:
            error = 'Форма была неверной'
    form = LinkForm
    data = {
            'form': form,
            'error': error,
            'link': link
        }

    return render(request, 'main/main.html', data)
