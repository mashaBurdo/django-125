from django.http import HttpResponse
from django.shortcuts import render

lst_data = [4,3.5,(4,1,5),[6,7,2],'hello world']


def test(request):
    return HttpResponse('My first project')
def first(request):
    return render(request,'first.html',{'int':lst_data[0],'float':lst_data[1],'tuple':lst_data[2],'list':lst_data[3],'str':lst_data[4],'data':lst_data})
