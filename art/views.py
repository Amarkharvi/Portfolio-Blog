from django.shortcuts import render

# Create your views here.
def artFun(request):
	return render(request, 'artWork.html')