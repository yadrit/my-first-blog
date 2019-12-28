from django.http import HttpResponse
from django.shortcuts import render
import string
import random

# Create your views here.
def generate_password(request):
    return HttpResponse(''.join(
        random.choice(string.ascii_lowercase)
        for _ in range(10)
    ), status=201)