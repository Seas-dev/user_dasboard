from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# ============================
# Renders Here
# ============================

# Home page landing
def index(request):
    request.session.setdefault('email', '')
    return render(request, 'login_app/index.html')

# Sign in page
def signin(request):
    return render(request, 'login_app/signin.html')


# Register Page
def register(request):
    return render(request, 'login_app/register.html')


# ==========================
# Redirects Here
# ==========================

# Logs the user out of the website
def logout(request):
    del request.session['email']
    return redirect('/')