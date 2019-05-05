from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import datetime

from .forms import BaseForm, UrlSnipetForm, CodeSnipetForm, FileSnipetForm
from .models import Base, UrlSnipet, CodeSnipet, FileSnipet
# Create your views here.

def get_file(request):
    if request.method == 'POST':
        form = BaseForm(request.POST)
        form0 = CodeSnipetForm(request.POST)
        form1 = UrlSnipetForm(request.POST)
        form2 = FileSnipetForm(request.POST)
        if form.is_valid():
            # snipp_name = form.cleaned_data['snipp_name']
            language = form.cleaned_data['language']
            visible = form.cleaned_data['visible']
            snip = Base(
                # snipp_name=snipp_name,
                language=language,
                # code=code,
                # file=file,
                visible=visible,
                created=datetime.datetime.now(),
            )
            snip.save()
        if form0.is_valid():
            code = form0.cleaned_data['code']
            snip0 = CodeSnipet(code=code, )
            snip0.save()
        if form1.is_valid():
            file_url = form1.cleaned_data['file_url']
            snip1 = UrlSnipet(file_url=file_url,)
            snip1.save()
        if form2.is_valid():
            try:
                file = str(request.FILES['file'].read(), 'utf-8')
            except MultiValueDictKeyError:
                file = False
            snip2 = FileSnipet(file=file,)
            snip2.save()
        return render(request, 'thanks.html', {
            'path': request.build_absolute_uri,
            # 'name': snipp_name
        })

    else:
        form = BaseForm()
        form0 = CodeSnipetForm()
        form1 = UrlSnipetForm()
        form2 = FileSnipetForm()

    return render(request, 'base.html', {
        'form': form,
        'form0': form0,
        'form1': form1,
        'form2': form2
    })


# def snip_list(request):
#     snip_l = Snipet.objects.all().filter(visible=True).order_by('-created')[:5]
#     context = {
#         'snip_l': snip_l
#     }
#     return render(request, 'snip_list.html', context)
#
#
# def snip(request, snip_slug):
#     snip = Snipet.objects.filter(snipp_name=snip_slug)
#     ctx = {
#         'snippet': snip
#     }
#     return render(request, 'snip_item.html', ctx)