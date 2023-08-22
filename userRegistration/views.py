from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .form import UserForm
from .models import UserReg


# Create your views here.
def testing(request):
    return HttpResponse("Hello this for testing")

def display(request):
    form = UserForm()
    userInfo = UserReg.objects.all()
    return render(request, "userRegistration/index.html", {"form" : form, "userInfo" : userInfo})

def saveForm(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            uid = request.POST.get("userId")
            nm = request.POST['name']
            em = fm.cleaned_data['email'] 
            pm = fm.cleaned_data['password']
            if(uid == ""):
                res = UserReg(name=nm, email=em, password=pm)
            else:
                res = UserReg(id=uid, name=nm, email=em, password=pm)
            
            res.save()
            userData = list(UserReg.objects.values())
            fm = UserForm()
            return JsonResponse({'status' : 'success', 'userData' : userData})
        else:
            return JsonResponse({'status' : 0}) 
        
# 
def delete_user(request):
    if request.method == "POST":
        # name = request.POST.get('name')
        sid = request.POST.get('sid')
        print(sid)
        uid = UserReg.objects.get(pk = sid)
        uid.delete()
        userData = list(UserReg.objects.values())
        return JsonResponse({'status' : 'success', 'userData' : userData})
    
def edit_user(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        uid = UserReg.objects.get(pk = id)
        fm = UserForm(request.POST, instance=uid)
        userData = {"id" : uid.id,"name" : uid.name, "email" : uid.email, "password" : uid.password}
        return JsonResponse({"userData" : userData, "status" : "success"})
        
