from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Student, StudentInfo
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, StudentInfoForm
from django.contrib import messages
# Create your views here.

@login_required
def studentIndex(request):
	student_list = Student.objects.all().order_by('-date_updated', 'timestamp')
	query = request.GET.get("q")
	if query:
		student_list = student_list.filter(
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query) |
			Q(middle_name__icontains=query) |
			Q(lrn_or_id_number__icontains=query) 
			).distinct()
	paginator = Paginator(student_list, 10)
	page = request.GET.get('page')
	try:
		student_list = paginator.page(page)
	except PageNotAnInteger:
		student_list = paginator.page(1)
	except EmptyPage:
		student_list = paginator.page(paginator.num_pages)
	context = {
		"title": "Student Index",
		"studentlist": student_list,
		"searchPlaceholder": "Search by LRN or name",
	}
	return render(request, 'students/student_list.html', context)

@login_required
def studentDetail(request, pk):
	instance = get_object_or_404(Student, pk=pk)
	context = {
		"title": "Student Informations",
		"instance": instance,
	}
	return render(request, "students/student_detail.html", context)

@login_required
def addStudent(request):
	if request.method == 'POST':
		form = StudentForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			addstudent=form.save(commit=False)
			addstudent.save()
			return redirect('student:detail', pk=addstudent.pk)
	else:
		form = StudentForm()
	context = {
		"form": form,
		"title": "Register Student",
	}
	return render(request, "students/add_student.html", context)

@login_required
def editStudent(request, pk):
	instance=get_object_or_404(Student, pk=pk)
	form = StudentForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "Edit Student Informations",
		"instance": instance,
	}
	return render(request, "students/edit_student.html", context)

@login_required
def addStudentInfo(request):
	if request.method == 'POST':
		form = StudentInfoForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			addstudentinfo=form.save(commit=False)
			addstudentinfo.save()
			return redirect('student:detail', pk=addstudentinfo.pk)
	else:
		form = StudentInfoForm()
	context = {
		"form": form,
		"title": "add details",
	}
	return render(request, "students/add_detail_student.html", context)

@login_required
def editStudentInfo(request, pk):
	instance=get_object_or_404(StudentInfo, pk=pk)
	form = StudentInfoForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "Edit Student Informations",
		"instance": instance,
	}
	return render(request, "students/edit_student_info.html", context)

@login_required
def deleteStudent(request, pk):
	instance=get_object_or_404(Student, pk=pk)
	messages.warning(request, "Delete Student %s"%(instance.full_name))
	instance.delete()
	return redirect('student:studentindex')