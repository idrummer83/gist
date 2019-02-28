from django.shortcuts import render

from .forms import Download
from .models import Snipet
# Create your views here.

def get_file(request):
    if request.method == 'POST':
        form = Download(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            file = form.cleaned_data['file']
            link = form.cleaned_data['link']

            snip = Snipet(
                language=language,
                code=code,
                file=file,
                link=link,
            )
            snip.save()
            return render(request, 'thanks.html')
    else:
        form = Download()

    return render(request, 'base.html', {'form': form})