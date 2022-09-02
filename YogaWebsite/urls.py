from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('', views.index, name='index'),
    path('yogaclass', views.yogaclass, name='yogaclass'),
    path('examine_DAS',views.examine_DAS,  name='examine_DAS'),
    path('DAS_result', views.DAS_result, name='DAS_result'),
#    path('admin/YogaWebsite/testresultvisitor', views.TestResultVisitor, name='testresultvisitor'),
#    path('testchart', testchart.as_view(), name='testchart'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('account', views.account, name='account'),
    path('result_records', views.result_records, name='result_records'),
    path('password_change', ChangePasswordView.as_view(), name='password_change'),
   # path('testresult', views.TestResultVisitor, name='testresult'),
    path('contact', views.contact, name='contact'),
]
