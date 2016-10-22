#coding=utf-8
from django.contrib import admin

# Register your models here.
from models import *


class HeroInline(admin.StackedInline):
    model = HerInfo
    extra = 2


class BookAdmin(admin.ModelAdmin):
    inlines = [HeroInline]

    list_display = ['id', 'bittle', 'bpub_date']

class HerAdmin(admin.ModelAdmin):

	list_display = ['id','hname','hgender','Hcontent','hBook']




admin.site.register(BookInfo, BookAdmin)
admin.site.register(HerInfo,HerAdmin)
