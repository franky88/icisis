from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import SubjectForm
from .models import Subject
# Create your views here.
@login_required
def subjectIndex(request):
	subject_list = Subject.objects.all().order_by('-id')
	query = request.GET.get("q")
	if query:
		subject_list = subject_list.filter(
			Q(subject_code__icontains=query) |
			Q(descriptive_title__icontains=query) 
			).distinct()
	context = {
		"title": "Subjects List",
		"subjectlist": subject_list, 
		"searchPlaceHolder": "Search subjects",
	}
	return render(request, "subjects/subject_home.html", context)

@login_required
def subjectDetail(request, pk):
	instance = get_object_or_404(Subject, pk=pk)
	context = {
		"title": "Subject Details",
		"instance": instance,
	}
	return render(request, "subjects/subject_detail.html", context)

@login_required
def addSubject(request):
	if request.method == 'POST':
		form = SubjectForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			addsubject=form.save(commit=False)
			addsubject.save()
			return redirect('subject:detail', pk=addsubject.pk)
	else:
		form = SubjectForm()
	context = {
		"form": form,
		"title": "Add Subject",
	}
	return render(request, "subjects/add_subject.html", context)

@login_required
def editSubject(request, pk):
	instance=get_object_or_404(Subject, pk=pk)
	form = SubjectForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('subject:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "Edit Subject Informations",
		"instance": instance,
	}
	return render(request, "subjects/edit_subject.html", context)