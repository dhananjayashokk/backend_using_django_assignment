from rest_framework import serializers
from .models import *

class AuthSerializer(serializers.ModelSerializer):
	class Meta:
		model=AuthUser
		fields=('password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined')

