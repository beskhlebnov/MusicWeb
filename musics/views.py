from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from . import forms
from .forms import RegisterForm
from .models import Favorite, Song, SongForm
def favorite(request):
    fav = []
    for e in Favorite.objects.filter(user=request.user):
        fav.append(e.music)
    context = {"songs": fav, 'user': request.user, "isauth": request.user.is_authenticated, "favorites": fav,
               "isempty": len(fav) == 0}
    return render(request, 'musics/favorite.html', context)
def profile(request):
    fav = []
    if not request.user.is_authenticated:
        return redirect(loginPage)
    for i in Favorite.objects.filter(user=request.user):
        fav.append(i.music)
    context = {"songs": Song.objects.filter(loader=request.user), "favorites": fav, 'user': request.user,
               "isauth": request.user.is_authenticated}
    return render(request, 'musics/profile.html', context)
def doLogout(request):
    logout(request)
    return redirect(main)
def loginPage(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(main)
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'musics/login.html', {'form': form})
def main(request):
    fav = []
    if request.user.is_authenticated:
        for i in Favorite.objects.filter(user=request.user):
            fav.append(i.music)
    context = {'user': request.user, "isauth": request.user.is_authenticated, "favorites": fav,
               "songs": Song.objects.all()}
    return render(request, 'musics/main.html', context)
def about(request):
    context = {'user': request.user, "isauth": request.user.is_authenticated}
    return render(request, 'musics/about.html', context)
def addfavorite(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)
    music = Song.objects.filter(id=request.GET["id"]).first()
    user = request.user
    Favorite.objects.create(music=music, user=user)
    if request.GET['page'] == "favorite":
        return redirect(favorite)
    return redirect(main)
def add_music_page(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.cleaned_data["loader"] = request.user
                Song.objects.create(**form.cleaned_data)
                return redirect(profile)
            except Exception as Ex:
                print(Ex)
                form.add_error(None, 'Ошибка добавления песни')
    form = SongForm()
    return render(request, "musics/profile/profile_add_music.html",
                  {"form": form, 'user': request.user, "isauth": request.user.is_authenticated})
def delfavorite(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)
    Favorite.objects.filter(music=request.GET['id']).delete()
    return redirect(profile)
def delete(request):
    if not request.user.is_authenticated:
        return redirect(loginPage)
    Song.objects.filter(id=request.GET['id']).delete()
    return redirect(profile)
def registerPage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'musics/registration.html', {'form': form})