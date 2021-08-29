from django.contrib.auth.models import User
from users.models import Reviews
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Team, Crop, EditableField
from users.models import Reviews, CustomUser
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.
def home_page(request):
    header = EditableField.objects.filter(field_id__contains="header")
    feature_1 = EditableField.objects.filter(field_id__contains="feature_1")
    feature_2 = EditableField.objects.filter(field_id__contains="feature_2")
    feature_3 = EditableField.objects.filter(field_id__contains="feature_3")
    team_member = Team.objects.all()
    about_us = EditableField.objects.filter(field_id__contains="about")
    agr_exp = EditableField.objects.filter(field_id__contains="agr_exp")
    total_crops = Crop.objects.count()
    farm_task = Task.objects.all()
    reviews = Reviews.objects.filter(location=1).order_by('-created_on')
    total_visitors = CustomUser.objects.count()
    footer = EditableField.objects.filter(field_id__contains="footer")
    form = CustomUserCreationForm()
    
    if request.method == 'GET':
        return render(
            request, 
            'comoxo_farm/index.html',
                {
                    "header":header,
                    "feature_1":feature_1,
                    "feature_2":feature_2,
                    "feature_3":feature_3,
                    "team_member":team_member,
                    "about_us":about_us,
                    "agr_exp":agr_exp,
                    "total_crops":total_crops,
                    "total_visitors":total_visitors,
                    "farm_task":farm_task,
                    "reviews":reviews,
                    "footer":footer,
                })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create(
                email=request.POST['email'],
                password=request.POST['password1'],
                full_name=request.POST['full_name'],
                country=request.POST['country'],
                birthdate=request.POST['birthdate'],
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                details=request.POST['details'],
                location=1,
                status=0
                )
                user.save()
                login(request, user)
                return redirect("users:dashboard")
            except IntegrityError:
                return render(
                    request, 
                    'comoxo_farm/index.html', 
                    {
                        "header":header,
                        "feature_1":feature_1,
                        "feature_2":feature_2,
                        "feature_3":feature_3,
                        "team_member":team_member,
                        "about_us":about_us,
                        "agr_exp":agr_exp,
                        "total_crops":total_crops,
                        "total_visitors":total_visitors,
                        "farm_task":farm_task,
                        "reviews":reviews,
                        "error":"That username has already been taken. Please choose a new username",
                        "footer":footer,
                        })
        else:
            return render(
                request,
                'comoxo_farm/index.html',
                {
                    "header":header,
                    "feature_1":feature_1,
                    "feature_2":feature_2,
                    "feature_3":feature_3,
                    "team_member":team_member,
                    "about_us":about_us,
                    "agr_exp":agr_exp,
                    "total_crops":total_crops,
                    "total_visitors":total_visitors,
                    "farm_task":farm_task,
                    "reviews":reviews,
                    "error":"Passwords did not match",
                    "footer":footer,
                })
