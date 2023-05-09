from django.urls import include, path,re_path
from django.views.generic import TemplateView
from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    # URLs that do not require a session or valid token
    re_path(r'^auth/password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    re_path(r'^auth/password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    re_path(r'^auth/login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    re_path(r'^auth/logout/$', LogoutView.as_view(), name='rest_logout'),
    re_path(r'^auth/user/$', UserDetailsView.as_view(), name='rest_user_details'),
    re_path(r'^auth/password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
    re_path(r'^auth/register/$', RegisterView.as_view(), name='rest_register'),
    re_path(r'^auth/register/verify-email/$', VerifyEmailView.as_view(), name='rest_verify_email'),
    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
    re_path(r'^auth/register/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
]

