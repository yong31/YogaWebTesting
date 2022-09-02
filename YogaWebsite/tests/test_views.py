from distutils.log import error
from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup
from django.contrib.auth.models import User
from YogaWebsite.forms import UpdateUserForm
from YogaWebsite.models import Member

class TestViews(TestSetup):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"login.html")
    
    def test_should_signup_user(self):
        response=self.client.post(reverse("register"),self.user)
        self.assertEquals(response.status_code, 302)
        
    def test_should_not_signup_user_with_taken_username(self):
        self.user={
            "first_name":"first_name",
            "last_name":"last_name",
            "username":"username",
            "email":"email1@gmail.com",
            "password1":"password1",
            "password2":"password1",
            "gender":"gender",
            "age_group":"age_group",
            "orientation":"orientation"
        }

        self.client.post(reverse("register"),self.user)
        response=self.client.post(reverse("register"),self.user)
        self.assertEquals(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Username Taken", list(map(lambda x: x.message,storage)))

    def test_should_not_signup_user_with_taken_email(self):
        self.user={
            "first_name":"first_name",
            "last_name":"last_name",
            "username":"username",
            "email":"email1@gmail.com",
            "password1":"password1",
            "password2":"password1",
            "gender":"gender",
            "age_group":"age_group",
            "orientation":"orientation"
        }

        self.test_user2={
            "first_name":"first_name",
            "last_name":"last_name",
            "username":"username1",
            "email":"email1@gmail.com",
            "password1":"password1",
            "password2":"password1",
            "gender":"gender",
            "age_group":"age_group",
            "orientation":"orientation"
        }

        self.client.post(reverse("register"),self.user)
        response=self.client.post(reverse("register"),self.test_user2)
        self.assertEquals(response.status_code, 409)

    def test_should_not_signup_user_with_password_not_match(self):
        self.user={
            "first_name":"first_name",
            "last_name":"last_name",
            "username":"username",
            "email":"email1@gmail.com",
            "password1":"password1",
            "password2":"password2",
            "gender":"gender",
            "age_group":"age_group",
            "orientation":"orientation"
        }

        self.client.post(reverse("register"),self.user)
        response=self.client.post(reverse("register"),self.user)
        self.assertEquals(response.status_code, 409)

    def test_should_not_signup_user_with_empty_field(self):
        self.user={
            "first_name":"",
            "last_name":"",
            "username":"",
            "email":"",
            "password1":"",
            "password2":"",
            "gender":"",
            "age_group":"",
            "orientation":""
        }

        self.client.post(reverse("register"),self.user)
        response=self.client.post(reverse("register"),self.user)
        self.assertEquals(response.status_code, 409)

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"login.html")

    def test_should_login_successfully(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"),{
            'username':user.username,
            'password':'password12!'
        })
        self.assertEquals(response.status_code, 302)

    def test_should_not_login_with_invalid_username_password(self):
        response = self.client.post(reverse("login"), {
            'username': 'username123',
            'password': 'password12!32'
        })
        self.assertEquals(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn("Invalid credentials, try again",
            list(map(lambda x: x.message, storage)))

    def test_should_not_login_with_empty_field(self):
        response = self.client.post(reverse("login"),{
            'username':'',
            'password':''
        })
        self.assertEquals(response.status_code, 401)

    def test_logout(self):
        user = self.create_test_user()
        self.client.force_login(user)
        self.client.logout()
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)    

    def test_account_page_invalid_id(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code,302)

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"index.html")
    
    def test_yogaclass_page(self):
        response = self.client.get(reverse('yogaclass'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"yogaclass.html")

    def test_examine_DAS_page(self):
        response = self.client.get(reverse('examine_DAS'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"examine_DAS.html")

    def test_examine_DAS_page_submit_valid_input(self):
        response = self.client.post(reverse('DAS_result'), {
            'Q1A':'1',
            'Q2A':'1',
            'Q3A':'1',
            'Q4A':'1',
            'Q5A':'1',
            'Q6A':'1',
            'Q7A':'1',
            'Q8A':'1',
            'Q9A':'1',
            'Q10A':'1',
            'Q11A':'1',
            'Q12A':'1',
            'Q13A':'1',
            'Q14A':'1',
            'Q15A':'1',
            'Q16A':'1',
            'Q17A':'1',
            'Q18A':'1',
            'Q19A':'1',
            'Q20A':'1',
            'Q21A':'1',
            'gender':'2',
            'age_group':'2',
            'orientation':'2',
            'name':'visitor',
            'email':'visitor@gmail.com'
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"DAS_result.html")

    def test_examine_DAS_page_submit_empty_input(self):
        response = self.client.post(reverse('DAS_result'), {
            'Q1A':'',
            'Q2A':'',
            'Q3A':'',
            'Q4A':'',
            'Q5A':'',
            'Q6A':'',
            'Q7A':'',
            'Q8A':'',
            'Q9A':'',
            'Q10A':'',
            'Q11A':'',
            'Q12A':'',
            'Q13A':'',
            'Q14A':'',
            'Q15A':'',
            'Q16A':'',
            'Q17A':'',
            'Q18A':'',
            'Q19A':'',
            'Q20A':'',
            'Q21A':'',
            'gender':'2',
            'age_group':'2',
            'orientation':'2',
            'name':'visitor',
            'email':'visitor@gmail.com'
        })

        self.assertEquals(response.status_code, 409)

        
""""
    def test_account_page(self):
        user = self.create_test_user()
        self.client.force_login(user)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_account_update_details(self):
        user = self.create_test_user()
        self.client.force_login(user)
        response = self.client.post(reverse('account'), {
            'first_name':'user1',
            'last_name':'user1',
            'username':'user1',
            'email': 'updated@example.com'
        })

        self.assertEqual(response.status_code,302)
        response = self.client.get(reverse('account'))

        self.assertEqual(response.status_code,200)

        user.refresh_from_db() # here you get the latest info
        self.assertEqual(user.username,'user1')
"""