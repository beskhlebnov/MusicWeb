from MusicWeb import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path
from musics import views

urlpatterns = [
    path("admin/", admin.site.urls),

    re_path("addfavorite/", views.addfavorite),
    re_path("delfavorite/", views.delfavorite),
    re_path("favorite/", views.favorite, name="favorite"),

    re_path("logout/", views.doLogout),
    path('registration', views.registerPage, name='registration'),
    path('login/', views.loginPage, name='login'),
    re_path("login/", views.loginPage, name="loginpage"),

    re_path("about", views.about, name="about"),

    re_path("profile/", views.profile, name="profile"),
    re_path("delete/", views.delete, name="delete"),
    re_path("add_music_page/", views.add_music_page, name="add_music_page"),


    path("", views.main),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
