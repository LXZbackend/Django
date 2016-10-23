#coding=utf-8
from django.db import models

# Create your models here.
class BookInfo(models.Model):
	bittle = models.CharField(max_length=10)
	# bittle = models.CharField(max_length=10)
	bpub_date = models.DateTimeField()

	def __str__(self):
		return self.bittle.encode('utf-8')



class HeroInfo(models.Model):
	hname = models.CharField(max_length=20)
	hgender = models.BooleanField()
	hcontent = models.CharField(max_length=100)
	# 设置外键  
	hBook = models.ForeignKey('BookInfo')

	def gender(self):
		if self.hgender:
			return "男"
		else:
			return "女"
	gender.short_description = '性别'



	def __str__(self):
		return self.bittle.encode("utf-8")