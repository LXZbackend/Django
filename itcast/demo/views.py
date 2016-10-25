#coding=utf-8
from django.shortcuts import render

from models import BookInfo #下面用到这个数据库操作 所需要吧类引入
# 这是那三句话所需有的包
# from django.template import RequestContext,loader
# from django.http import HttpResponse

# Create your views here.

def index(request):

	booklist = BookInfo.objects.all()
	# 第一中方法 通过三部  先加载模板就是把模板引进来  context 是传的内容
	 # 然后再通过 返回 返回 渲染模板
	# 加载模板
	# 模板里面的占位符{{}}  在通过传入的参数改变
	# template = loader.get_template('demo/index.html') #加载模板

	# 往模板里传入字典类型的参数
	# context = RequestContext(request,{"list":booklist})

	# render 是渲染的意思
	# return HttpResponse(template.render(context))

	# 第二种方法 封装成一个方法 其实内部还是执行三句话

	return render(request,"demo/index.html",{"list":booklist})


def detail(request,id):
	# 同上
	book = BookInfo.objects.get(pk=id)
	# template = loader.get_template('demo/detail.html')
	# context = RequestContext(request,{"book":book})

	# return HttpResponse(template.render(context))
	return render(request,'demo/detail.html',{'book':book})
