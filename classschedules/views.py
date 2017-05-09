from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from django.contrib.auth.decorators import login_required
from .forms import ScheduleForm
# Create your views here.
@login_required
def scheduleIndex(request):
	schedule_list = Schedule.objects.all()
	context = {
		"title": "class schedules",
		"schedulelist": schedule_list,
	}
	return render(request, "classschedule/classschedule_index.html", context)

@login_required
def scheduleDetail(request, pk):
	instance = get_object_or_404(Schedule, pk=pk)
	context = {
		"title": "Schedule Details",
		"instance": instance,
	}
	return render(request, "classschedule/schedule_detail.html", context)

@login_required
def addSchedule(request):
	if request.method == "POST":
		form = ScheduleForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			addschedule=form.save(commit=False)
			addschedule.save()
			return redirect('schedule:scheduleindex')

	else:
		form = ScheduleForm()
	context = {
			"title": "Add Schedule",
			"form": form,
			}
	return render(request, "classschedule/add_schedule.html", context)

@login_required
def editSchedule(request, pk):
	instance=get_object_or_404(Schedule, pk=pk)
	form = ScheduleForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('schedule:detail', pk=instance.pk)
	context = {
		"form": form,
		"title": "Edit Schedule Informations",
		"instance": instance,
	}
	return render(request, "classschedule/edit_schedule.html", context)