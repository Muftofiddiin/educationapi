from django.db import models
from django.db.models import IntegerChoices
#home page
# OneToOneField(Universities , on_delete=models.CASCADE , to_field=Universities.rating)
class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()



class About(models.Model):
    logo = models.ImageField()
    amount = models.CharField(max_length=20)
    description = models.TextField()

class Universities(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.CharField(max_length=25)
    quality = models.IntegerField()
    cost = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    # search
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    grade = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)


class Faculties(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()


class Student(models.Model):
    name = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    university = models.ForeignKey(Universities , on_delete=models.CASCADE)
    specialization = models.CharField(default= 'No Data',max_length=255)
    passport = models.FileField(blank=True , null=True)
    diplom = models.FileField(blank=True , null=True)


class Comments(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    text = models.TextField()


class Uni_Details(models.Model):
    university = models.ForeignKey(Universities , on_delete=models.CASCADE)
    description = models.TextField()
    process = models.CharField(max_length=255)
    location = models.URLField(blank=True , null=True)
    gallery = models.ImageField(blank=True , null=True)


class Profile(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)




class P_Universities(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date = models.DateField()
    status = models.IntegerField(choices=(
        (1, 'Прием Документов'),
        (2 , 'Прием Закрыт')
    ))
    info = models.CharField(max_length=255)

class Assistent(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255)
    about = models.TextField()
    number = models.CharField(max_length=16)
    email = models.EmailField(blank=True , null=True)


class Econtract(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pdf = models.FileField(blank=True , null=True)


class Statistics(models.Model):
    univ = models.ForeignKey(Universities , on_delete=models.CASCADE)
    students = models.IntegerField()
    invoices = models.IntegerField()
    accepted = models.IntegerField()
    naccepted = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    langs = models.CharField(max_length=25)
    faculties = models.ForeignKey(Faculties , on_delete=models.CASCADE)
    semesters = models.CharField(max_length=25)
    payment = models.BooleanField(default=False)


class Search(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties , on_delete=models.CASCADE)
    gpa = models.IntegerField()
    ielts = models.IntegerField()
    accept = models.IntegerField(choices=(
        (1, 'Да'),
        (2, 'Нет')
    ))

class UnivCab(models.Model):
    name = models.CharField(max_length=100)
    found = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    bachelors = models.IntegerField()
    masters = models.IntegerField()
    teachers = models.IntegerField()
    startingsalary = models.CharField(max_length=100)
    description = models.TextField()
    gallery = models.FileField(blank=True , null=True)
    map = models.URLField(blank=True , null=True)



