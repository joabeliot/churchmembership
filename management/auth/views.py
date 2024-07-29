from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import IdentitySerializer
from django.shortcuts import redirect
from django.views.generic import View
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from .models import Identity
import requests
import bcrypt
import uuid
import json
import os


@method_decorator(csrf_exempt, name='dispatch')
class SignInView(View):
    def post(self, request):
        # JSON load the data sent from the client throught the request body
        bodyData = json.loads(request.body)

        # Assigning the parameters from the request body to the string variables email and password 
        email = bodyData.get('email')
        password = bodyData.get('password')

        try:
            # checking the existance of the user data in db
            user = Identity.objects.get(email=email)
            # if StablishAuthentication().checkPassword(user,password): #Checking the given password to validate the user's session 
            #     #Generate Refresh and Access token after authentication
            #     refreshToken = StablishToken().RefreshToken(str(user.uid))
            #     accessToken = StablishToken().AccessToken(str(user.uid))
            #     print(f"{email} Signed in...")
            #     return JsonResponse({'message':'Signin Successful','access':str(accessToken),'refresh':str(refreshToken)},status=200)
            
            # else:
            #     #If the password is invalid
            #     return JsonResponse({'error':'Invalid Password'},status=401)
        except Identity.DoesNotExist:
            #When that user record isn't found in db in that case the user has to SignUp
            return JsonResponse({'error':'User doesnt exist'},status=404)