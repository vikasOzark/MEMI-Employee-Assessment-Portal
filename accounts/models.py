from django.db import models
from .validators import vid_size

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True )
    fullname = models.CharField(max_length=100,null=True)
    assesment_taken =  models.BooleanField(default = False)
    answer_saved=models.BooleanField(default = False)
    profile_pic= models.ImageField(upload_to='Assesment/static/media',null=True,blank=True)
    address = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=20,null=True)
    pos_applied_for= models.CharField(max_length=20,null=True)
    tenth_percent= models.FloatField(null=True)
    twelfth_percent= models.FloatField(null=True)
    Graduation = (
        ('B.Tech', 'B.Tech'),
        ('B.Com', 'B.Com'),
        ('BBA', 'BBA'),
        ('B.E', 'B.E'),
        ('Others', 'Others')
    )
    graduation=models.CharField(max_length=100,choices=Graduation, default ='Select Graduation')
    graduation_spcl=models.CharField(max_length=100,null=True)
    Post_graduation = (
        ('M.Tech', 'M.Tech'),
        ('MBA', 'MBA'),
        ('ME', 'ME'),
        ('M.Sc', 'M.Sc'),
        ('Not Applicable', 'Not Applicable')
    )
    post_graduation=models.CharField(max_length=100,choices=Post_graduation, default ='Select Post_Graduation')
    post_graduation_spcl=models.CharField(max_length=100,null=True)
    other_qual=models.CharField(max_length=100,null=True)
    currrent_loc=models.CharField(max_length=100,null=True)
    currrent_employer=models.CharField(max_length=50,null=True)
    currrent_ctc=models.FloatField(null=True)
    expected_ctc=models.FloatField(null=True)
    notice_per=models.FloatField(null=True)
    reson_for_leaving=models.TextField(max_length=400, null=True)
    userform_filled=models.BooleanField(default = False)
    intro_vid= models.FileField(upload_to='Assesment/static/introvedios/',null=True,blank=True, validators=[vid_size])
    comment = models.TextField(max_length=400, null=True)
    time_taken= models.TimeField(null=True)
    

