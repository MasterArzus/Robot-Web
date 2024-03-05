from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from robot_app.EmailBackEnd import EmailBackEnd
from robot_app.models import CustomUser, TestUser


# Create your views here.
def loginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        # user = EmailBackEnd.authenticate(request, email=request.POST.get('email'),
        #                                  password=request.POST.get('password'))
        user = EmailBackEnd.authenticate(request, email=request.POST.get('email'),
                                         password=111)
        if user != None:
            login(request, user)
            user_type = user.user_type
            # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                # return HttpResponse("TestUser Login")
                # 进行了重定向
                return redirect("testuser_home")
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            # return HttpResponseRedirect("/")
            return redirect('login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def sign_up(request):
    return render(request, 'sign_up.html')


def doRegister(request):
    if request.method != "POST":
        return HttpResponse("Register Fail!")
    else:
        # Get the post parameters
        email = request.POST.get('邮箱')
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        user_type = request.POST.get('type')
        name = request.POST.get('姓名')
        gender = request.POST.get('性别')
        job = request.POST.get('职业')
        # Check for errorneous inputs
        # if password1 != password2:
        #     messages.error(request, "Password do not match")
        #     return redirect('sign_up')

        if user_type == '1':
            try:
                user = CustomUser.objects.create_user(email=email, username=name, job=job, gender=gender,
                                                      password="111", user_type=1)
                user.save()
            except Exception as e:
                print(str(e))
                messages.error(request, "Failed to Add Admin!")
                return redirect('login')
        if user_type == '2':
            try:
                user = CustomUser.objects.create_user(email=email, username=name, job=job, gender=gender,
                                                      password="111", user_type=2)
                # testUser = TestUser.objects.create(admin=user)
                user.save()
                # testUser.save()
            except Exception as e:
                print(str(e))
                messages.error(request, "Failed to Add TestUser!")
                return redirect('login')

    messages.success(request, "Register successfully!")
    return redirect('login')
