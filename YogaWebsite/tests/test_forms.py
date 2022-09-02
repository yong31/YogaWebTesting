from django.test import TestCase
from YogaWebsite.forms import UpdateUserForm,UpdateMemberForm,ContactForm

class TestForms(TestCase):

    def test_update_user_form_valid_data(self):
        form = UpdateUserForm(data={
            'first_name':'user2',
            'last_name':'user2',
            'username':'user2',
            'email':'user2@gmail.com'
        })

        self.assertTrue(form.is_valid())
    
    def test_update_user_form_no_data(self):
        form = UpdateUserForm(data={
            'first_name':'',
            'last_name':'',
            'username':'',
            'email':''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    def test_update_member_form_valid_data(self):
        form = UpdateMemberForm(data={
            'gender':'1',
            'age':'1',
            'orientation':'1',
        })

        self.assertTrue(form.is_valid())
    
    def test_update_member_form_no_data(self):
        form = UpdateMemberForm(data={
            'gender':'',
            'age':'',
            'orientation':'',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'from_name':'ali',
            'from_email':'ali@gmail.com',
            'subject':'hello',
            'message':'asdad'
        })

        self.assertTrue(form.is_valid())
    
    def test_contact_form_no_data(self):
        form = ContactForm(data={
            'from_name':'',
            'from_email':'',
            'subject':'',
            'message':''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)