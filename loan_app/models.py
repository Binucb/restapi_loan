from django.db import models

# Create your models here.
class Approval(models.Model):    
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	MARRIED_CHOICES = (
        ('Yes', 'Yes'),
		('No', 'No')
	)
	GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
	SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	dependants=models.IntegerField(default=0)
	applicantincome=models.IntegerField(default=0)
	coapplicatincome=models.IntegerField(default=0)
	loanamt=models.IntegerField(default=0)
	loanterm=models.IntegerField(default=0)
	credithistory=models.IntegerField(default=0)
	gender=models.CharField(max_length=15, choices=GENDER_CHOICES,default='Male')
	married=models.CharField(max_length=15, choices=MARRIED_CHOICES, default='No')
	graduatededucation=models.CharField(max_length=15, choices=GRADUATED_CHOICES,default='Graduate')
	selfemployed=models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES,default='No')
	area=models.CharField(max_length=15, choices=PROPERTY_CHOICES,default=0)

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)




