from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from EcomApp.models import Setting
from Product.models import Category, Comment
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'user_img/default.jpg'
            data.save()

            return redirect('home')
        # else:
        #     messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'setting' : setting,
        'category' : category,
        'form' : form,
    }
    return render(request, 'user_signup.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
             messages.warning(request, "Username or Password is Wrong!!")
    
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)

    context = {
        'setting' : setting,
        'category' : category,
    }
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_profile(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {
        'setting' : setting,
        'category' : category,
        'profile' : profile,
    }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/user/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Account has been Updated!")
            return redirect('user_profile')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance= request.user.userprofile)
        context ={
            'setting' : setting,
            'category' : category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'userupdate.html', context)


@login_required(login_url='/user/login')  # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password has been successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('user_password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'userpasswordupdate.html', {'form': form,
                                                           'category': category,
                                                           'setting': setting,
                                                           })


@login_required(login_url='/user/login')
def usercomment(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'comment': comment

    }
    return render(request, 'usercomment.html', context)


def comment_delete(request, id):
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id, id=id)
    comment.delete()
    messages.success(request, 'Your comment is successfully deleted')
    return redirect('usercomment')