"""
Author: CL
Time：2023-10-16 22:50
"""
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.db.models import Avg, Count
from django.dispatch import receiver
from .models import TestUser, CustomUser
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture


def testuser_home(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, "user_templates/home_content.html", context)


def scoring_done(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('testuser_home')
    else:
        robot = request.POST.get('robot')
        try:
            user = CustomUser.objects.get(id=request.user.id)
            if robot == "r1":
                user.r1feeling = request.POST.get("feeling")
                user.r1score = request.POST.get("score")
            if robot == "r2":
                user.r2feeling = request.POST.get("feeling")
                user.r2score = request.POST.get("score")
            user.save()
            return redirect('statics')
        except Exception as e:
            print(str(e))
            messages.error(request, "Failed to report!")
            return redirect('testuser_home')


def statics(request):
    users = CustomUser.objects.all()
    r1_count = CustomUser.objects.aggregate(total=Count('r1score'))['total']
    r2_count = CustomUser.objects.aggregate(total=Count('r2score'))['total']

    feeling_list = ["很差", "不好", "一般", "较好", "很好"]

    # r1
    r1_feeling_list = {"很差": 0, "不好": 0, "一般": 0, "较好": 0, "很好": 0}
    for user in users:
        if user.r1feeling:
            r1_feeling_list[user.r1feeling] += 1
            # print(user.r1feeling)
    r1_feeling_count =[]
    for key in r1_feeling_list.keys():
        r1_feeling_count.append(r1_feeling_list[key])
    print(r1_feeling_count)

    # r2
    r2_feeling_list = {"很差": 0, "不好": 0, "一般": 0, "较好": 0, "很好": 0}
    for user in users:
        if user.r2feeling:
            r2_feeling_list[user.r2feeling] += 1
            # print(user.r2feeling)
    r2_feeling_count =[]
    for key in r2_feeling_list.keys():
        r2_feeling_count.append(r2_feeling_list[key])
    print(r2_feeling_count)

    r1_score = CustomUser.objects.aggregate(avg_value=Avg('r1score'))['avg_value']
    r2_score = CustomUser.objects.aggregate(avg_value=Avg('r2score'))['avg_value']

    context = {
        "r1_count": r1_count,
        "r2_count": r2_count,
        "r1_score": r1_score,
        "r2_score": r2_score,
        "users": users,
        "feeling_list": feeling_list,
        "r1_feeling_list": r1_feeling_count,
        "r2_feeling_list": r2_feeling_count,
    }
    return render(request, "user_templates/statics.html", context)
