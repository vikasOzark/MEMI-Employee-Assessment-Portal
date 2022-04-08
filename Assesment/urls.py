from django.contrib import admin
from django.urls import path
from Assesment.views import home, allresults, starttest, logoutPage, addquestion, alluserresults,student_dashboard,exam_categories, thankyoupge
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts.views import LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('starttest',views.starttest,name='starttest'),

    path('',views.home,name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('addquestion', addquestion,name='addQuestion'),
    # path('login', views.login,name='login'),
    path('logout', logoutPage,name='logout'),
    # path('register', registerPage,name='register'),
    path('alluserresults', alluserresults,name='alluserresults'),
    path('dashboard', student_dashboard,name='dashboard'),
    path('exam_categories', exam_categories,name='exam_categories'),
    path('thankyoupge', thankyoupge, name = 'thankyou') 

]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  