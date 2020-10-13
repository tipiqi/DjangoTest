from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login  # 引入内部的用户管理和用户认证
from .forms import LoginForm, RegistrationForm, UserProfileForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 校验前端提交到后端的数据是否符合表单类属性要求，检验数据是否合法
            cd = login_form.cleaned_data  # cleand_date是实例的属性，以字典形式返回实例的具体数据，校验数据格式是否合法
            user = authenticate(username=cd["username"], password=cd['password'])
            #  authenticate 校验此用户是否为本网站项目的用户，以及密码是否正确，成功返回实例，失败返回NOne
            if user:
                login(request, user)
                return HttpResponse("wellcome you ,欢迎您，authenticated successfully")
            else:
                return HttpResponse("sorry ,you username or password is not right")
        else:
            return HttpResponse("Invalid login,,")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("success")
        else:
            return HttpResponse("sorry ,your can not register,")
    else:
        user_form = RegistrationForm(request.GET)
        userprofile_form = UserProfileForm(request.GET)
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})
