from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        if form_is_valid:

            return HttpResponseRedirect('home')
    return render(request,'index.html')