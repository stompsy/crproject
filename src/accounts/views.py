from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
    return render(request, 'pages/accounts/login.html', {})

def logout_view(request):
    
    return render(request, 'pages/accounts/logout.html', {})

def register_view(request):
    
    return render(request, 'pages/accounts/register.html', {})