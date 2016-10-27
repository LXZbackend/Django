#coding=utf-8
from django.shortcuts import render
from django.http import *
from models import *

# Create your views here.


def cityTest(request):
	return render(request, 'booktest/cityTest.html')


# def pro(requset):
#     list1 = AreaInfo.objects.filter(aParent__isnull=True)
#     list2 = []
#     for area in list1:
#         list2.append({"id": area.id, "title": area.atitle})
#     data = {'list': list2}
#     print data
#     return JsonResponse(data)


def pro(request):
		# 获取上级为空的  返回的是一个列表
	list1 = AreaInfo.objects.filter(aParent__isnull=True)
	print list1
	list2 = []
	# 这里注意 因为JsonRespons  只能返回一个字典 所以得对列表进行从新组装格式
	for area in list1:
		list2.append({"id": area.id, 'title': area.atitle})
	data = {'list': list2}
	return JsonResponse(data)


def pro2(request, id):
		# 这是根据传进来的id 上一级id 获取他的关联的所有的数据
	list1 = AreaInfo.objects.get(pk=id).areainfo_set.all()

	list2 = []
	for area in list1:
		list2.append({"id": area.id, 'title': area.atitle})

	data = {'list': list2}

	return JsonResponse(data)
