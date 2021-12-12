from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("res_system.urls", namespace="res_system")),

    # blog url
    path("blog/", include("blog.urls", namespace="blog")),

    # auth urls
    path("users/", include("users.urls", namespace="users")),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

    path("password-reset/", user_views.password_reset_request, name="password_reset"),
    path("password-reset-done/", 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name="password_reset_confirm"),
    path("password-reset-complete/", 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name="password_reset_complete"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)