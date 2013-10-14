from directorio.models import negocio
from django.shortcuts import render_to_response,get_object_or_404,render_to_response,render
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
	n = negocio.objects.all()
	template = 'index.html'
	return render(request, template,{
		'negocio' : n,
		'request' : request,
})