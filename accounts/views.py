from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index_view(request):
    return redirect('/articles')

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/articles')
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     print('user: ', username)
    #     print('passw: ', password)
    #     user = authenticate(username=username, password=password)
    #     if user is None:
    #         messages.error(request, 'username yoki parol xato')
    #         return redirect('login-view')
    #     login(request, user)
    #     return redirect('/articles')
    return render(request, 'accounts/login.html', {'form':form})
def log_out(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            return redirect('/articles')    
        else :
            return redirect('/login')
    return render(request, "accounts/logout.html" , {})

def user_register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('/login')
    return render(request, 'accounts/register.html',{'form':form})
        