from django.shortcuts import render

def jinja_tag(request):

    d={'name':'Lokesh Vennapusa','batch':'74YM1'}

    return render(request,'jinja_tag.html',d)
