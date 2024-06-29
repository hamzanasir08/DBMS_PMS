
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages

# Create your views here.



def loginPage(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    # Authenticate the user based on email (as you're using email as username)
    user = authenticate(email=email, password=password)

    if user is not None:
      login(request, user)  # Login the user if credentials are valid
      return redirect('home')  # Redirect to the home page after successful login
    else:
      # Handle unsuccessful login attempt (e.g., display error message)
      messages.error(request,'Invalid login credentials. Please try again.')

  return render(request, 'registration/checklogin.html')


def home(request):
    return render(request,'home.html')

def signup(request):
  if request.method == 'POST':
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone')
    cnic = request.POST.get('cnic')

    # Validate data (optional)
    # ... add validation logic here ...

    phNum_status = False
    cnic_status = False
    try:
        # chk if ph num is in digits
        ph_chk = int(phone_number)
    except ValueError:
        messages.error(request, 'Phone number is invalid.')
    else:
        # chk if ph num is 11 digits long
        if len(phone_number) == 11:
            phNum_status = True
                      
    try:
      cnicChk = int(cnic)
    except ValueError:
      messages.error(request, 'CNIC is invalid.')
    else:
        if len(cnic) == 13:
           cnic_status = True

    if phNum_status == True and cnic_status == True:
      if CustomUser.objects.filter(email=email).exists():
        messages.error(request, 'Email already exists!')
      elif CustomUser.objects.filter(cnic = cnic).exists():
        messages.error(request,'cnic already exists.')
      elif CustomUser.objects.filter(phone_number = phone_number).exists():
        messages.error(request,'phone number already exists.')
      else:
        user = CustomUser.objects.create_user(
           username = email,
           email=email,
           password=password,
           first_name=first_name,
           last_name=last_name,
           cnic=cnic,
           phone_number=phone_number
        )
        if user is not None:
           login(request, user)  # Login the user
           return redirect('home')  # Redirect to the home page after successful login
        else:
          # Handle user creation error (e.g., display message)
          messages.error(request,'User creation failed. Please try again.')
          # print('User creation failed. Please try again.')
    else:
      messages.error(request, f'Failed to register, ensure your data is entered properly.')
  return render(request, 'registration/checkregister.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')