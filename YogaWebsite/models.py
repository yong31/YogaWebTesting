from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class GetInTouchContact(models.Model):
    name = models.TextField(max_length=191)
    email = models.EmailField()
    subject = models.TextField(max_length=191)
    message = models.TextField(max_length=255)
    
class YogaClass(models.Model):
    name = models.TextField(max_length=191)
    description = models.TextField()
    class_details = models.TextField(default="")
    image = models.ImageField(upload_to='pics')
    CLASS_TYPES = (
        ('D', 'Depression'),
        ('A', 'Anxiety'),
        ('S', 'Stress'),
        ('G', 'General'),
    )
    type = models.CharField(max_length=1, choices=CLASS_TYPES)

    def __str__(self):
        return self.name
    
    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width >300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


    class Meta:
        verbose_name_plural = "Yoga Classes"


class Visitor(models.Model):
    name = models.TextField(max_length=191)
    email = models.EmailField()
    GENDER = (
        ('1','Male'),
        ('2','Female'),
    )
    gender = models.TextField(choices=GENDER)
    AGE = (
        ('0','below 19'),
        ('1','19 to 23'),
        ('2','24 to 40'),
        ('3','above 40'),
    )
    age = models.TextField(choices=AGE)
    ORIENTATION = (
        ('1','Heterosexual'),
        ('2','Bisexual'),
        ('3','Homosexual'),
        ('4','Asexual'),
        ('5','Other'),
    )
    orientation = models.TextField(choices=ORIENTATION)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER = (
        ('1','Male'),
        ('2','Female'),
    )
    gender = models.TextField(choices=GENDER)
    AGE = (
        ('0','below 19'),
        ('1','19 to 23'),
        ('2','24 to 40'),
        ('3','above 40'),
    )
    age = models.TextField(choices=AGE)
    ORIENTATION = (
        ('1','Heterosexual'),
        ('2','Bisexual'),
        ('3','Homosexual'),
        ('4','Asexual'),
        ('5','Other'),
    )
    orientation = models.TextField(choices=ORIENTATION)
    
class TestResultVisitor(models.Model):
    visitor= models.ForeignKey(Visitor, on_delete=models.CASCADE)
    depressionLvl = models.TextField(max_length=191)
    anxietyLvl= models.TextField(max_length=191)
    stressLvl= models.TextField(max_length=191)
    submit_datetime= models.DateTimeField(max_length=191, default='2022-7-12 20:38:00')

    class Meta:
        verbose_name = "Overall Test Result"

class TestResultMember(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    member= models.ForeignKey(Member, on_delete=models.CASCADE)
    depressionLvl = models.TextField(max_length=191)
    anxietyLvl= models.TextField(max_length=191)
    stressLvl= models.TextField(max_length=191)
    submit_datetime= models.DateTimeField(max_length=191, default='2022-7-12 20:38:00')


