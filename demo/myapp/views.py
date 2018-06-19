from django.shortcuts import render

# Create your views here.
def register(request):
	if request.method=='POST':
		post=Register()
		post.name=request.POST.get('name')
		post.email=request.POST.get('email')
		post.dof=request.POST.get('dof')
		post.password=request.POST.get('password')
	return render(request,'index.html')