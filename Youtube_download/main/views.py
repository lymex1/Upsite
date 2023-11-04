from django.shortcuts import render, redirect
from .forms import LinkForm
import webbrowser

def up_text(request):
    error = ''
    link = ''
    result = 'sd'
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            webbrowser.open(link)
            form = LinkForm()
            result = 'Вы перешли по ссылке'
        else:
            error = 'Форма была неверной'
    form = LinkForm()
    data = {
            'form': form,
            'error': error,
            'link': link,
            'result': result
        }

    return render(request, 'main/main.html', data)
