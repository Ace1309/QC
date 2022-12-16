from django.shortcuts import render, redirect
from .forms import CallCheckForm


def index_page(request):
    return render(request, 'index.html')


def add_call(request):
    #error = ''
    form = CallCheckForm
    if request.method == 'POST':
        form = CallCheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            #error = 'This call record is already exit in database'
    data = {
        'form': form
        #'error': error
    }

    return render(request, 'add_call.html', data)

