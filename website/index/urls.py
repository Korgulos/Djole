from django.urls import path
from . import views

#app_name = 'index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('chapter/<int:pk>', views.DetailChapter.as_view(), name='detail_chapter'),
    path('chapter/<int:pk>/comment', views.CommentCreate.as_view(), name='chapter_comment_create'),
    path('signout', views.signout_user, name='signout'),
    path('signin/', views.signin_user, name='signin'),
    path('onama', views.OnamaView.as_view(), name='onama'),
    path('mesnazajednica', views.MesnazajednicaView.as_view(), name='mesnazajednica'),
    path('lokacija', views.LokacijaView.as_view(), name='lokacija'),
    path('istorija', views.IstorijaView.as_view(), name='istorija'),
    path('stanovnistvo', views.StanovnistvoView.as_view(), name='stanovnistvo'),
    path('zeokekrozvremeiprostor', views.ZeokekrozvremeiprostorView.as_view(), name='zeokekrozvremeiprostor'),
    path('galerija', views.GalerijaView.as_view(), name='galerija'),
    path('zaprati', views.ZapratiView.as_view(), name='zaprati'),
    path('urediknjigu', views.UrediknjiguView.as_view(), name='urediknjigu'),
]
