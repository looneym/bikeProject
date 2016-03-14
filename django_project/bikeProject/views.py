from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bikeProject.models import Counter
import json
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
# from login import settings

def index(request):
    return render(request, 'bikeProject/home.html')


def getRotationCount(request):

    counterSet =  Counter.objects.all()
    i = len(counterSet)
    mostRecent = counterSet[i-1]
    count = mostRecent.currentCount

    responseData = {}
    try:
        responseData['result'] = ['Success']
        responseData['message'] = [str(count)]
    except:
        responseData['result'] = ['Fail']
        responseData['message'] = ["Error fetching from DB"]

    return HttpResponse(json.dumps(responseData), content_type="application/json")


def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "bikeProject/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "bikeProject/myhome.html", {})

def Blog(request):
    return render(request, "bikeProject/blog.html", {})



# def success(request):
#     return render(request, 'bikeProject/success.html')

# def fail(request):
#     return render(request, 'bikeProject/fail.html')

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return render(request, 'bikeProject/success.html')
#         else:
#             return render(request, 'bikeProject/success.html')
#     else:
#         return render(request, 'bikeProject/fail.html')

# def index(request):
#     return render(request, 'personal/home.html')

# def contact(request):
#     return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me','hskinsley@gmail.com']})
