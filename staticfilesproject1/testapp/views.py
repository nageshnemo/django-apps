from django.shortcuts import render
import datetime
# Create your views here.

def date_time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))

    if h < 12:
        msg = "hello guest !! very good morning!!!"
    elif h < 16:
        msg = "Hello guest !! very good afternoon!!!"
    elif h < 21:
        msg = "Hello guest !! very good evening!!!"
    else:
        msg = "Hello guest !! very good night!!!"

    my_dict = {'date':date,'msg':msg}
    return render(request,'testapp/results.html',my_dict)
    # we can also write context
