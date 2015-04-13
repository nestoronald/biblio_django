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
    def post(self, request, *args, **kwargs):
        s = request.POST['fieldSearch']
        items = Item.objects.filter(title__icontains=s)
        # return render(request, 'buscar.html')
        if items:
            # data = []
            # for item in items:
            #     authors =item.author.all()
            #     data.append(dict([(item,authors)]))
            return render(request,'buscar.html',{'items':items,'s':s})
        else:
            return render(request,'buscar.html',{'s':s})
