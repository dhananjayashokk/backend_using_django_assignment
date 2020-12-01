from django.urls import path,include
from . views import auth
from rest_framework import routers



urlpatterns = [
	path('signin', auth.signin	),
	path('signup', auth.signup	)
] 