from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from instructors.models import Instructor
from subjects.models import Subject
from .forms import InstructorForm
from main.models import Department
# Create your views here.
@login_required
def instructorIndex(request):
	department_list = Department.objects.all()
	instructor_list = Instructor.objects.all().order_by('-id')
	query = request.GET.get("q")
	if query:
		instructor_list = instructor_list.filter(
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query) |
			Q(middle_name__icontains=query)
			).distinct()
	context = {
		"title": "Instructor's List",
		"instructorslist": instructor_list,
		"departmentlist": department_list,
		"searchPlaceHolder": "Search instructor",
	}
	return render(request, "instructors/instructor_home.html", context)

@login_required
def instructorDetail(request, pk):
	instance = get_object_or_404(Instructor, pk=pk)
	context = {
		"title": "Instructor's Information",
		"instance": instance,
	}
	return render(request, "instructors/instructor_detail.html", context)

@login_required
def addInstructor(request):
	if request.method == "POST":
		form = InstructorForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			addinstructor=form.save(commit=False)
			addinstructor.save()
			return redirect('instructor:instructorindex')

	else:
		form = InstructorForm()
	context = {
			"title": "Add Instructor",
			"form": form,
			}
	return render(request, "instructors/add_instructor.html", context)

@login_required
def editInstructor(request, pk):
	instance=get_object_or_404(Instructor, pk=pk)
	form = InstructorForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('instructor:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "Edit Instructor's Informations",
		"instance": instance,
	}
	return render(request, "instructors/edit_instructor.html", context)