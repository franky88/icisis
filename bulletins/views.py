from django.shortcuts import render

# Create your views here.
def bulletinIndex(request):
	context = {
		"title": "bulletins",
	}
	return render(request, "bulletins/bulletins_home.html", context)