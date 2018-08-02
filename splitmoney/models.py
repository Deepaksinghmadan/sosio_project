from django.db import models

#creation of individual models for each user to save all activities
class Ram(models.Model):
	activity=models.CharField(max_length=50)
	personal_exp=models.IntegerField(null=True,blank=True)
	sharing_exp=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.activity


class Shyam(models.Model):
	activity=models.CharField(max_length=50)
	personal_exp=models.IntegerField(null=True,blank=True)
	sharing_exp=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.activity