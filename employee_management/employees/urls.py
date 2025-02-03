from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),

    # Department URLs
    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department_detail'),

    # Position URLs
    path('positions/', views.PositionList.as_view(), name='position_list'),
    path('positions/<int:pk>/', views.PositionDetail.as_view(), name='position_detail'),
]
