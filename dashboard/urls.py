from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),

    # crud admin
    path('admin_noc/list/', views.admin_list, name='admin_list'),
    path('admin_noc/add/', views.admin_add, name='admin_add'),
    path('admin_noc/edit/<int:admin_id>', views.admin_edit, name='admin_edit'),
    path('admin_noc/delete/<int:admin_id>', views.admin_delete, name='admin_delete'),

    # crud company client
    path('company/list/', views.company_list, name='company_list'),
    path('company/add/', views.company_add, name='company_add'),
    path('company/edit/<int:company_id>', views.company_edit, name='company_edit'),
    path('company/delete/<int:company_id>', views.company_delete, name='company_delete'),
    ]