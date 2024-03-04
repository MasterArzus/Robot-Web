from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import ListView

from .models import TestUser, CustomUser
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from robot_web import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def admin_home(request):
    user_count = TestUser.objects.all().count()
    users = TestUser.objects.all()

    context = {
        "user_count": user_count,
        "users": users,

    }
    return render(request, "admin_templates/home_content.html", context)


def personal_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user
    }
    return render(request, 'admin_templates/personal_profile.html', context)
