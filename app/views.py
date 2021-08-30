from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import CustomerRegistrationForm, CustomerProfileForm
# Create your views here.
from app.models import Home, Customer


def home(request):
    if request.method == 'GET':
        movie=Home.objects.all()
        context={
            'movie': movie,
        }
    return render(request, 'home.html', context)

class CustomerRegistrationView(View):
 def get(self,request):
  form = CustomerRegistrationForm()
  return render(request, 'customerregistration.html', {'form':form})

 def post(self,request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulations! You have registered successfully')
   form.save()
  return render(request, 'customerregistration.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(self,request):
  form=CustomerProfileForm()
  return  render(request,'profile.html',{'form':form, 'active':'btn-primary'})

 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   user = request.user
   name=form.cleaned_data['name']
   phone=form.cleaned_data['phone']
   locality=form.cleaned_data['locality']
   city=form.cleaned_data['city']
   zipcode=form.cleaned_data['zipcode']

   reg = Customer(user=user, name=name, phone=phone, locality=locality, city=city, zipcode=zipcode)
   reg.save()
   messages.success(request,'Congratulations! Your Profile is updated Successfully')

  return render(request, 'profile.html',{'form':form, 'active':'btn-primary'})


# @login_required
# def bookseat(request):
#  if request.method == 'POST'
