from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse('true', safe=False)
        else:
            return JsonResponse('false', safe=False)
    else:
        return render(request, 'signin/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return JsonResponse('user', safe=False)
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname)
                user.save()
                print('user created')
                return JsonResponse('true', safe=False)

        else:
            return JsonResponse('false', safe=False)
    else:
        return render(request, 'signup/signup.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect(login)


def admin_sign_in(request):
    if request.session.has_key('password'):
        return redirect(admin_home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            request.session['password'] = password
            return JsonResponse('true', safe=False)
        else:
            return JsonResponse('false', safe=False)
    else:
        return render(request, 'adminsignin/adminsignin.html')


def admin_home(request):
    if request.session.has_key('password'):
        user = User.objects.all()
        return render(request, 'adminhome/adminhome.html', {'user': user})
    else:
        return redirect(admin_sign_in)


def admin_logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(admin_sign_in)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(admin_home)


def edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['username']
        user.save()
        return redirect(admin_home)
    else:
        user=User.objects.get(id=id)
        return render(request, 'edit/edit.html',{'user':user})



