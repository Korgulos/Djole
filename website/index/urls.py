from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('chapter/<int:pk>', views.DetailChapter.as_view(), name='detail_chapter'),
    path('signout', views.signout_user, name='signout'),
    path('signin/', views.signin_user, name='signin'),
]
