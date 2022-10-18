from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from users.forms import UserLoginForm, UserRegistrationForm

class UserLogin(TemplateView):
    form_class = UserLoginForm
    initial = {"key": "value"}
    template_name = "users/user_login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            
            if form.is_valid():
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        print("Logged in")
                        return render(request, "users/index.html", {"username": username})
                    
                    else:
                        return render(request, self.template_name, {"form": form}) # return HttpResponse("Incorrect Username and Password")
        
        else:
            form = UserLoginForm()
        
        return render(request, self.template_name,{"form": form})

class UserRegistration(TemplateView):
    form_class = UserRegistrationForm
    initial = {"key": "value"}
    template_name = "users/user_registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect("users:user-login")
            else:
                return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})