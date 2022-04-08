from asyncio.windows_events import NULL
from enum import unique
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from pandas import notnull
# from .forms import *

from Assesment.models import QuesModel
from Assesment.models import resultModel
from django.http import HttpResponse
import random
from collections import defaultdict
import json
from .forms import *
from django.contrib import messages
from accounts.models import CustomUser
from django.core.paginator import Paginator

from rest_framework.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .resources import PersonResource
from tablib import Dataset
# from .serializers import QuesModelSerializer 
# from serializers import QuesModelSerializer





# Create your views here.


firstrun = 0
@api_view(["GET", "POST"])
def home(request):
    # print("user.is_staff", request.user.is_staff)
    # print("user: ", request.user)

    filtereduser = resultModel.objects.filter(username=request.user)
    # print("usernamefilter", filtereduser )
    # print('request.user.is_staff', request.user.is_staff)
    if not request.user.is_authenticated:
        return redirect('login/')
    first_attempt = True
    if len(list(filtereduser)) == 0:
      if request.method == 'POST'  :
          
          user_here=CustomUser.objects.get(username=request.user)
          user_here.assesment_taken =True
          user_here.save()
          print("user..... ", user_here)
        #   testtaken = CustomUser.objects.create(assesment_taken=True)
        #   testtaken.save()
        #   print("request.POST in if ", request.POST)
          category=  request.GET.get('category')    
          questions = list(QuesModel.objects.filter(category=category).values (
                'question', 'op1', 'op2', 'op3', 'op4', 'ans', 'difficulty', 'category','saved_answer'))
          
          print("all ques ", questions)
          print("request.post", request.POST)
          for q in questions:
            print("question is ",q['question'])
            
            saveans= request.POST.get(q['question'])
           
            print("saveans.... ",saveans)
            question=QuesModel.objects.get(question=q['question'])
            # print("selected question", question)
            a = {}
            username=request.user.username
            a[username] = saveans 
            question.saved_answer = a
            print("question.saved_answer" , question.saved_answer)
            question.save()
          filtereduser_cat = categories.objects.filter(user = request.user, category= category ) 
          print("filtereduser_cat", filtereduser_cat)
          if len(list(filtereduser_cat)) == 0: 
            cat = categories(user=request.user, category = request.GET.get('category'),attempt = True )
            cat.save()




          cat_model=list(categories.objects.values ('attempt', 'category'))
         
          print("cat_model",cat_model)
          return redirect('/exam_categories')
            # render(request,'Assesment/result.html',context)
      else:
            # print('code is in else..')
            global firstrun
            firstrun = 0
            firstrun += 1
            
            if firstrun == 1:
                
                questions = list(QuesModel.objects.values(
                'question', 'op1', 'op2', 'op3', 'op4', 'ans', 'difficulty', 'category', 'saved_answer','questiontype'))
                
                quessets_diff_cat = defaultdict(list)
                # questions['saved_answer'][request.user.username] = ""
                
                for i in questions:
                    # =i['difficulty']
                    difftype_catgry = i['difficulty'] + \
                        "_" + str(i['category'])
                    
                    
                    if i['saved_answer'] and request.user.username in i['saved_answer'] :
                        # print("i[saved_answer]" , i['saved_answer'])
                        saved_ans =  i['saved_answer'][request.user.username]
                    else:
                        saved_ans = ''
                    question = {"question": i['question'], "op1": i['op1'],
                        "op2": i['op2'], "op3": i['op3'], "op4": i['op4'], "ans": i['ans'], "saved_answer":saved_ans, "questiontype" : i['questiontype'] }
                   
                    print("questions",questions)
                    quessets_diff_cat[difftype_catgry].append(question)
                
                print(" quessets_diff_cat", quessets_diff_cat)
            
                
                print(" questionsetdiff cat", quessets_diff_cat)

                
                # questionset2=random.sample(
                #     quessets_diff_cat['a_verbal reasoning'],1 )

                # p = Paginator(questionset, 1)  # creating a paginator object
                # page_number = request.GET.get('page')
                # try:
                #     # returns the desired page object
                #     page_obj = p.get_page(page_number)
                   
                   
                # except PageNotAnInteger:
                #     # if page_number is not an integer then assign the first page
                #     page_obj = p.page(1)
                    
                # except EmptyPage:
                #     # if page is empty then return last page
                #     page_obj = p.page(p.num_pages)

                category=  request.GET.get('category')   
                print ("category", category)

                cat_questions= quessets_diff_cat['a_' + category] 
                qno= 0 
                for n in cat_questions: 
                    qno = qno +  1
                    n["qno"] = "Q " +  str(qno) 
               
                # 'question', 'op1', 'op2', 'op3', 'op4', 'ans', 'difficulty', 'category')) 
                context = {

                    'category_name': category,
                    'category': cat_questions,
                }
                print ("context ['category']", context ['category'])
                return render(request, 'Assesment/home.html', context )
            else:
                print('code is in second else..')
                return render(request,'Assesment/thankyoupge.html')
    print('code is in last else..')            
    return render(request,'Assesment/thankyoupge.html')


def allresults(request): 
    
    Username = request.user
    # User_Score= request.session['score']
    Time_Taken = request.session['time']
    # Correct_Answers= request.session['correct']
    # Wrong_Answers=request.session['wrong']
    Percentage_Scored=request.session['percent']
    # Total = request.session['total']
    new_user = resultModel(username=Username, time = Time_Taken, percent= Percentage_Scored)
    new_user.save()
    updated_results= resultModel.objects.all()
    print("updated_results",updated_results)
    # print("User_Score",User_Score)
    print("time",Time_Taken)
    # print("corr answers",Correct_Answers)
    context = {'updated_results': updated_results}

def starttest(request): 
    category=  request.GET.get('category')  
    print("print category:",category)  
    context= { "category" : category }
    return render(request,'Assesment/starttest.html', context)

def logoutPage(request):

    logout(request)
    return redirect('/')

def thankyoupge (request):
    q_answered_lr = list(QuesModel.objects.filter(category= "Logical Reasoning").values( 'saved_answer','ans' ))
    q_answered_PA = list(QuesModel.objects.filter(category= "Personality Assessment").values( 'saved_answer','ans'))
    q_answered_FQ = list(QuesModel.objects.filter(category= "Financial Question").values( 'saved_answer', 'ans'))
    q_answered_VA = list(QuesModel.objects.filter(category= "Verbal Ability").values( 'saved_answer', 'ans'))

    # cats=categories.objects.get(user= request.user.username , category= "Logical Reasoning" )
    # cats.score
    logical_score= 0
    financial_score= 0
    verbal_score= 0
    personality_score = 0
    # for q in q_answered_lr:
    #       if q['ans'] == q['saved_answer'][request.user.username]:
    #         logical_score += 10
          
    lr_percentage= logical_score/(20*10) * 100

    for q in q_answered_VA: 
        print("q['saved_answer']", q['saved_answer'][request.user.username] , "q['ans']", q['ans'])
        if q['ans'] == q['saved_answer'][request.user.username]:
            verbal_score += 10
            print ("verbal_score",verbal_score ) 
    
    VA_percentage = verbal_score/(20*10) * 100

    for q in q_answered_PA:
          
          if q['ans'] == q['saved_answer'][request.user.username]:
            personality_score += 10
            
    PA_percentage = personality_score/(20*10) * 100

    for q in q_answered_FQ:
          
          if q['ans'] == q['saved_answer'][request.user.username]:
            financial_score += 10
          
    FQ_percentage = financial_score/(20*10) * 100



    cats_lr=categories.objects.get(user= request.user.username , category= "Logical Reasoning" )
    cats_lr.score = lr_percentage
    cats_lr.save()
    cats_VA=categories.objects.get(user= request.user.username , category= "Verbal Ability" )
    cats_VA.score = VA_percentage
    cats_VA.save()
    cats_PA=categories.objects.get(user= request.user.username , category= "Personality Assessment" )
    cats_PA.score = PA_percentage
    cats_PA.save()
    cats_FQ=categories.objects.get(user= request.user.username , category= "Financial Question" )
    cats_FQ.score = FQ_percentage
    cats_FQ.save()

    user_scores= list(categories.objects.filter(user=request.user.username ).values( "score", "category" ))
    print("user_scores", user_scores)
    print(FQ_percentage, PA_percentage,VA_percentage, lr_percentage)
   
    return render(request,'Assesment/thankyoupge.html')


def addquestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)


            if(form.is_valid()):
                form.save()
                return redirect('/addquestion')
        context={'form':form}
        return render(request,'Assesment/addquestion.html',context)
    else: 
        return redirect('/home') 

def alluserresults(request):
  allresults= list(resultModel.objects.values('username','percent','time'))
  print("Allusers",  allresults)
  return render(request,'Assesment/alluserresults.html', {
    'allresults':   allresults
  })
  
def student_dashboard(request):
    total_question= 80 
    print("Request.user", request.user)
    candidateinfo = CustomUser.objects.get(username=request.user)
    total_course= QuesModel.objects.values('category').distinct().count() 

    dict={
    'total_course':total_course,
    'total_question': total_question,
    'profile_pic': candidateinfo.profile_pic,
    'fullname': candidateinfo.fullname
    }
    return render(request,'Assesment/dashboard.html',context=dict)

def exam_categories(request):
    
    courses_category =list(QuesModel.objects.values('category').distinct())
    print("courses_category", courses_category )
    username=request.user.username
    q_answered_lr = list(QuesModel.objects.filter(category= "Logical Reasoning").values( 'saved_answer','ans' ))
    q_answered_PA = list(QuesModel.objects.filter(category= "Personality Assessment").values( 'saved_answer','ans'))
    q_answered_FQ = list(QuesModel.objects.filter(category= "Financial Question").values( 'saved_answer', 'ans'))
    q_answered_VA = list(QuesModel.objects.filter(category= "Verbal Ability").values( 'saved_answer', 'ans'))
    print ("........q_answered_VA......." ,q_answered_VA)

    score = 0
    wrong = 0
    correct = 0
    total = 0
    
    # if request.method == 'POST'  : 
    #     for q in q_answered_lr:
    #       total += 1
    #       if q['ans'] == q['saved_answer']:
    #         score += 10
    #         correct += 1
    #       else:
    #         wrong += 1
    # score_lr = score/(total*10) * 100
    attempted_lr= 0
    attempted_FQ= 0
    attempted_VA= 0
    attempted_PA= 0
    print ("........username......." ,username)
    print ("........q_answered_lr......." ,q_answered_lr)
    

    for q in q_answered_lr:
    
      if q['saved_answer'] and username in q['saved_answer']:
            attempted_lr += 1
      else: 
            attempted_lr= 0
   
            
         
    for q in q_answered_PA:
      if q['saved_answer'] and username in q['saved_answer']:
            attempted_PA +=  1
            
      else: 
            attempted_PA= 0      

    
    for q in q_answered_FQ:
      if q['saved_answer'] and username in q['saved_answer']:
            attempted_FQ += 1
      else: 
            attempted_FQ= 0 

    for q in q_answered_VA:
      print ("attempted_VA", attempted_VA) 
      if q['saved_answer'] and username in q['saved_answer']:
            attempted_VA += 1
            print ("attempted_VA", attempted_VA)
      else: 
            attempted_VA= 0   



    
    remaining_lr = 20 - attempted_lr
    remaining_FQ = 20 - attempted_FQ
    remaining_VA = 20 - attempted_VA
    remaining_PA = 20 - attempted_PA

    
    
    # for c in q_answered_lr:
    #     if c['saved_answer'] is not None :
    #         attempted_lr += 1
    # print("attempted", attempted_lr )
    # print('q_answered', q_answered_lr)
    
    for c in courses_category:
       cat_model=list(categories.objects.filter(category= c['category'], user= request.user).values('attempt'))
    #  print('cat_model',cat_model)
       if len(cat_model) > 0 :
           c['attempt'] = cat_model[0]['attempt']
       else:
            c['attempt'] = False
       if c['category']== "Logical Reasoning" :
          c['remaining'] = remaining_lr
          c['attempted'] = attempted_lr
       elif c['category']== "Verbal Ability":
           c['remaining'] = remaining_VA
           c['attempted'] = attempted_VA
       elif c['category']== "Financial Question":
            c['remaining'] = remaining_FQ
            c['attempted'] = attempted_FQ
       elif c['category']== "Personality Assessment":
            c['remaining'] = remaining_PA
            c['attempted'] = attempted_PA

    
       


    # print("courses_categories", courses_category)
    context= {'courses_categories' : courses_category 
    }
    
    return render(request,"Assesment/exam_categories.html", context  )