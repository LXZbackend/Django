#coding=utf-8
# from django.shortcuts import render
from django.http import HttpResponse
#coding=utf-8
from django.template import RequestContext,loader
from models import BookInfo
from models import HeroInfo

# Create your views here.
# 加载模板  渲染模板
def index(request):
	mylist = BookInfo.objects.all()
	template = loader.get_template("booktest/index.html")
	context = RequestContext(request,{"booklist":mylist})


	return HttpResponse(template.render(context))



def detail(request,id):
	book = BookInfo.objects.get(pk=id)
	template = loader.get_template("booktest/detail.html")
	context = RequestContext(request,{"book":book})
	return HttpResponse(template.render(context))


