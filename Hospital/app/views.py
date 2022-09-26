from django.shortcuts import render,redirect
from .forms import PatientForm,DoctorForm
from .models import Doctor,Patient
# Create your views here.


def Dashboard(request):
  if request.session.get("user")==None:  
    return redirect("login")
  user=request.session.get("user")
  name=request.session.get("name")
  return render(request,"app/dashboard.html",{"name":name,"user":user})
  
def Signup(request): 
  if request.session.get("name")!=None:
    return redirect("dashboard")
  msg=''
  if request.method=='POST':
    fm=PatientForm(data=request.POST,files=request.FILES)
    print("-------------------Aftter validation------------------------")
    if fm.is_valid():
      user=fm.cleaned_data["user"]
      print("-------------------before validation------------------------")
      print("----------------------------------------------")
      print("user:",user,user=="Patient")
      print("-----------------------------------------------")
      if user=="Patient":
        print("patient save---------------------------  ")
        fm.save()
        msg="Patient-your are successfully registerd !!!"
        fm=PatientForm()
      else:
        first_name=fm.cleaned_data["first_name"]
        last_name=fm.cleaned_data["last_name"]
        profile_picture=fm.cleaned_data["profile_picture"]
        username=fm.cleaned_data["username"]
        email=fm.cleaned_data["email"]
        password=fm.cleaned_data["password"]
        confirm_password=fm.cleaned_data["confirm_password"]
        address1=fm.cleaned_data["address1"]
        city=fm.cleaned_data["city"]
        state=fm.cleaned_data["state"]
        pincode=fm.cleaned_data["pincode"]
        d=Doctor(first_name=first_name,last_name=last_name,profile_picture=profile_picture,username=username,email=email,password=password,confirm_password=confirm_password,address1=address1,city=city,state=state,pincode=pincode)
        d.save()
        print("doctor save  ---------------------------  ")
        msg="Doctor-your are successfully registerd !!!"
        fm=PatientForm()
      
  else:
    fm=PatientForm()

  return render(request,"app/signup.html",{"fm":fm,"msg":msg})

def Login(request):
  if request.session.get("name")!=None:
    return redirect("dashboard")
  errors=""
  if request.method=="POST":    
    email=request.POST['email']
    password=request.POST['password']
    errors=None     
    try:
      if request.POST['user']=="Patient":
        User=Patient.objects.get(email=email)
      else:
        User=Doctor.objects.get(email=email)
    except:
      errors='Enter valid email and password !!!'
      
    if not errors:
      if password==User.password:
        request.session["user"]=request.POST["user"]
        request.session["name"]=User.first_name
        request.session["email"]=User.email
        return redirect("dashboard")
      else:
        errors='Enter valid  password !!!'
    
  form=PatientForm()
  return render(request,"app/login.html",{"forms":form,"errors":errors})

def logout(request):
  request.session.flush()
  return redirect('login')

