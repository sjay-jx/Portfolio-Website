from django.shortcuts import render, get_object_or_404

from .models import Project


def index(request):
	"""Return the homepage for the website"""
	projects = Project.objects.all()
	context = {
		'projects':projects
	}
	return render(request, 'project/index.html',context)

def detail(request, project_id):
	"""Return the project details"""
	project = get_object_or_404(Project, id = project_id)
	context = {
		'project': project
	}
	return render(request, 'project/detail.html', context)