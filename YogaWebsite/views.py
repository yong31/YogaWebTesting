from queue import Empty
from django.shortcuts import render, redirect
from numpy import integer
from django.contrib.auth.models import User, auth
from django.contrib import messages
from YogaWebsite.models import Member, GetInTouchContact,TestResultMember, YogaClass, Visitor, TestResultVisitor
from .forms import UpdateUserForm,UpdateMemberForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

import joblib
import pandas as pd


reloadModel=joblib.load('./models/Depr_KNN.pkl')
reloadModel2=joblib.load('./models/Anx_RF.pbz2')
reloadModel3=joblib.load('./models/Stress_LR.pkl')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if username and password is not None:
            if user is not None:
                auth.login(request,user)
                return redirect("/",status=302)
            else:
                messages.info(request,'Invalid credentials, try again')
                return render(request,'login.html',status=401)
        else:
            messages.info(request,'Field cannot be empty!')
            return render(request,'login.html',status=401)
    
    return HttpResponse("login.html")

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gender=request.POST.get('gender')
        age_group=request.POST.get('age_group')
        orientation=request.POST.get('orientation')

        if first_name and last_name and username and email and password1 and password2 is not Empty:
            if password1 != password2:
                messages.info(request,'Password Not Matching')
                return render(request,'login.html',status=409)

            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'login.html',status=409)
                    
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'login.html',status=409)

            user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name,last_name=last_name)
            user.save()
            member = Member(gender=gender, age=age_group, orientation=orientation, user_id=user.id)
            member.save()
            messages.info(request,'Congratz! Account created successfully.')
            return render(request,'login.html',status=302)
        else:
            messages.info(request,'Field cannot be empty!')
            return render(request,'login.html',status=409)

    return render(request,'login.html')                
    


def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url='login')
def account(request):
    user = request.user
    member_info = Member.objects.get(user_id=user.id)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)
        member_form = UpdateMemberForm(request.POST, instance=member_info)
       

        if user_form.is_valid():
            user_form.save()

        if member_form.is_valid():
            member_form.save()
            
        if user_form.is_valid() or member_form.is_valid():
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='account')

    else:
        user_form = UpdateUserForm(instance=request.user)
        member_form = UpdateMemberForm(instance=member_info)

    context={'user_form': user_form,'member_form':member_form,'member_info':member_info}
    return render(request, 'account.html', context)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('account')
    success_message = "Successfully Changed Your Password"



@login_required(login_url='login')
def result_records(request):
    user = request.user

    results = TestResultMember.objects.filter(user_id=user.id)

    context={'results':results}
    return render(request, 'result_records.html', context)


def index(request):

    classes = YogaClass.objects.all()

    return render(request, 'index.html', {'classes':classes})

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = GetInTouchContact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.info(request,'Congratz! Account created successfully.')
        return render(request,'index.html',status=302)

def yogaclass(request):

    classes = YogaClass.objects.all()

    return render(request, 'yogaclass.html', {'classes':classes})


def DAS_result(request):
    print(request)
    user = request.user
    member = Member.objects.filter(user_id=user.id).values('gender')    
    member_id = Member.objects.filter(user_id=user.id).values('id')

    if request.method == 'POST':
        depr={}
        depr['Q3A']=request.POST.get('Q3A')
        depr['Q5A']=request.POST.get('Q5A')
        depr['Q10A']=request.POST.get('Q10A')
        depr['Q13A']=request.POST.get('Q13A')
        depr['Q16A']=request.POST.get('Q16A')
        depr['Q17A']=request.POST.get('Q17A')
        depr['Q21A']=request.POST.get('Q21A')
        depr['gender']=request.POST.get('gender')
        depr['age_group']=request.POST.get('age_group')
        depr['orientation']=request.POST.get('orientation')

        anx={}
        anx['Q2A']=request.POST.get('Q2A')
        anx['Q4A']=request.POST.get('Q4A')
        anx['Q7A']=request.POST.get('Q7A')
        anx['Q9A']=request.POST.get('Q9A')
        anx['Q15A']=request.POST.get('Q15A')
        anx['Q19A']=request.POST.get('Q19A')
        anx['Q20A']=request.POST.get('Q20A')
        anx['gender']=request.POST.get('gender')
        anx['age_group']=request.POST.get('age_group')
        anx['orientation']=request.POST.get('orientation')

        stress={}
        stress['Q1A']=request.POST.get('Q1A')
        stress['Q6A']=request.POST.get('Q6A')
        stress['Q8A']=request.POST.get('Q8A')
        stress['Q11A']=request.POST.get('Q11A')
        stress['Q12A']=request.POST.get('Q12A')
        stress['Q14A']=request.POST.get('Q14A')
        stress['Q18A']=request.POST.get('Q18A')
        stress['gender']=request.POST.get('gender')
        stress['age_group']=request.POST.get('age_group')
        stress['orientation']=request.POST.get('orientation')


        if (depr['Q3A'] and depr['Q5A'] and depr['Q10A'] and depr['Q13A'] and depr['Q16A'] and depr['Q17A'] 
        and depr['Q21A'] and anx['Q2A'] and anx['Q4A'] and anx['Q7A'] and anx['Q9A'] and anx['Q15A'] 
        and anx['Q19A'] and anx['Q20A'] and stress['Q1A'] and stress['Q6A'] and stress['Q8A'] 
        and stress['Q11A'] and stress['Q12A'] and stress['Q14A'] and stress['Q18A'] is not None): 

            testDepr=pd.DataFrame({'x':depr}).transpose()
            deprPred=reloadModel.predict(testDepr)[0]

            testAnx=pd.DataFrame({'x':anx}).transpose()
            anxPred=reloadModel2.predict(testAnx)[0]

            testStress=pd.DataFrame({'x':stress}).transpose()
            stressPred=reloadModel3.predict(testStress)[0]

            name = request.POST.get('name')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            age_group = request.POST.get('age_group')
            orientation = request.POST.get('orientation')

            current_datetime = timezone.now()
      
            if user.is_authenticated and user.is_superuser == 0:
                testResult = TestResultMember(depressionLvl=deprPred, anxietyLvl=anxPred, stressLvl=stressPred,member_id=member_id,user_id=user.id,submit_datetime=current_datetime)
                testResult.save()

            else:      
                visitor = Visitor(name=name, email=email, gender=gender, age=age_group, orientation=orientation)
                visitor.save()
                testResult = TestResultVisitor(depressionLvl=deprPred, anxietyLvl=anxPred, stressLvl=stressPred,visitor_id=visitor.id,submit_datetime=current_datetime)
                testResult.save()

            deprClass = YogaClass.objects.filter(type='D')
            anxClass = YogaClass.objects.filter(type='A')
            stressClass = YogaClass.objects.filter(type='S')
            generalClass = YogaClass.objects.filter(type='G')


            x=integer
            y=integer
            z=integer

            if deprPred == "Normal":
                x=0
            elif deprPred == "Mild":
                x=1
            elif deprPred  == "Moderate":
                x=2
            elif deprPred  == "Severe":
                x=3
            elif deprPred  == "Extremely Severe":
                x=4

            if anxPred == "Normal":
                y=0
            elif anxPred == "Mild":
                y=1
            elif anxPred  == "Moderate":
                y=2
            elif anxPred  == "Severe":
                y=3
            elif anxPred  == "Extremely Severe":
                y=4

            if stressPred == "Normal":
                z=0
            elif stressPred == "Mild":
                z=1
            elif stressPred  == "Moderate":
                z=2
            elif stressPred  == "Severe":
                z=3
            elif stressPred  == "Extremely Severe":
                z=4
        else:
            messages.info(request,'Field cannot be empty!')
            return render(request,'examine_DAS.html',status=409)
    else:
        messages.info(request,'Error')
        return redirect('examine_DAS')

    context={'deprPred': deprPred,'anxPred':anxPred,'stressPred':stressPred,'x':x,'y':y,'z':z, 'deprClass':deprClass, 'anxClass':anxClass,'stressClass':stressClass,'generalClass':generalClass}
    return render(request,'DAS_result.html',context)

def examine_DAS(request):
    user = request.user
    if user.is_authenticated and user.is_superuser == 0:
        member_info = Member.objects.get(user_id=user.id) 

        context={'member_info': member_info}
        return render(request,'examine_DAS.html',context)
    else:
        return render(request,'examine_DAS.html')

