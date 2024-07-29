from ..serializers import RefreshTokenSerializer
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
from ..models import Identity
import datetime
import bcrypt
import base64
import time
import jwt

class Authentication:
    @classmethod
    def verifyPassword(cls, user, password):
        bPass = password.encode('utf-8')
        salt = bytes(user.hashSalt,'utf-8')
        hash = bcrypt.hashpw(bPass, salt)
        hash = hash.decode('utf-8')

        if hash==user.passwordHash:
            return True
        else:
            return False