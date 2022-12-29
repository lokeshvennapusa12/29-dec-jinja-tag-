from django.shortcuts import render

def jinja_tag1(request):
    d={'name':'Vennapusa Lokeswara Reddy','mobile':'0987654345678'}
    return render(request,'jinja_tag1.html',d)
