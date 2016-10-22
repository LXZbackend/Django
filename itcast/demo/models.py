from django.db import models

# Create your models here.
class BookInfo(models.Model):
	bittle = models.CharField(max_length=10)
	bpub_date = models.DateTimeField()
	def __str__(self):
		return "%d"%self.pk
	
	


class HerInfo(models.Model):
	hname = models.CharField(max_length=10)
	hgender = models.BooleanField()
	Hcontent = models.CharField(max_length=1000)
	hBook = models.ForeignKey(BookInfo)