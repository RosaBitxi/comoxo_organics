from django.shortcuts import render, redirect
from .models import EditableField_Conga, Room
from users.models import Reviews, CustomUser
from comoxo_farm.models import EditableField
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError

def conga_page(request):
    header = EditableField_Conga.objects.filter(field_id__contains="header")
    feature_1 = EditableField_Conga.objects.filter(field_id__contains="feature_1")
    feature_2 = EditableField_Conga.objects.filter(field_id__contains="feature_2")
    feature_3 = EditableField_Conga.objects.filter(field_id__contains="feature_3")
    conga_room = Room.objects.all()
    reviews = Reviews.objects.filter(location=1).order_by('-created_on')
    footer = EditableField.objects.filter(field_id__contains="footer")
    form = CustomUserCreationForm()
    
    if request.method == 'GET':
        return render(
            request, 
            'conga_house/index2.html',
                {
                    'header':header,
                    'feature_1':feature_1,
                    'feature_2':feature_2,
                    'feature_3':feature_3,
                    'conga_room':conga_room,
                    'reviews':reviews,
                    'footer':footer,
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
                location=2,
                status=0
                )
                user.save()
                login(request, user)
                return redirect("users:dashboard")
            except IntegrityError:
                return render(
                    request, 
                    'conga_house/index2.html', 
                    {
                        'header':header,
                        'feature_1':feature_1,
                        'feature_2':feature_2,
                        'feature_3':feature_3,
                        'conga_room':conga_room,
                        'reviews':reviews,
                        'footer':footer,
                        'error':'That username has already been taken. Please choose a new username',
                        })
        else:
            return render(
                request,
                'conga_house/index2.html',
                {
                    'header':header,
                    'feature_1':feature_1,
                    'feature_2':feature_2,
                    'feature_3':feature_3,
                    'conga_room':conga_room,
                    'reviews':reviews,
                    'footer':footer,
                    'error':'Passwords did not match',
                })