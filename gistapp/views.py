from django.shortcuts import render

# Create your views here.


from django.http import HttpResponseRedirect

from .forms import Download

# def get_file(request):
#     context = {}
#     return render(request, 'base.html', context=context)



def get_file(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Download(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Download()

    return render(request, 'base.html', {'form': form})