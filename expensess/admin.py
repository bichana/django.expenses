from django.contrib import admin

# Register your models here.
"""
	家計簿
	admin用の設定

	Filename admin.py
	Date: 2020.3.7
	Written by Nobuharu Shimazu

"""
from django.contrib import admin
from .models import Expensess,Category

admin.site.register(Expensess)
admin.site.register(Category)



######### admin2はnobu8717
