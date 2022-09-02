from django.contrib import admin
from  django.contrib.auth.models  import  Group
from YogaWebsite.models import YogaClass, TestResultVisitor, Member, Visitor, TestResultMember, GetInTouchContact
from django.contrib.auth.models import User

# Register your models here.

admin.site.unregister(Group)

class YogaClassAdmin(admin.ModelAdmin):
    list_display = ("name","description","image","type")

class TestResultVisitorAdmin(admin.ModelAdmin):

    list_display = ("id", "depressionLvl", "anxietyLvl","stressLvl")
    ordering = ("id",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
        
    def changelist_view(self, request, extra_context=None):

        depr_normalV = TestResultVisitor.objects.filter(depressionLvl='Normal').count()
        depr_normalM = TestResultMember.objects.filter(depressionLvl='Normal').count()

        depr_mildV = TestResultVisitor.objects.filter(depressionLvl='Mild').count()
        depr_mildM=TestResultMember.objects.filter(depressionLvl='Mild').count()

        depr_moderateV = TestResultVisitor.objects.filter(depressionLvl='Moderate').count()
        depr_moderateM = TestResultMember.objects.filter(depressionLvl='Moderate').count() 

        depr_severeV = TestResultVisitor.objects.filter(depressionLvl='Severe').count()
        depr_severeM = TestResultMember.objects.filter(depressionLvl='Severe').count() 

        depr_extremeV = TestResultVisitor.objects.filter(depressionLvl='Extremely Severe').count()
        depr_extremeM = TestResultMember.objects.filter(depressionLvl='Extremely Severe').count()

        anx_normalV = TestResultVisitor.objects.filter(anxietyLvl='Normal').count()
        anx_normalM = TestResultMember.objects.filter(anxietyLvl='Normal').count()

        anx_mildV = TestResultVisitor.objects.filter(anxietyLvl='Mild').count()
        anx_mildM = TestResultMember.objects.filter(anxietyLvl='Mild').count()

        anx_moderateV = TestResultVisitor.objects.filter(anxietyLvl='Moderate').count()
        anx_moderateM = TestResultMember.objects.filter(anxietyLvl='Moderate').count()

        anx_severeV = TestResultVisitor.objects.filter(anxietyLvl='Severe').count()
        anx_severeM = TestResultMember.objects.filter(anxietyLvl='Severe').count()

        anx_extremeV = TestResultVisitor.objects.filter(anxietyLvl='Extremely Severe').count()
        anx_extremeM = TestResultMember.objects.filter(anxietyLvl='Extremely Severe').count()


        stress_normalV = TestResultVisitor.objects.filter(stressLvl='Normal').count()
        stress_normalM = TestResultMember.objects.filter(stressLvl='Normal').count()

        stress_mildV = TestResultVisitor.objects.filter(stressLvl='Mild').count()
        stress_mildM = TestResultMember.objects.filter(stressLvl='Mild').count()

        stress_moderateV = TestResultVisitor.objects.filter(stressLvl='Moderate').count()
        stress_moderateM = TestResultMember.objects.filter(stressLvl='Moderate').count()

        stress_severeV = TestResultVisitor.objects.filter(stressLvl='Severe').count()
        stress_severeM = TestResultMember.objects.filter(stressLvl='Severe').count()

        stress_extremeV = TestResultVisitor.objects.filter(stressLvl='Extremely Severe').count()
        stress_extremeM = TestResultMember.objects.filter(stressLvl='Extremely Severe').count()

        extra_context = extra_context or {'depr_normal':depr_normalV+depr_normalM,'depr_mild':depr_mildV+depr_mildM,
        'depr_moderate':depr_moderateV+depr_moderateM,'depr_severe':depr_severeV+depr_severeM,'depr_extreme':depr_extremeV+depr_extremeM,
        'anx_normal':anx_normalV+anx_normalM,'anx_mild':anx_mildV+anx_mildM,'anx_moderate':anx_moderateV+anx_moderateM,
        'anx_severe':anx_severeV+anx_severeM,'anx_extreme':anx_extremeV+anx_extremeM,'stress_normal':stress_normalV+stress_normalM,
        'stress_mild':stress_mildV+stress_mildM,'stress_moderate':stress_moderateV+stress_moderateM,
        'stress_severe':stress_severeV+stress_severeM,'stress_extreme':stress_extremeV+stress_extremeM}

        extra_context['title'] = 'Overall Depression, Anxiety and Stress Results'
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    change_list_template = 'change_list_graph.html'
    

class VisitorAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "gender","age","orientation","depressionLvl","anxietyLvl","stressLvl")

    def depressionLvl(self, visitor_id):
        depr = TestResultVisitor.objects.select_related().filter(visitor=visitor_id).values_list('depressionLvl',flat=True)
        return list(depr)

    depressionLvl.short_description = 'Depression Level'

    def anxietyLvl(self, visitor_id):
        anx = TestResultVisitor.objects.select_related().filter(visitor=visitor_id).values_list('anxietyLvl',flat=True)
        return list(anx)

    anxietyLvl.short_description = 'Anxiety Level'

    def stressLvl(self, visitor_id):
        stress = TestResultVisitor.objects.select_related().filter(visitor=visitor_id).values_list('stressLvl',flat=True)
        return list(stress)

    stressLvl.short_description = 'Stress Level'

    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class MemberAdmin(admin.ModelAdmin):

    list_display = ("username", "email", "gender","age","orientation","depressionLvl","anxietyLvl","stressLvl")

    def username(self, user_id):
        username = User.objects.select_related().filter(member=user_id).values_list('username',flat=True)
        return list(username)
    
    def email(self, user_id):
        email = User.objects.select_related().filter(member=user_id).values_list('email',flat=True)
        return list(email)

    def depressionLvl(self, member_id):
        depr = TestResultMember.objects.select_related().filter(member=member_id).values_list('depressionLvl').latest('submit_datetime')
        return list(depr)

    depressionLvl.short_description = 'Depression Level'

    def anxietyLvl(self, member_id):
        anx = TestResultMember.objects.select_related().filter(member=member_id).values_list('anxietyLvl').latest('submit_datetime')
        return list(anx)

    anxietyLvl.short_description = 'Anxiety Level'

    def stressLvl(self, member_id):
        stress = TestResultMember.objects.select_related().filter(member=member_id).values_list('stressLvl').latest('submit_datetime')
        return list(stress)

    stressLvl.short_description = 'Stress Level'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class GetInTouchContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","subject","message")
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(TestResultVisitor,TestResultVisitorAdmin)
admin.site.register(YogaClass,YogaClassAdmin)
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(GetInTouchContact,GetInTouchContactAdmin)


