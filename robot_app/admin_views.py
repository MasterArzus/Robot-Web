from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import ListView
from django.db.models import Avg, Count
from .models import TestUser, CustomUser
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from robot_web import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def admin_home(request):
    users = CustomUser.objects.all()
    r1_count = CustomUser.objects.aggregate(total=Count('r1feeling'))['total']
    r2_count = CustomUser.objects.aggregate(total=Count('r2feeling'))['total']

    feeling_list = ["很差", "不好", "一般", "较好", "很好"]

    # r1
    r1_feeling_list = {"很差": 0, "不好": 0, "一般": 0, "较好": 0, "很好": 0}
    r1_feeling1 = [0, 0, 0, 0, 0]
    r1_feeling2 = [0, 0, 0, 0, 0]
    r1_feeling3 = [0, 0, 0, 0, 0]
    for user in users:
        if user.r1feeling:
            r1_feeling_list[user.r1feeling] += 1
        if user.r1feeling1:
            r1_feeling1[user.r1feeling1-1] += 1
        if user.r1feeling2:
            r1_feeling2[user.r1feeling2-1] += 1
        if user.r1feeling2:
            r1_feeling3[user.r1feeling3-1] += 1

    r1_feeling_count = []
    for key in r1_feeling_list.keys():
        r1_feeling_count.append(r1_feeling_list[key])
    print(r1_feeling_count)

    # r2
    r2_feeling_list = {"很差": 0, "不好": 0, "一般": 0, "较好": 0, "很好": 0}
    r2_feeling1 = [0, 0, 0, 0, 0]
    r2_feeling2 = [0, 0, 0, 0, 0]
    r2_feeling3 = [0, 0, 0, 0, 0]
    for user in users:
        if user.r2feeling:
            r2_feeling_list[user.r2feeling] += 1
        if user.r2feeling1:
            r2_feeling1[user.r2feeling1-1] += 1
        if user.r2feeling2:
            r2_feeling2[user.r2feeling2-1] += 1
        if user.r2feeling2:
            r2_feeling3[user.r2feeling3-1] += 1

    r2_feeling_count = []
    for key in r2_feeling_list.keys():
        r2_feeling_count.append(r2_feeling_list[key])
    print(r2_feeling_count)

    r1_score = 0
    sr1 = CustomUser.objects.aggregate(avg_value=Avg('r1feeling1'))['avg_value']
    sr2 = CustomUser.objects.aggregate(avg_value=Avg('r1feeling2'))['avg_value']
    sr3 = CustomUser.objects.aggregate(avg_value=Avg('r1feeling3'))['avg_value']
    if sr1 and sr2 and sr3:
        r1_score = round((sr1 + sr2 + sr3) / 3, 2)

    r2_score = 0
    sr4 = CustomUser.objects.aggregate(avg_value=Avg('r2feeling1'))['avg_value']
    sr5 = CustomUser.objects.aggregate(avg_value=Avg('r2feeling2'))['avg_value'] 
    sr6 = CustomUser.objects.aggregate(avg_value=Avg('r2feeling3'))['avg_value']
    if sr4 and sr5 and sr6:
        r2_score = round((sr4 + sr5 + sr6) / 3, 2)

    context = {
        "r1_count": r1_count,
        "r2_count": r2_count,
        "r1_score": r1_score,
        "r2_score": r2_score,
        "users": users,
        "feeling_list": feeling_list,
        "r1_feeling_list": r1_feeling_count,
        "r2_feeling_list": r2_feeling_count,
        "r1_feeling1": r1_feeling1,
        "r2_feeling1": r2_feeling1,
        "r1_feeling2": r1_feeling2,
        "r2_feeling2": r2_feeling2,
        "r1_feeling3": r1_feeling3,
        "r2_feeling3": r2_feeling3,
    }
    return render(request, "admin_templates/home_content.html", context)

