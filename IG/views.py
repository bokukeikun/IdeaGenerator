from django.shortcuts import render
from datetime import datetime
from . import forms

def home(request):
#     now = datetime.now()
#     import random
#     import os

#     tech = random.choice(Tech_li)
#     industory = random.choice(Category_li)
#     feeling = random.choice(Feeling_li)
#     web = random.choice(Web_service_li)
#     religion = random.choice(Religion_li)

#     Comb = tech + "×" + industory + "×" + feeling

#     Comb2 = religion + "×" + feeling + "×" + web

#     context = {
#         'tech': tech,
#         'industory': industory,
#         'religion': religion,
#         'web': web,
#         'feeling': feeling,
#         'text': Comb,
#     }
    return render(request, 'IG/home.html')

# def category_forms(request):
#     form = forms.CategoryForm()
#     d = {
#         'form': form
#     }
#     return render(request, 'IG/form.html', d)

def category_forms(request):
    form = forms.CategoryForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'IG/form.html', d)
