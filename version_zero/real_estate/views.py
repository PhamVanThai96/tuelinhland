from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    
    context = {
        'projects': Project.objects.all(),
        'form': form
    }
    return render(request, 'home.html', context)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'real_estate/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'real_estate/project_detail.html', {'project': project})
