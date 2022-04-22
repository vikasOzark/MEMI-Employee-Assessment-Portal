from email.policy import default
from re import T
from unicodedata import category
from django.db import models

import json
from django.db import models
# Create your models here.

 
# Create your models here.
class QuesModel(models.Model):
    question= models.CharField(max_length=750,null=True,blank=True)
    op1 = models.CharField(max_length=100,null=True,blank=True)
    op2 = models.CharField(max_length=100,null=True,blank=True)
    op3 = models.CharField(max_length=100,null=True,blank=True)
    op4 = models.CharField(max_length=100,null=True,blank=True)
    single_answer= models.FloatField(max_length=20,null=True,blank=True)
   
    ans = models.CharField(max_length=100,null=True,blank=True)
    difficulties = (
        ('a', 'a'),
    )
    difficulty=models.CharField(max_length=100, choices=difficulties, default="Select Difficulty" )
    qtypes = (
        ('multiple choice', 'multiple choice'),
        ('single answer', 'single answer'),
        
    )
    questiontype= models.CharField(max_length=100, choices=qtypes, default="Select Qtype" ) 
   
    categories = (
        ('Logical Reasoning', 'Logical Reasoning'),
        ('Verbal Ability', 'Verbal Ability'),
        ('Financial Question', 'Financial Question'),
        ('Personality Assessment', 'Personality Assessment'),
    )
    category= models.CharField(max_length=100, choices=categories, default="Logical Reasoning" )
    #ans = JSONField()
    saved_answer = models.JSONField(null=True, blank=True)
    # def __str__(self):
    #     return self.question

class categories(models.Model):
   user= models.CharField(max_length=50,null=True,blank=True)
   category= models.CharField(max_length=50,null=True,blank=True)
   attempt= models.BooleanField(default = False)
   score = models.FloatField(default = False)
#    time = models.CharField(max_length=50,null=True)


class resultModel(models.Model):

    username = models.CharField(max_length=100,null=True)

    # score = models.CharField(max_length=200,null=True)

    time = models.CharField(max_length=50,null=True)

    # correct = models.CharField(max_length=200,null=True)

    # wrong = models.CharField(max_length=200,null=True)

    # score_logical_reasoning=models.ForeignKey(QuesModel, max_length=50,null=True)

    percent = models.CharField(max_length=50,null=True)

    # total = models.CharField(max_length=200,null=True)
















