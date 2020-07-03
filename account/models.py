from django.db import models

############### models are created here ###############

# model for Student() #

class Student(models.Model):
    name = models.CharField(null = True,max_length=30)
    email = models.CharField(max_length=52)
    course = models.CharField(null = True,max_length=20)
    sem = models.IntegerField()
    department = models.TextField(null = True,max_length=30)
    mobno = models.CharField(null = True,max_length=20)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

# model for StudentApplication() #

class StudentApplication(models.Model):
    Submitted = 1
    UnderReview = 2
    Rejected = 3
    Approved = 4
    STATUS = (
    (Submitted, 'Submitted'),
    (UnderReview, 'UnderReview'),
    (Rejected, 'Rejected'),
    (Approved, 'Approved'),
    )
    email = models.CharField(null=True,max_length=56)
    company = models.CharField(null = True,max_length=30)
    position = models.CharField(null = True, max_length=50)
    reason_to_join = models.TextField(null = True)
    applied_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(null = True,upload_to='resume/')
    status = models.PositiveSmallIntegerField(default=0, choices=STATUS)
    button = models.BooleanField(default = True)

    def __str__(self):
        return self.email.__str__()

# model for TPO() #

class TPO(models.Model):
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.name
