from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import bcrypt
from apps.login_app.models import User
from apps.dashboard_app.models import Post, Comment
from datetime import datetime, timedelta, timezone

# Create your views here.
# ============================
# Renders Here
# ============================

# Admin Dashboard
def adminDash(request):
    user = User.objects.filter(email = request.session['email'])
    # just in case the user somehow gets to this point and not be in the system
    if len(user) < 1:
        return redirect('/logout')

    all_users = User.objects.all()
    context = {
        'users': all_users,
    }

    return render(request, 'dashboard_app/admin_dash.html', context)

def dashboard(request):
    user = User.objects.filter(email = request.session['email'])
    # just in case the user somehow gets to this point and not be in the system
    if len(user) < 1:
        return redirect('/logout')

    all_users = User.objects.all()
    context = {
        'users': all_users,
    }

    return render(request, 'dashboard_app/dashboard.html', context)

def adminAddNew(request):
    user = User.objects.filter(email = request.session['email'])
    if len(user) != 1 or user[0].user_level != 9:
        return redirect('/dashboard')
    return render(request,'dashboard_app/create_user.html')

def adminEditUser(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'dashboard_app/edit_user_admin.html', context)

def editProfile(request):
    user = User.objects.get(email=request.session['email'])
    context = {
        'user': user,
    }
    return render(request, 'dashboard_app/edit_profile.html', context)

def showUser(request,id):
    user = User.objects.get(id=id)
    messages = user.posts.all()
    context = {
        'user': user,
        'messages': messages,
    }
    return render(request, 'dashboard_app/show_messages.html', context)


# ============================
# Redirects Here
# ============================

# A switching function to direct users to the correct dashboards that they should see when they login
# Could be useful if different levels of users are added later, like moderators who can delete offensive posts but not create/delete users
def whichDash(request):
    user = User.objects.filter(email = request.session['email'])
    # just in case the user somehow gets to this point and not be in the system
    if len(user) < 1:
        return redirect('/logout')
    if user[0].user_level == 9:
        return redirect('/adminDash')
    else:
        return redirect('/dashboard')

def deleteUser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/whichDash')

def editUser(request, id):
    user = User.objects.get(id=id)
    errors = {}

    if request.POST['pw'] == 'True':
        errors = User.objects.passwordValidator(request.POST)
    else:
        errors = User.objects.editValidator(request.POST)

    
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        if request.POST['admin'] == 'True':
            return redirect('/users/edit/' + id)
        else:
            return redirect('/users/edit')

    if request.POST['pw'] == 'True':
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user.password = hash_pw.decode()
        user.save()
    else:
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.user_level = request.POST['user_level']
        user.save()


    
    return redirect('/whichDash')

def editDesc(request):
    user = User.objects.get(email=request.session['email'])
    user.description = request.POST['description']
    user.save()
    return redirect('/whichDash')

def createPost(request, id):
    author = User.objects.get(email=request.session['email'])
    user = User.objects.get(id=id)
    Post.objects.create(user=user,content=request.POST['message'],author=author)
    return redirect('/users/show/' + id)

def createComment(request,messageID):
    message = Post.objects.get(id=messageID)
    poster = User.objects.get(email=request.session['email'])
    Comment.objects.create(user=poster,post=message,content=request.POST['message'])
    return redirect('/users/show/' + str(message.user.id))