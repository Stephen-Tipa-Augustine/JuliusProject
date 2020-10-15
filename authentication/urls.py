from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
path('login/', views.login_view, name = 'login'),
    path('logout-current-user/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('sent-failed/resend-link/<str:slug>', views.resendActivationLink, name="resend-activation-link"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]