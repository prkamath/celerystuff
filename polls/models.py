from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    schoolName=models.CharField(max_length=30,null=False)

class standardClass(models.Model):
    verboseStandardName=models.CharField(max_length=30,null=False)
    school=models.ForeignKey(School,max_length=30)

class Student(models.Model):
    studentName=models.CharField(max_length=30,null=False)
    studentSex=models.CharField(max_length=30,null=False)
    standard=models.ForeignKey(standardClass,null=False)


