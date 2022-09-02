from django.test import TestCase
from YogaWebsite.models import YogaClass,Visitor,Member,TestResultVisitor,TestResultMember
from django.contrib.auth.models import User

class TestModels(TestCase):

    def create_test_user(self):
        user = User.objects.create_user(
            username='username', email='email@gmail.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()
        return user

    def setUp(self):
        self.yogaclass = YogaClass.objects.create(
            name='yoga example',
            description='afdafaf',
            class_details='aaaaaaaaaaaaaa',
            image='pic3.jpg',
            type='G'
        )

        self.visitor = Visitor.objects.create(
            name='visitor1',
            email='visitor1@gmail.com',
            gender='1',
            age='1',
            orientation='1'
        )

        self.resultVisitor = TestResultVisitor.objects.create(
            visitor=self.visitor,
            depressionLvl='Severe',
            anxietyLvl='Moderate',
            stressLvl='Mild',
            submit_datetime='2022-7-12 20:38:00'
        )




    def test_yogaclass_has_information_fields(self):
        entry = YogaClass(name="My entry yoga name")
        self.assertEqual(str(entry), entry.name)

    def test_visitor_has_information_fields(self):
        entry = Visitor(name="Visitor entry")
        self.assertEqual(str(entry), entry.name)

    def test_member_has_one_to_one_relationship_with_user(self):
        user = self.create_test_user()
        self.client.force_login(user)
        self.member = Member.objects.create(
            user=user,
            gender='1',
            age='1',
            orientation='1'
        )
        self.assertEqual(self.member.user.username, 'username')

    def test_visitor_has_test_result(self):
        
        self.assertEqual(self.resultVisitor.visitor.name, 'visitor1')

    def test_member_has_test_result(self):
        user = self.create_test_user()
        self.client.force_login(user)
        self.member = Member.objects.create(
            user=user,
            gender='1',
            age='1',
            orientation='1'
        )
        self.resultMember = TestResultMember.objects.create(
            user=user,
            member=self.member,
            depressionLvl='Severe',
            anxietyLvl='Moderate',
            stressLvl='Mild',
            submit_datetime='2022-7-12 20:38:00'
        )
        self.assertEqual(self.resultMember.member.gender, '1')