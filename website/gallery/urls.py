from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('galerije', views.GalleryView.as_view(), name='gallery'),
    path('fotografije', views.PicturesView.as_view(), name='pictures'),
    path('karte', views.MapsView.as_view(), name='karte'),
    path('video', views.VideoView.as_view(), name='video'),
    path('mojefotografije', views.YourPicturesView.as_view(), name='mojefotografije'),
]
