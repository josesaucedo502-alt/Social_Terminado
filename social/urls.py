from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('', views.pag1, name='pag1'),
	path('perfil/', views.perfil, name='perfil'),
	path('perfil/<str:username>/', views.perfil, name='perfil'),
	path('registro/', views.registro, name='registro'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('seguir/<str:username>/', views.seguir, name='seguir'),
	path('noseguir/<str:username>/', views.noseguir, name='noseguir'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)