import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


# Create your views here.
def hotel_image_view(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            destination = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            #destination = os.path.join(BASE_DIR, "static")
            print(destination)
            print(request.user.username)
            with open(destination+'/static/' + str(request.user)+'.png','wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)
        process(x)
    return HttpResponse("Files Uploaded!!")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
