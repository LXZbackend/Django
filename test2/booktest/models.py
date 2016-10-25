# coding=utf-8
from django.db import models

# 从写管理器 类 可以从写查询方法
class BookInfoManager(models.Manager):
	def create_book(self,title,pub_date):
		# self.modls 这个方法可以获取是哪个模型类调用的
		book = self.model()
		book.btitle = title
		book.bpub_date = pub_date
		book.bread=0
		book.bcommet=0
		book.isDelete = False

		return book
  # 注意这里的这个查询回应用的所有的查询 就是你其他查询选择的数据 最后都经过这显示出最后
	def get_queryset(self):
		return super(BookInfoManager,self).get_queryset().filter(isDelete=False)


# Create your models here.
class BookInfo(models.Model):
	btitle = models.CharField(max_length=10)
	bpub_date = models.DateTimeField()
	bread = models.IntegerField(default=0)
	bcommet = models.IntegerField(default=0)
	isDelete = models.BooleanField(default=False)

	book = BookInfoManager()

	# # 通过类方法仅进行初始化
	# @classmethod
	# def create(cls, title, pub_date):
	#     '''
	#         问题？这里面这样写是上面意思？不是说没有构造方法么？
				# 这样传参数 ？ 
	#     '''
	#     #book = cls(btitle = title,bpub_date=pub_date)

	#     book = BookInfo()
	#     book.btitle = title
	#     book.bpub_date = pub_date

	#     book.bread = 0
	#     book.bcommet = 0
	#     book.isDelete = 0
	#     return book

	class Meta():
		db_table = 'bookinfo'
		ordering = ['id']


class HeroInfo(models.Model):
	hname = models.CharField(max_length=10)
	hgender = models.BooleanField()
	Hcontent = models.CharField(max_length=1000)
	hBook = models.ForeignKey('BookInfo')
	isDelete = models.BooleanField(default=False)




class AreaInfo(models.Model):
	atitle = models.CharField(max_length=20)
	aparent = models.ForeignKey("self",null=True,blank=True)
	
	class Meta():
		db_table = 'areaInfo'