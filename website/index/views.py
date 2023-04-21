from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
from django.contrib import messages
from .models import Profile,Chapter,Comment,Image,Img
from django.contrib.auth.models import User

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

class DetailChapter(View):
    model = Chapter
    template_name = 'index/detail_chapter.html'
    
    def get(self, request, pk):
        x = Chapter.objects.get(id=pk)
        images = Image.objects.filter(chapter=x)
        comments = Comment.objects.filter(chapter=x).order_by('-created_at')
        text = Chapter.text
        context = {
            'chapters': Chapter.objects.all(),
            'chapter': x,
            'images': images,
            'comments': comments,
            }
        return render(request, self.template_name, context)

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