from django.shortcuts import render

# Create your views here.
# render is basically a fn use to get a response of request,results.html
# render function return type is HttpResponse


from django.http import HttpResponse
import datetime
# there is no need to import this

def template_view(request):
    dt = datetime.datetime.now()
    my_dict = {'date':dt}
    return render(request,'testapp/results.html',context = my_dict)
