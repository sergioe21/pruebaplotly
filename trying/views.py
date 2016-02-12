from django.shortcuts import render
# Create your views here.

def show(request):

	sh = [4,-1,6]

	return render(request,'trying/show.html',{'pp':sh})
