from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser, Reviews
from .forms import CustomUserCreationForm, CustomUserChangeForm, ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    user = request.user
    if user.status == 1:
        return redirect("users:review_add")
    else:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return render(request, 'users/home.html', {'form':CustomUserChangeForm(), 'success':'Your changes has been saved.',})
            else:
                return render(request, 'users/home.html', {'form':CustomUserChangeForm(), 'error':'Your changes has not been saved.',})
        else:
            return render(request, 'users/home.html', {'form':CustomUserChangeForm()})

@login_required
def review_add(request):
    already_reviewed = Reviews.objects.filter(author=request.user).count()
    if already_reviewed >= 1:
        return redirect("users:review_update")
    else:
        print(already_reviewed)
        if request.method == 'GET':
            return render(request, 'users/review_add.html', {'form':ReviewForm()})
        else:
            try:
                form = ReviewForm(request.POST, request.FILES)
                new_review = form.save(commit=False)
                new_review.author = request.user
                new_review.save()
                return render(request, 'users/home.html', {'form':ReviewForm(), 'success':'Your review has been added'})
            except ValueError:
                return render(request, 'users/review_add.html', {'form':ReviewForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def review_update(request):
    review_approved = Reviews.objects.filter(author=request.user, status=1).count()
    last_review = Reviews.objects.all()[:1]
    last_review_item = get_object_or_404(Reviews, author=request.user)
    if review_approved == 1:
        return redirect("users:thank_you")
    else:
        if request.method == 'GET':
            return render(request, 'users/review_update.html', {'form':ReviewForm(),'last_review':last_review})
        else:
            try:
                form = ReviewForm(request.POST, request.FILES, )
                edit_review = form.save(commit=False)
                edit_review.author = request.user
                edit_review.save()
                return render(request, 'users/review_update.html', {'form':ReviewForm(), 'last_review':last_review, 'success':'Your review has been added'})
            except ValueError:
                return render(request, 'users/review_update.html', {'form':ReviewForm(), 'last_review':last_review, 'error':'Bad data passed in. Try again.'})

@login_required
def thank_you(request):
    return render(request,'users/thank_you.html')

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users:sign_in')

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'users/sign_in.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/sign_in.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('users:dashboard')