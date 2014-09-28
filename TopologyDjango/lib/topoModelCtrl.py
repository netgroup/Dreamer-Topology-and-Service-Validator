import pkgutil
import sys
import os
import imp
import json
#from TopoModels.oshi.oshi import oshi

class ModelController():

	

	def jsonmodel(self, modelname):

		try: #gestire meglio la definizione del path del modello
			x = __import__('TopologyDjango.lib.TopoModels.'+modelname+'.'+modelname,fromlist=[modelname] )
		except ImportError, e:
			print "import error! %s" % e
			return json.dumps({ 'error': {'message': 'Model Spec not found'} })
		try:
			cls = getattr(x,modelname)
		except AttributeError, e:
			print "AttributeError!"
			return json.dumps({ 'error': {'message': 'Model Spec not found'} })
		a = cls('')
		#if(modelname == 'oshi'):
		#	a = oshi('')
		#else:
		#	return {}
	
		return a.to_JSON()

	"""docstring for ModelController"""
	def __init__(self, arg):
		#super(ModelController, self).__init__()
		self.arg = arg

	def validateTopology(self, topology, modelname):
		result = {}
		#example = {"vertices": {"3": {"pos": {"x": 477.3105529387208, "y": 359.5564421318443 }, "v": {"x": 0.0035644859802187456, "y": -0.0003678184322717711 }, "vertex_info": {"frozen": "false" } }, "OSHI-CR#01": {"pos": {"x": 571.645587789206, "y": 260.57006773541957 }, "v": {"x": -0.0005012924164955468, "y": -0.008078636265402117 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-CR"} }, "OSHI-CR#02": {"pos": {"x": 343.46842265480825, "y": 265.1071814627707 }, "v": {"x": 0.0003789057184639122, "y": -0.0017395130358406896 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-CR"} }, "OSHI-CR#03": {"pos": {"x": 430.39318093174245, "y": 199.05731743393878 }, "v": {"x": -0.002163273333355198, "y": -0.0028420946490407273 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-CR"} }, "OSHI-CR#04": {"pos": {"x": 243.8844992787802, "y": 183.27015249856393 }, "v": {"x": -0.004556435119165703, "y": 0.000016304893190211 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-CR"} }, "OSHI-CR#05": {"pos": {"x": 529.2382245698698, "y": 173.06882694953057 }, "v": {"x": -0.0034116077547209356, "y": -0.005871884333641275 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-CR"} }, "OSHI-PE#06": {"pos": {"x": 640.3849197006057, "y": 339.19156652333174 }, "v": {"x": -0.00742332678703711, "y": 0.0003708985499277784 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-PE"} }, "OSHI-PE#07": {"pos": {"x": 312.58904093980925, "y": 353.34617200846276 }, "v": {"x": 0.005391255918603288, "y": -0.00000590230079858256 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-PE"} }, "OSHI-PE#08": {"pos": {"x": 303.91447641624836, "y": 110.06143678318273 }, "v": {"x": -0.005137044154760628, "y": -0.001232734466973251 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-PE"} }, "OSHI-PE#09": {"pos": {"x": 582.1536223214617, "y": 65.852377971866 }, "v": {"x": -0.001482757906184684, "y": -0.0024401659616921645 }, "vertex_info": {"frozen": "false", "node-type": "OSHI-PE"} }, "L2SW#10": {"pos": {"x": 729.7399333452596, "y": 283.445290257405 }, "v": {"x": -0.0008653721268885653, "y": 0.01443851734511814 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "L2SW#11": {"pos": {"x": 338.949857882099, "y": 38.695333142850856 }, "v": {"x": -0.0023467513834182496, "y": 0.00012013969347424158 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "L2SW#12": {"pos": {"x": 217.37206502183986, "y": 50.70980541461902 }, "v": {"x": -0.003724114635455855, "y": -0.0003094759959772764 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "L2SW#13": {"pos": {"x": 221.32874070071674, "y": 352.0507559846285 }, "v": {"x": 0.007276436751229354, "y": 0.00102747353644074 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "L2SW#14": {"pos": {"x": 398.85044697434125, "y": 361.74708348239415 }, "v": {"x": 0.004052367263665424, "y": -0.0003953079103612752 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "L2SW#15": {"pos": {"x": 504.2728676036877, "y": 40.183063551670266 }, "v": {"x": -0.002470467246925734, "y": -0.00045277093720762305 }, "vertex_info": {"frozen": "false", "node-type": "L2SW"} }, "CE#16": {"pos": {"x": 124.27399147231507, "y": 58.74509547499744 }, "v": {"x": -0.0042285172653654945, "y": 0.0004570623048270467 }, "vertex_info": {"frozen": "false", "node-type": "CE"} }, "CE#17": {"pos": {"x": 430.73011781981313, "y": 41.18049787164649 }, "v": {"x": -0.002547450215794278, "y": -0.00022835299889285756 }, "vertex_info": {"frozen": "false", "node-type": "CE"} }, "CE#18": {"pos": {"x": 736.4952754707438, "y": 178.71981153966888 }, "v": {"x": 0.00030596100178620356, "y": 0.014412333046186554 }, "vertex_info": {"frozen": "false", "node-type": "CE"} }, "CE#20": {"pos": {"x": 126.88083720945107, "y": 339.46679319440915 }, "v": {"x": 0.008556819703654461, "y": 0.0018314490720695437 }, "vertex_info": {"frozen": "false", "node-type": "CE"} } }, "edges": {"OSHI-CR#05&&OSHI-CR#01": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-CR#03&&OSHI-CR#01": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-CR#03&&OSHI-CR#04": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-CR#03&&OSHI-CR#02": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-PE#07&&OSHI-CR#02": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-PE#08&&OSHI-CR#05": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-PE#08&&OSHI-CR#04": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-PE#09&&OSHI-CR#03": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "OSHI-PE#06&&OSHI-CR#01": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#12&&OSHI-PE#08": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#11&&OSHI-PE#08": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#13&&OSHI-PE#07": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#14&&OSHI-PE#07": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#10&&OSHI-PE#06": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#15&&OSHI-PE#09": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "L2SW#13&&CE#20": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "3&&L2SW#14": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "CE#18&&L2SW#10": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "CE#17&&L2SW#15": {"links": [{"link_label": "ciao", "link-type": "Data"} ] }, "CE#16&&L2SW#12": {"links": [{"link_label": "ciao", "link-type": "Data"} ] } }, "graph_parameters": {} }
		#topology = example

		model = self.jsonmodel(modelname)
		print (model)
		###validazione nodi
		jsontopology = json.loads(topology)
		resvnodes = self.validateNodes(jsontopology['vertices'], model);

		if("error" in resvnodes):
			result = resvnodes
		

		resvedges = self.validateEgdes(jsontopology['edges'], model);

		if("error" in resvedges):
			result = resvedges
		 


		return result

	def validateNodes(self, nodes, model):
		result = {}


		return result

	def validateEgdes(self, edges, model):
		result = {}

		return result


if __name__ == '__main__':
	test = ModelController('ciao')
	print test.jsonmodel('oshi')