from django.http import HttpResponse
import requests as req

# Create your views here.
def index(request):
	return HttpResponse("Hello world!")