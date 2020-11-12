from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	company = models.CharField(max_length=200, blank=True)
	title = models.CharField(max_length=200, blank=True)
	summary = models.TextField(max_length=2000)
	start_date = models.DateField()
	end_date = models.DateField()

	# def __str__(self):
	# 	return self.title
	#
	# def start_date_neat(self):
	# 	return self.start_date.strftime('%m/%Y')
	#
	# def end_date_neat(self):
	# 	return self.end_date.strftime('%m/%Y')

class Certificate(models.Model):
	image = models.ImageField(upload_to='images/')
	issuer = models.CharField(max_length=200, blank=True)
	topic = models.CharField(max_length=200, blank=True)

	# def __str__(self):
	# 	return self.topic


'''
python manange.py makemigrations
python manange.py migrate
'''
