from django.urls import path
from .views import login_view, log_out, user_register, index_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('login/', login_view, name='login-view'),
    path('logout/', log_out, name='log-out'),
    path('register/', user_register, name='register')
]
