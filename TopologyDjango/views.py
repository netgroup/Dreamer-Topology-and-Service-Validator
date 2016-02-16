from django.http import HttpResponse
from lib.topoModelCtrl import ModelController
from lib.nxrand_builder import RandomBuilder
import json

def getSpecModel(request):
	modelname = request.GET.get('model')
	mctrl = ModelController('')
	response = mctrl.jsonmodel(modelname)
	#print response
	response =  HttpResponse(response, content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	return response

def getRandom(request):
	response = {}
	n = request.GET.get('n')
	p = request.GET.get('p')
	builder = RandomBuilder(n,p)
	response = builder.getJson()
	response =  HttpResponse(response, content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	return response


def validate(request):

	response = {}
	response['error'] = 'false'
	modelname = request.POST.get('modelname')
	topology = request.POST.get('topology')
	print modelname + "++++++"
	#print topology
	mctrl = ModelController('')
	response = mctrl.validateTopology(topology,modelname)
	# topology = request.POST.get('topology')
	# print topology
	# mctrl = ModelController('')
	# response = mctrl.jsonmodel(modelname)
	print response
	response =  HttpResponse(json.dumps(response), content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	return response

#return value of the traffic
def getValue(request):

	response = {}
	#response['errore'] = 'false'
	select_node = request.POST.get('node_id') 
	print select_node
	mctrl = ModelController('')
	response = mctrl.getValue(select_node)
	print response
	#print "sssssssssssssssssssssssss"
	response = HttpResponse(json.dumps(response),content_type ="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	print response
	return response

#return value Url Graph
def getGraph(request):

	response = {}
	select_node = request.POST.get('node_interface')
	select_time = request.POST.get('series_time')
	select_type = request.POST.get('type')
	mctrl = ModelController('')
	response = mctrl.getGraph(select_node,select_time,select_type)
	print response
	response  = HttpResponse(json.dumps(response),content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	print response
	return response

#return value file avaible
def getFileAvaible(request):


	response = {}
	first_node = request.POST.get('node_first')
	second_node = request.POST.get('node_second')
	mctrl = ModelController('')
	response = mctrl.getFileAvaible(first_node,second_node)
	# print response
	response  = HttpResponse(json.dumps(response),content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	# print response
	return response
