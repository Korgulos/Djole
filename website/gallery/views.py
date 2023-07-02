from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.conf import settings
from django.contrib import messages

from .forms import ImageForm
from .models import Images

from django.core.mail import EmailMultiAlternatives
from PIL import Image



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

    def get(self, request, *args, **kwargs):
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
        imgform = ImageForm()
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all().order_by('-created_at'),
        }
        return render(request, 'gallery/your_pictures.html', context)
    
class YourPicturesCreateView( View):
    
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        imgform = ImageForm()
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'imgform': imgform,
        }
        return render(request, 'gallery/add_your_pictures.html', context)
    
    def post(self, request):
        imgform = ImageForm(request.POST, request.FILES or None)
        if imgform.is_valid(): 
            image = request.FILES['image']
            images = Images(
                name=request.POST['name'],
                image=image,
                image300=image,
                )
            try:
                mail = EmailMultiAlternatives(
                'Postavljen novi fajl', # subject
                'Poslat zahtev za postavlanje {} sa failom {}. Prati link http://127.0.0.1:8000/galerija/uredi da bi odobrio prikaz.'.format(images.name, images.image), # message
                settings.EMAIL_HOST_USER, # from email
                ['katicod100@gmail.com'], # To Email
                )
                mail.content_subtype='html'
                
                #mail.attach(image.name, image.read(), image.content_type)
                mail.send()
                images.save()
                
            except:
                
                return render(request, 'gallery/add_your_pictures.html', context)
                    
            return redirect('gallery:mojefotografije')
        context = {'imgform': imgform,}
        
        return render(request, 'gallery/add_your_pictures.html', context)


class YourPicturesEditView(LoginRequiredMixin,View):
    
    def get(self, request):
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/edit_your_pictures.html', context)

    def post(self, request):
        try:
            id = int(request.POST['id'])
        except:
            id = 0
        image = get_object_or_404(Images, id=id)
        if (request.POST['approved'] == "true"):
            image.approved = True
        elif(request.POST['approved'] == "false"):
            image.approved = False
        image.save()
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'gallery': Images.objects.all(),
        }
        return render(request, 'gallery/edit_your_pictures.html', context)
class YourPicturesDeleteView (LoginRequiredMixin, View):
    model = Images
    success_url = reverse_lazy('gallery:uredi')
    def get(self, request, pk):
        image = get_object_or_404(self.model, id=pk)
        print(image.name)
        context = {
            'image':image
        }
        return render(request, 'gallery/delete_your_pictures.html',context)

    def post(self, request, pk):
        image = get_object_or_404(self.model, id=pk)
        image.delete()
        return redirect(self.success_url)       

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