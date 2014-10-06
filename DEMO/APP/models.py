from django.db import models

# Create your models here.

class Tipo(models.Model):
	int_id	= models.IntegerField(primary_key=True)
	str_desc	= models.CharField(max_length=100)
	"""docstring for Tipo"""
	def __init__(self, arg):
		super(Tipo, self).__init__()
		self.arg = arg

class User(models.Model):
	str_id	= models.CharField(max_length=10,primary_key=True)
	str_user	= models.CharField(max_length=15)
	str_pass	= models.CharField(max_length=15)
	str_name	= models.CharField(max_length=50)
	int_edad	= models.IntegerField()
	int_id_tip	= models.ForeignKey(Tipo)
	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
