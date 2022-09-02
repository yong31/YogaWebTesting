from django.test import TestCase
from YogaWebsite.models import YogaClass, TestResultVisitor, Member, Visitor, TestResultMember
from django.contrib.admin.sites import AdminSite
from YogaWebsite.admin import MemberAdmin, TestResultVisitorAdmin, VisitorAdmin

class MockRequest:
    pass

request = MockRequest()


class ModelAdminTest(TestCase):

    def setUp(self):
        self.visitorAdmin=VisitorAdmin(model=Visitor,admin_site=AdminSite())
        self.memberAdmin=MemberAdmin(model=Member,admin_site=AdminSite())
        self.testResultVisitorAdmin=TestResultVisitorAdmin(model=TestResultVisitor,admin_site=AdminSite())

    
    def test_had_add_permission(self):
        self.assertEquals(self.visitorAdmin.has_add_permission(request),False)
        self.assertEquals(self.memberAdmin.has_add_permission(request),False)
        self.assertEquals(self.testResultVisitorAdmin.has_add_permission(request),False)


    def test_had_change_permission(self):
        self.assertEquals(self.visitorAdmin.has_change_permission(request),False)
        self.assertEquals(self.memberAdmin.has_change_permission(request),False)







