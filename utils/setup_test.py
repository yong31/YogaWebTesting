from django.test import TestCase
from django.contrib.auth.models import User
from YogaWebsite.views import Member

class TestSetup(TestCase):

    def setUp(self):
        self.user={
            "first_name":"first_name",
            "last_name":"last_name",
            "username":"username",
            "email":"email@gmail.com",
            "password1":"password1",
            "password2":"password1",
            "gender":"gender",
            "age_group":"age_group",
            "orientation":"orientation"
        }

        self.member={
            "gender":"1",
            "age":"1",
            "orientation":"1",
            "user_id":"10"
        }

    def create_test_user(self):
        user = User.objects.create_user(
            username='username', email='email@gmail.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()
        return user

    def create_test_member(self):
        member = Member.objects.create(
            gender='1', age='1',orientation='1',user_id='10')
        member.save()
        return member
    
    def tearDown(self):
        return super().tearDown()