


from django.urls import path,include
from . import views

app_name="quizapp"
urlpatterns = [
    path('user/register/',views.UserView.as_view(),name='register'),
    path('books',views.BookView.as_view(),name='books'),
    path('employees',views.EmployeeView.as_view(),name='employees'),
    path('companys',views.CompanyView.as_view(),name='companys'),
]
