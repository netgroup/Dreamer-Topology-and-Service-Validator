from django.http import HttpResponse
from lib.topoModelCtrl import ModelController
from lib.nxrand_builder import RandomBuilder
import json

def getSpecModel(request):
	modelname = request.GET.get('model')
	mctrl = ModelController('')
	response = mctrl.jsonmodel(modelname)
	return HttpResponse(response, content_type="application/json")

def getRandom(request):
	response = {}
	n = request.GET.get('n')
	p = request.GET.get('p')
	builder = RandomBuilder(n,p)
	response = builder.getJson()
	return HttpResponse(response, content_type="application/json")


def validate(request):

	response = {}
	response['error'] = 'false'
	modelname = request.POST.get('modelname')
	topology = request.POST.get('topology')
	print topology
	mctrl = ModelController('')
	#response = mctrl.validateTopology(topology,modelname)
	# topology = request.POST.get('topology')
	# print topology
	# mctrl = ModelController('')
	# response = mctrl.jsonmodel(modelname)
	print response
	return HttpResponse(json.dumps(response), content_type="application/json")
