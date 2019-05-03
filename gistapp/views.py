from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import datetime

from .forms import Download
from .models import Snipet
# Create your views here.

def get_file(request):
    if request.method == 'POST':
        form = Download(request.POST)
        if form.is_valid():
            snipp_name = form.cleaned_data['snipp_name']
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            try:
                file = str(request.FILES['file'].read(), 'utf-8')
            except MultiValueDictKeyError:
                file = False
            visible = form.cleaned_data['visible']
            snip = Snipet(
                snipp_name=snipp_name,
                language=language,
                code=code,
                file=file,
                visible=visible,
                created=datetime.datetime.now(),
            )
            snip.save()
            return render(request, 'thanks.html', {
                'path': request.build_absolute_uri,
                'name': snipp_name
            })
    else:
        form = Download()

    return render(request, 'base.html', {'form': form})


def snip_list(request):
    snip_l = Snipet.objects.all().filter(visible=True).order_by('-created')[:5]
    context = {
        'snip_l': snip_l
    }
    return render(request, 'snip_list.html', context)


def snip(request, snip_slug):
    snip = Snipet.objects.filter(snipp_name=snip_slug)
    ctx = {
        'snippet': snip
    }
    return render(request, 'snip_item.html', ctx)