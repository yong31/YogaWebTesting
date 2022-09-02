from django.test import SimpleTestCase
from django.urls import reverse,resolve
from YogaWebsite.views import index, yogaclass,examine_DAS,DAS_result,login,register,logout,account,ChangePasswordView,result_records

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_yogaclass_url_is_resolved(self):
        url = reverse('yogaclass')
        self.assertEquals(resolve(url).func, yogaclass)

    def test_examine_DAS_url_is_resolved(self):
        url = reverse('examine_DAS')
        self.assertEquals(resolve(url).func, examine_DAS)

    def test_DAS_result_url_is_resolved(self):
        url = reverse('DAS_result')
        self.assertEquals(resolve(url).func, DAS_result)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_account_url_is_resolved(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func, account)

    def test_password_change_url_is_resolved(self):
        url = reverse('password_change')
        self.assertEquals(resolve(url).func.view_class, ChangePasswordView)

    def test_result_records_url_is_resolved(self):
        url = reverse('result_records')
        self.assertEquals(resolve(url).func, result_records)