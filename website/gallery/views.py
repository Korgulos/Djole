from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.conf import settings
from django.contrib import messages
from .models import Images

from django.contrib.auth.models import User

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.utils import IntegrityError


# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class GalleryView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/galerija.html', context)

class PicturesView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/pictures.html', context)

class MapsView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/maps.html', context)
    
class YourPicturesView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/your_pictures.html', context)
    
class VideoView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/video.html', context)