import random
import string
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'layout.html')

def password(request):
    characters= list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        characters.append(string.ascii_uppercase)
    if request.GET.get('numbers'):
        characters.append(string.digits)
    if request.GET.get("symbols"):
        characters.extend(string.punctuation)
        
    length = int(request.GET.get('length',12))
    generated_password = "".join(random.choice(characters) for _ in range(length))

    return render(request,'password.html',{'password':generated_password})
    