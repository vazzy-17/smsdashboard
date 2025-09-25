from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Admin,Company_group
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

def home(request):
   return render(request, 'dashboard/home.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Username atau password salah'})
    
    return render(request, 'dashboard/login.html', {
        'error' : 'Username atau password salah' if error else None,
        'now' : datetime.now().year
    })

@login_required
def home_view(request):
    return render(request, 'dashboard/home.html', {
        'now':datetime.now().year
    })

def logout_view(request):
    logout(request)
    return redirect('login')

# crud admin
@login_required
def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_noc/admin_list.html', {
        'admins' : admins,
        'now' : datetime.now().year
    })
@login_required
def admin_add(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = make_password(request.POST['password']).encode()
        role = request.POST['role']
        try:
            Admin.objects.create(username=username, password=password, role=role)
            return redirect('admin_list')
        except Exception as e:
            error = f'Terjadi kesalahan: {e}'

    return render(request, 'admin_noc/admin_form.html',{
        'action': 'Tambah',
        'error': error,
        'now': datetime.now().year
    })
@login_required
def admin_edit(request, admin_id):
    admin_obj = get_object_or_404(Admin, id=admin_id)
    error = None
    if request.method == 'POST':
        admin_obj.username = request.POST['username']
        if request.POST['password']:
            admin_obj.password = make_password(request.POST['password'])
        admin_obj.role = request.POST['role']
        admin_obj.save()
        return redirect('admin_list')
    
    return render(request, 'admin_noc/admin_form.html',{
        'action':'Edit',
        'admin': admin_obj,
        'error': error,
        'now': datetime.now().year
    })
@login_required
def admin_delete(request, admin_id):
    admin_obj = get_object_or_404(Admin, id=admin_id)
    admin_obj.delete()
    return redirect('admin_list')

# crud account_group
@login_required
def company_list(request):
    company_groups = Company_group.objects.all()
    return render(request,'company/list.html', {
        'company_groups' : company_groups,
        'now' : datetime.now().year
    })
@login_required
def company_add(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        status = request.POST['status']
        email = request.POST['email']
        phone = request.POST['phone']
        try:
            Company_group.objects.create(username=username, status=status, email=email, phone=phone)
            return redirect('company_list')
        except Exception as e:
            error = f'Terjadi kesalahan: {e}'

    return render(request,'company/new.html', {
        'action':'Tambah',
        'error':error,
        'now':datetime.now().year
        })
@login_required
def company_edit(request, company_id):
    company_obj = get_object_or_404(Company_group, id = company_id)
    error = None
    if request.method == 'POST':
        company_obj.username = request.POST['username']
        company_obj.status = request.POST['status']
        company_obj.email = request.POST['email']
        company_obj.phone = request.POST['phone']
        company_obj.save()
        return redirect('company_list')
    return render(request,'company/new.html',{
        'action':'Edit',
        'company':company_obj,
        'error':error,
        'now':datetime.now().year
    })
@login_required
def company_delete(request, company_id):
    company_obj = get_object_or_404(Company_group, id=company_id)
    company_obj.delete()
    return redirect('company_list')