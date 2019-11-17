from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.login_app.models import User
import bcrypt

# TODO: start creating users, then you can move on to the dashboard, make sure to hash those PWs when you create and set the user_level


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

# Create a new User
def createUser(request):
    errors = User.objects.regValidator(request.POST)

    if len(errors) > 0:
        # pass all the errors into messages and redirect to the registration page
        for value in errors.values():
            messages.error(request, value)
        return redirect('/register')

    else:
        # if there are no other users in the database, add them to admin level 9, and redirect them to /dashboard/admin
        num_users = User.objects.all().count()
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        # interrupted to take the assessment
        print("count", num_users)
        if num_users == 0:
            # give this user user_level 9 (admin status)
            User.objects.create(email=request.POST['email'],
                                first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                )
            pass
        else:
            # create a user with user_level 1
            pass
    print("user sucesfully created!")
    # all other accounts should be redirects to /dashboard
    return redirect('/')

# Log in the user
def loginUser(request):
    errors = User.objects.loginValidator(request.POST)

    if len(errors) > 0:
        # pass all the errors into messages and redirect to the registration page
        for value in errors.values():
            messages.error(request, value)
        return redirect('/signin')

    # if the user is an admin, redirect them to /dashboard/admin
    # otherwise, the user is directed to /dashboard
    return redirect('/')