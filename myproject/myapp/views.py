from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CustomerRegistrationForm
# Create your views here.
def index(request):
    
    return render(request,'index.html')




# def registration_form(request):
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the data to the database
#             return redirect('index')  # Redirect to index page
#         else:
#             form = CustomerRegistrationForm()
    
#     return render(request, 'registration_form.html', {'form': form})


# from django.shortcuts import render, redirect
# from .forms import CustomerRegistrationForm  # Import your form

def registration_form(request):
    form = CustomerRegistrationForm()  # Initialize the form outside of the if statement

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('index')  # Redirect to the index page
    
    return render(request, 'registration_form.html', {'form': form})
