#coding=utf-8
from django.contrib import admin
from models import BookInfo
from models import HeroInfo


# 关联注册  就是再创建书名的时候 给他添加英雄
class HeroInfoInline(admin.StackedInline):
	model = HeroInfo
	extra = 2




class BookAdmin(admin.ModelAdmin):
	list_display = ['pk','bittle','bpub_date']
	inlines = [HeroInfoInline]
	# 过滤字段 过滤会显示再右边
	# list_filter =['bittle']
	search_fields = ['btitle']

class HeroAdmin(admin.ModelAdmin):
	list_display = ["id",'hname','gender','hcontent']


# 上面的类是显示的格式，创建完了 需要给注册的表调用才有用
admin.site.register(BookInfo,BookAdmin)
admin.site.register(HeroInfo,HeroAdmin)
# Register your models here.
