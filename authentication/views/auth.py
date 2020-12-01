from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .. models import *
from .. serializers import *
from django.contrib.auth.hashers import make_password
import json
from django.contrib.auth import authenticate




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signin(request):
	request = json.loads(request.body.decode('utf-8'))
	auth = authenticate(username=request['username'], password=request['password'])
	user = AuthUser.objects.filter(username=request['username'])
	if user:
		serializer = AuthSerializer(user, many=True)
		return Response(serializer.data)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
	form_data=request.data.copy() 
	form_data["password"]=make_password(form_data["password"])
	serializer = AuthSerializer(data=form_data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

