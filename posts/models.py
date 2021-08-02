from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):

	user        = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	title       = models.CharField(max_length=200,null=True)
	description = models.TextField(null=True)
	created_at  = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated_at  = models.DateTimeField(auto_now_add=False,auto_now=True)
	status      = models.IntegerField(default = 1)
