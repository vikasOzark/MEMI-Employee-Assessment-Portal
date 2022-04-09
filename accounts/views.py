from termios import ECHOE
from django.shortcuts import render
from django.contrib import messages
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import LoginForm, RegisterForm, CommentForm
from django.conf import settings
from django.core.mail import send_mail
import os
from Assesment.models import categories
from accounts.send_email import *
class LoginView(auth_views.LoginView):
    # form_class = LoginForm
    template_name = 'accounts/login.html'
    
    def get(self,request):

        if request.user.is_authenticated:
            print("in if........")
            return redirect('/dashboard')
        else:
            if request.method=="POST":
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                # print("user is ........",user)
                if user is not None:
                    login(request,user)
                    return redirect ('accounts/candidateintro.html')
                    # return redirect('accounts/starttest.html')
            context={}
            
            return render(request,'accounts/login.html')
class RegisterView(generic.CreateView):
    
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def post(self,request):
        
    # if request.user.is_authenticated:
    #     return redirect('home') 
    # else: 
        form =  RegisterForm
        print("request.POST outside if", request.method)
        if request.method=='POST':
            form = RegisterForm(request.POST)
            print("request.POST", request.POST)
            if form.is_valid() :
                #request.user=form.save()
                user = CustomUser.objects.create_user(fullname=form.cleaned_data['fullname'],username =form.cleaned_data['email'],  email=form.cleaned_data['email'], password='letsdoit')
                user.is_active = True
                user.save()
                mail = send_login_mail(request = request,user = user)
                #instance.save()
                messages.success(request, 'Contact request submitted successfully.')
                allresults= list(CustomUser.objects.values('fullname','email','last_login','username', 'assesment_taken')) 
                form =  RegisterForm 
                context={
                    'form':form,
                    'allresults': allresults
                }
                return render(request,'accounts/register.html',context)
            
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)  
            return redirect('/register')
    def get(self,request):

        

        allresults= list(CustomUser.objects.values('fullname','email','last_login','username', 'assesment_taken')) 
        for result in allresults:
            if result['assesment_taken'] == True:
                result['assesment_taken']  = "yes"
            else:
                 result['assesment_taken']  = "no"
        print('allusers', allresults)
        form =  RegisterForm 
        context={
            'form':form,
            'allresults': allresults
        }
        return render(request,'accounts/register.html',context)

def candidateintro(request):
    
    CandidateForm= forms.CandidateForm()
    
    mydict={ 
        'CandidateForm': CandidateForm

    }

    
    candidateinfo = CustomUser.objects.get(username=request.user)
    if request.method=='POST':
        
        Form=forms.CandidateForm(request.POST)
        
        # print('Form.is_valid',Form.is_valid())
        
        if Form.is_valid():
            
            address=request.POST['address']
            profile_pic=request.FILES['profile_pic']
            profile_pic = "/".join(str(profile_pic).strip("/").split('/')[1:])
            mobile=request.POST['mobile']
            pos_applied_for=request.POST['pos_applied_for']
            tenth_percent=request.POST['tenth_percent']
            twelfth_percent=request.POST['twelfth_percent']
            graduation=request.POST['graduation']
            post_graduation=request.POST['post_graduation']
            other_qual=request.POST['other_qual']
            currrent_loc=request.POST['currrent_loc']
            currrent_employer=request.POST['currrent_employer']
            currrent_ctc=request.POST['currrent_ctc']
            expected_ctc=request.POST['expected_ctc']
            notice_per=request.POST['notice_per']
            mobile=request.POST['mobile']
            reson_for_leaving=request.POST['reson_for_leaving']
            intro_vid=request.FILES['intro_vid']

            
            
            # print('request....... ', request.user)

            # candidateinfo = CustomUser.objects.get(username=request.user)
            # print("candidateinfo", candidateinfo.address)
            # print("candidateinfo", candidateinfo)
            candidateinfo.userform_filled = True
            candidateinfo.address=address
            candidateinfo.profile_pic= profile_pic
            candidateinfo.intro_vid = intro_vid
            candidateinfo.mobile = mobile
            candidateinfo.tenth_percent = tenth_percent
            candidateinfo.twelfth_percent =twelfth_percent
            candidateinfo.graduation= graduation
            candidateinfo.post_graduation = post_graduation
            candidateinfo.other_qual = other_qual
            candidateinfo.currrent_loc = currrent_loc
            candidateinfo.currrent_employer = currrent_employer
            candidateinfo.currrent_ctc = currrent_ctc
            candidateinfo.expected_ctc= expected_ctc
            candidateinfo.notice_per=notice_per
            candidateinfo.reson_for_leaving = reson_for_leaving
            candidateinfo.pos_applied_for = pos_applied_for
            candidateinfo.save()
            # candidate.save()
            # print('saved form', candidate.save())
            return redirect('/dashboard')
    
    
            
            
            
        return HttpResponseRedirect('/starttest')
    # candidateinfo = CustomUser.objects.get(username=request.user)
    if candidateinfo.userform_filled == False:
        return render(request,'accounts/candidateintro.html',context=mydict)
    return redirect('/dashboard')


def candidateinfo(request):
    generalinfo = list(CustomUser.objects.values('email','address','graduation_spcl','post_graduation_spcl', 'profile_pic', 'fullname' , 'intro_vid', 'mobile', 'tenth_percent', 'twelfth_percent', 'graduation', 'post_graduation', 'other_qual','currrent_loc', 'currrent_employer','currrent_ctc','expected_ctc', 'notice_per', 'reson_for_leaving', 'pos_applied_for'))

    username=  request.GET.get('username')
    print("username", username )
    cf=forms.CommentForm(request.POST)
    candidateinfo = CustomUser.objects.get(username=username)
    # print("candidateinfo",candidateinfo)
    if request.method=='GET':
        lr_score= list(categories.objects.filter(user=request.user.username, category= "Logical Reasoning" ).values( "score"))
        for s in lr_score: 
            lr_score = lr_score[0]['score']
        va_score= list(categories.objects.filter(user=request.user.username, category= "Verbal Ability" ).values( "score"))
        for s in va_score: 
            va_score = va_score[0]['score']
        fq_score = list(categories.objects.filter(user=request.user.username, category= "Financial Question" ).values( "score"))
        for s in fq_score: 
            fq_score = fq_score[0]['score']
        
        pa_score = list(categories.objects.filter(user=request.user.username, category= "Personality Assessment" ).values( "score"))
        for s in pa_score: 
            pa_score =  pa_score[0]['score']

        cf = CommentForm()
        profile_pic=candidateinfo.profile_pic
        fullname=candidateinfo.fullname
        mobile= candidateinfo.mobile
        email= candidateinfo.email
        pos_applied_for= candidateinfo.pos_applied_for
        address = candidateinfo.address
        graduation =  candidateinfo.graduation
        post_graduation= candidateinfo.post_graduation
        graduation_spcl= candidateinfo.graduation_spcl
        post_graduation_spcl= candidateinfo.post_graduation_spcl
        other_qual= candidateinfo.other_qual
        currrent_employer=candidateinfo.currrent_employer
        currrent_ctc= candidateinfo.currrent_ctc
        expected_ctc=candidateinfo.expected_ctc
        notice_per=candidateinfo.notice_per
        currrent_loc= candidateinfo.currrent_loc
        tenth_percent= candidateinfo.tenth_percent
        twelfth_percent= candidateinfo.twelfth_percent
        reson_for_leaving= candidateinfo.reson_for_leaving
        intro_vid= candidateinfo.intro_vid



        print ("lr_score......................", lr_score)
        mydict= {
        "profile_pic": profile_pic,
        "fullname" : fullname,
        "mobile": mobile,
        "email": email,
        "pos_applied_for": pos_applied_for,
        "address" : address,
        "graduation": graduation,
        "post_graduation": post_graduation, 
        "graduation_spcl" :  graduation_spcl,
        "post_graduation_spcl": post_graduation_spcl,
        "other_qual": other_qual,
        "currrent_employer": currrent_employer,
        "currrent_ctc": currrent_ctc,
        "expected_ctc" : expected_ctc,
        "notice_per": notice_per,
        "currrent_loc": currrent_loc,
        "tenth_percent": tenth_percent,
        "twelfth_percent": twelfth_percent,
        "reson_for_leaving": reson_for_leaving,
        "intro_vid": intro_vid,
        "CommentForm": cf,
        "lr_score":lr_score,
        "va_score":va_score,
        "fq_score": fq_score,
        "pa_score": pa_score,
                }
        return render(request,'accounts/candidateinfo.html', mydict)

    else:
        print("username postttt", username )
        cf=forms.CommentForm(request.POST)
        check= CustomUser.objects.filter(username=username)
        print("check", check)
        candidateinfo = CustomUser.objects.get(username=username)
        
        if cf.is_valid():
            content = request.POST['content']
            # print("content", content)
            candidateinfo.content=content
            candidateinfo.save()

        return redirect('/candidateinfo')


def user_login(request,id):
    try:
        user=CustomUser.objects.get(id = id)
    except:
        return render(request,'accounts/login.html')
    CandidateForm= forms.CandidateForm()
    
    mydict={ 
        'CandidateForm': CandidateForm
    }
    if user is not None: 
        login(request,user)
        if user.userform_filled == False:
            return render(request,'accounts/candidateintro.html',context=mydict)
        return redirect('/dashboard')
        #return redirect ('accounts/candidateintro.html')
    
            
    return render(request,'accounts/login.html')