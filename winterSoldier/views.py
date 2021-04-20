from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import myform1
from django.views.generic import TemplateView

from django.views import View   #This contains default 8 fixed fuctions- get, post, put, patch, delete, head, options, trace

class myFirstClass(View):
    optional="Hello Ashish"

    def get(self, request):
        fetch= myform1()
        return render(request, 'index.html',{'fetch':fetch})
        #return HttpResponse(self.optional)

    def post(self, request):
        name=request.POST['name']
        print(name)
        return HttpResponse('Form submitted!')

class variable_template(View):
    template_name='home.html'
    
    def get(self, request):
        return render(request, self.template_name)

class hello(myFirstClass, variable_template):
    
    def get(self, request):
        print(self.optional)
        return render(request, self.template_name, {'xyz':"Hello class"})