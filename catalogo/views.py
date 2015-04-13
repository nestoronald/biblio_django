from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from .models import Item
# Create your views here.
def home(request):    
    return render_to_response('home.html',context_instance=RequestContext(request))

def logout_view(request):
    logout(request)

class SearchView(TemplateView):	
	#template_name = "buscar.html"
	def post(self, request, *args, **kwargs):
		s = request.POST['fieldSearch']		
		items = Item.objects.filter(title__contains=s)
		print items
		return render(request, 'buscar.html')
		