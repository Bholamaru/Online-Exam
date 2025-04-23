from django.db import models

# Create your models here.
class reg(models.Model):
    gender=[('male','MALE'),('female','FEMALE')]

    name = models.CharField(max_length=50)
    mob = models.BigIntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    gen=models.CharField(max_length=10 ,choices=gender,default='male')
    def __str__(self):
        return self.name
class subject(models.Model):
    sub_name=models.CharField(max_length=250)
    shor_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_name  
class course(models.Model):
    course_name=models.CharField(max_length=250)
    sub=models.ManyToManyField(subject,related_name='subjects')
    def __str__(self):
        return self.course_name

class paper(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,related_name='course')
    subject=models.ForeignKey(subject,on_delete=models.CASCADE,related_name='paper')
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=80)
    option2=models.CharField(max_length=80)
    option3=models.CharField(max_length=80)
    option4=models.CharField(max_length=80)
    answer=models.CharField(max_length=80)
    def __str__(self):
        return self.question
class resultmodel(models.Model):
    student_name=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    subject_id=models.BigIntegerField()
    subject_name=models.CharField(max_length=80)
    score=models.BigIntegerField()
    total_questions=models.BigIntegerField()
    result_percentage=models.FloatField()
    def __str__(self):
        return self.student_name