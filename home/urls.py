from django.urls import path
from . import views


urlpatterns = [	
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('contact', views.contact, name='contact'),
	path('pricing', views.pricing, name='pricing'),
	path('deliver', views.delivery, name='delivery'),
	path('assembly', views.assembly, name='assembly'),
	path('returns', views.returns, name='returns'),
	]
