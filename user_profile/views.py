from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        form = request.POST
        email = form.get("email")
        password = form.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Başarıyla giriş yapıldı...")
            return redirect("/")
        if user is None:
            messages.warning(request, "Bu mail kayıtlı değil.")
            return redirect("user_profile:register")
    return render(request, "core/login.html", {})


def logout_view(request):
    logout(request)
    return redirect("/user/login")


def register_view(request):
    if request.method == "POST":
        form = request.POST
        username = form.get("email")
        password = form.get("password")
        password2 = form.get("password2")
        if password != password2:
            messages.warning(request, "Şifre eşleşmedi...")
            return redirect("user_profile:register")
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Daha önce kayıt yaptığınız için login yapıldı.")
                return redirect("/")

        user = User.objects.create_user(
            username=username, email=username, password=password
        )
        login(request, user)
        messages.success(request, "Kayıt oldunuz.")
        return redirect("/")

    return render(request, "core/login.html", {})
