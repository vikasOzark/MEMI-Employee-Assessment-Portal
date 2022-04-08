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
    if len(list(filtereduser)) == 0:
      if request.method == 'POST'  :
          user_here=CustomUser.objects.get(username=request.user)
          user_here.answer_saved=True
          user_here.save()
          print("user..... ", user_here)
        #   testtaken = CustomUser.objects.create(assesment_taken=True)
        #   testtaken.save()
        #   print("request.POST in if ", request.POST)
          questions = QuesModel.objects.all()
          print("all ques ", list (QuesModel.objects.all()))
          score = 0
          wrong = 0
          correct = 0
          total = 0
          for q in questions:
              total += 1
              print("request.post.question", request.POST.get(q.question))
              print(q.ans)
              if q.ans == request.POST.get(q.question):
                  score += 10
                  correct += 1
              else:
                  wrong += 1
          percent = score/(total*10) * 100
          # request.session['score']=score
          request.session['time'] = request.POST.get('timer')
          # request.session['correct']=correct
          # request.session['wrong']=wrong
          request.session['percent'] = percent
          # request.session['total']=total

          print("percent", percent)
          context = {

              'time': request.POST.get('timer'),
              # 'correct':correct,
              # 'wrong':wrong,
              'percent': percent,
              # 'total':total
          }

          allresults(request)
          courses_category =list(QuesModel.objects.values('category').distinct())
          return render(request, 'Assesment/exam_categories.html', {'courses_categories' :  courses_category } )
            # render(request,'Assesment/result.html',context)
      else:
            # print('code is in else..')
            global firstrun
            firstrun = 0
            firstrun += 1
            if firstrun == 1:

                questions = list(QuesModel.objects.values(
                'question', 'op1', 'op2', 'op3', 'op4', 'ans', 'difficulty', 'category'))
                # print("questions",questions)
                quessets_diff_cat = defaultdict(list)
                for i in questions:
                    # =i['difficulty']
                    difftype_catgry = i['difficulty'] + \
                        "_" + str(i['category'])
                    question = {"question": i['question'], "op1": i['op1'],
                        "op2": i['op2'], "op3": i['op3'], "op4": i['op4'], "ans": i['ans']}

                    quessets_diff_cat[difftype_catgry].append(question)
                
                # print(" quessets_diff_cat", quessets_diff_cat)
            
                
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
                context = {
                    'category_name': category,
                    'category': quessets_diff_cat['a_' + category],
                }
                
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
    # Wrong_Answers=request.session['wrong
    # ']
    Percentage_Scored=request.session['percent']
    # Total = request.session['total']
    new_user = resultModel(username=Username,  time= Time_Taken , percent= Percentage_Scored)
    new_user.save()
    updated_results= resultModel.objects.all()
    print("updated_results",updated_results)
    # print("User_Score",User_Score)
    print("time",Time_Taken)
    # print("corr answers",Correct_Answers)
    context={'updated_results': updated_results}

def starttest(request): 
    category=  request.GET.get('category')  
    print("print category:",category)  
    context= { "category" : category }
    return render(request,'Assesment/starttest.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')


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
    print("courses_categories", courses_category)
    return render(request,"Assesment/exam_categories.html",{'courses_categories' :  courses_category } )

