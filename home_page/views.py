from django.shortcuts import render,redirect
from django.http import *
from .models import *
from .forms import *
from .models import ContactForm as ContactModel

# def view1(request):
#     return render(request, 'startTOend.html')
#     # return render(request, 'temp-new-chart.html')


# def index(request):
#     return render(request, 'startTOend.html')


def blog(request):
    return render(request, "blog-single.html")


def CommingSoon(request):
    return render(request, "CommingSoon.html")

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/home/')
            # return redirect('success')
            return HttpResponseRedirect('/homeMessageSucess/')


    else:
        form = ContactForm()
    return render(request, 'startTOend.html', {'form': form})

#
# def conformMessage(request):
#     obj = ContactModel.objects.all()
#     return render(request, 'email.html', {'obj': obj})


# def contact(request):
#     return render(request,'contact.html')

def homeMessageSucess(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/home/')
            # return redirect('success')
            return HttpResponseRedirect('/homeMessageSucess/')

    else:
        form = ContactForm()
    return render(request, 'homeMessageSucess.html', {'form': form})
