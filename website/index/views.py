from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.conf import settings
from django.contrib import messages
from .models import Profile,Chapter,Comment,Image,Img
from .forms import CommentForm
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


class IndexView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/index.html', context)

class OnamaView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/onama.html', context)

class MesnazajednicaView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/mesnazajednica.html', context)

class LokacijaView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/lokacija.html', context)

class IstorijaView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/istorija.html', context)

class StanovnistvoView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/stanovnistvo.html', context)

class ZeokekrozvremeiprostorView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/zeokekrozvremeiprostor.html', context)

class GalerijaView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/galerija.html', context)

class ZapratiView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/zaprati.html', context)

class UrediknjiguView(View):

    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'chapters': Chapter.objects.all(),
        }
        return render(request, 'index/urediknjigu.html', context)


class DetailChapter(View):
    model = Chapter
    template_name = 'index/detail_chapter.html'

    def get(self, request, pk):
        x = get_object_or_404(Chapter, id=pk)
        images = Image.objects.filter(chapter=x)
        comments = Comment.objects.filter(chapter=x).order_by('-created_at')
        text = Chapter.text
        comm = CommentForm
        context = {
            'chapters': Chapter.objects.all(),
            'chapter': x,
            'images': images,
            'comments': comments,
            'CommentForm': comm,
            }
        return render(request, self.template_name, context)

class CommentCreate(View):

    def post(self, request, pk):
        f = get_object_or_404(Chapter, id=pk)
        comment= Comment(
            name=request.POST['name'],
            chapter=f,
            image=request.FILES.get('image', None),
            text=request.POST['text'],
        )
        comment.save()
        return redirect(reverse('index:detail_chapter',args=[pk]))

def signout_user(request):
	logout(request)
	messages.success(request, ("You Have Been Logged Out."))
	return redirect('index')

def signin_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You Have Been Logged In!"))
			return redirect('index')
		else:
			messages.success(request, ("There was an error logging in. Please Try Again..."))
			return redirect('signin')

	else:
		return render(request, "signin.html", {})