from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method=='POST':
		post=Register()
		# post.id=request.POST.get('id')
		post.name=request.POST.get('name')
		post.email=request.POST.get('email')
		post.dof=request.POST.get('dof')
		post.doj=request.POST.get('doj')
		post.salary=request.POST.get('salary')
		post.password=request.POST.get('password')

		post.save()
		# return HttpRespose("success")

	return render(request,'index.html')
def show(request):
	form=Register.objects.filter(id='1')
	return render(request,'show.html',{"form":form})
def sendmail(request,deepa8354@gmail.com):
	res=send_mail("hello i.name","abcd","vijayalaxmi7062@gmail.com",[deepa8534@gmail.com])	
	return HttpResponse('%s'%res)