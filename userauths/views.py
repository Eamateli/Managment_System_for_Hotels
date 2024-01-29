from django.shortcuts import render
from userauths.models import User, Profile
from userauths.forms import UserRegisterForm

def RegisterView(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.clean_password2.get("full_name")
        
        
        
        
        
    context = {
        "form":form
    }
    return render(request,"userauths/sign-up.html", context)
    
    
