

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm  # Or your custom form
from .forms import RegistrationForm
# Create your views here.




def loginPage(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request,'registration/login.html')
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            # login(request, user)
            return render(request,'home.html')
            # return redirect('home')  # Redirect to your desired URL after successful registration
            # print(user.username)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})