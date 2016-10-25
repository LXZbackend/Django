#coding=utf-8
from django.shortcuts import render
from models import *
from django.db.models import Max,F,Q

# Create your views here.
def index(requset):

	# list1 = BookInfo.book.all()
	# list1 = BookInfo.book.filter(isDelete = False)
	# list1 = BookInfo.book.filter(btitle__contains='传')
	# list1 = BookInfo.book.filter(btitle__endswith="传")
	# list1 = BookInfo.book.filter(btitle__isnull=False)
	# list1 = BookInfo.book.filter(pk__in=[1,2,4])
	# list1 = BookInfo.book.filter(pk__gt=3)
	# list1 = BookInfo.book.filter(bpub_date__year = 1980)
	# list1 = BookInfo.book.filter(heroinfo__hname__startswith="郭")
	# list1 = BookInfo.book.filter(bread__gt = F("bcommet") /2)
	# list1 = BookInfo.book.filter(pk__gt =3).filter(btitle__contains='传')
	# list1 = BookInfo.book.filter(Q(pk__gt = 3) |Q(btitle__contains='传'))
	# list1 = BookInfo.book.filter(Q(pk__gt=3)) #这时候跟单独写一个没啥区别


	# 聚集函数
	maxdate  = BookInfo.book.all().aggregate(Max('bpub_date'))



	# return render(requset,"booktest/index.html","woshi li")


	print maxdate
	return render(requset, 'booktest/index.html', { "maxdate": maxdate})
	# return render(requset,"booktest/index.html",{"list":list1})


def area(request):
	city = AreaInfo.objects.get(pk=130100)
	# 多对一   通过多的那个 访问一个 直接通本模式中值属性访问
	pro = city.aparent
	dis = city.areainfo_set.all()
	value = {
		"city":city,
		"pro":pro,
		'dis':dis

	}

	return render(request,'booktest/area.html',value)