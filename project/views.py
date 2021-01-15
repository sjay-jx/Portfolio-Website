from django.shortcuts import render


def index(request):
	"""Return the homepage for the website"""
	return render(request, 'project/index.html')