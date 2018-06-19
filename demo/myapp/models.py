from django.db import models
from __future__ import unicode_literals
# Create your models here.
class Register(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	dof=models.DateField(max_length=20)
	password=models.CharField(max_length=20)

	class Meta:
		db_table=""
