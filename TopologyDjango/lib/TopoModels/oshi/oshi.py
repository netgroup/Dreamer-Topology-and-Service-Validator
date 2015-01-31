import json
import pkgutil
import re

class oshi():

	


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
	
	def validate(self, topology):
		print "validate oshi"
		result = {}
		messages = []
		
		nodes = topology['vertices']
		edges = topology['edges']
		mappl2sw = {}
		
		for n in nodes.keys():
			if(nodes[n]['vertex_info'].get('node-type',"") == "L2sw"):
				mappl2sw[n] = 0

		### verifica che ogni nodo l2sw ha almeno tre CER
		for e in edges.keys():
			enodes = e.split('&&')
			nodef = enodes[0]
			nodet = enodes[1]
			for l in edges[e]['links']:
				if( l['link-type'] == "VS"):
					if(nodes[nodef]['vertex_info'].get('node-type',"") == "L2sw"):
						l2sw = nodef
					elif(nodes[nodet]['vertex_info'].get('node-type',"") == "L2sw"):
						l2sw = nodet

					mappl2sw[l2sw] = mappl2sw[l2sw] + 1

		for m in mappl2sw.keys():
			if(mappl2sw[m] < 3):
				messages.append({m: "connected with less than three CER"})
		if(len(messages) > 0):
			result = {'error':{'messages': messages}}
		
		return result


	"""docstring for Oshi"""
	def __init__(self, arg):
		#super(oshi, self).__init__()
		
		self.model_name = 'oshi'

		self.list_of_all_node_types = ["OSHI-CR", "OSHI-PE", "CE", "L2sw", "OF Controller"]

		self.list_of_all_layer = ["Data", "Vll", "PW", "VS", "Control"]

		self.graph_parameters = {
			"tunneling": "OPENVPN",
			"testbed": "MININET",
			"mapped": "",
			"vlan":"",
			"generated":""
		}

		self.nodes = {}

		self.nodes["OSHI-CR"] = {
			"node_label" : 'cro',
			"properties": {
				"custom_label" : "",
				"loopback": "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{

				}

			}
		}

		self.nodes["L2sw"] = {
			"node_label" : 'l2sw',
			"properties": {
			"custom_label" : "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				}
			}
		}

		self.nodes["OSHI-PE"] = {
			"node_label" : 'peo',
			"properties": {
			"custom_label" : "",
				"loopback": "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{

				}	
			}
		}

		self.nodes["CE"] = {
			"node_label" : 'cer',
			"properties": {
			"custom_label" : "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				}
			}
		}

		self.nodes["OF Controller"] = {
			"node_label" : 'ctr',
			"properties": {
			"custom_label" : "",
				"tcp_port": "6633",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{

				}
			}
		}

		self.layer_constraints = {}

		self.layer_constraints["Data"] = {
			"list_of_nodes_layer":["OSHI-CR", "OSHI-PE", "CE", "OF Controller"],
            "multihoming": "false",
			"not_allowed_edge":[
				{"source":"CE", 
					"not_allowed_des":[
						"OSHI-CR",  "OF Controller"] }, 
				{"source":"OSHI-CR", 
					"not_allowed_des":[
						"CE"] }, 
				{"source":"OSHI-PE", 
					"not_allowed_des":[
						"CE", "OF Controller"] }, 
				{"source":"OF Controller", 
					"not_allowed_des":
						["OSHI-PE", "CE", "OF Controller"] } ],
			"edges-properties": {
				"bw": ""
			  }
		}

		self.layer_constraints["Vll"] = {
         	"list_of_nodes_layer":["CE"],
         	"changing_nodes_type":'false',
         	"insert_new_node":'false' }

		self.layer_constraints["PW"] = {
			"list_of_nodes_layer":["CE"],
			"changing_nodes_type":'false',
         	"insert_new_node" : 'false'
        }

		self.layer_constraints['Control'] = {
        	"list_of_nodes_layer":[
            	"OSHI-CR",
            	"OSHI-PE",
            	"OF Controller"
         	],
            "not_allowed_edge":[
                {"source":"OSHI-CR",
                	"not_allowed_des": ["OSHI-CR", "OSHI-PE", "CE", "OF Controller"] },
             	{"source":"OSHI-PE",
                	"not_allowed_des": ["OSHI-CR", "OSHI-PE", "CE", "OF Controller"] },
                {"source":"OF Controller",
                	"not_allowed_des": ["OSHI-CR", "OSHI-PE", "CE", "OF Controller"] }],
            "changing_nodes_type":"false",
            "insert_new_node":"false",
            "nodes-properties":{
						"cluster_id": ""
				}
		}
		
		self.layer_constraints['VS'] = {
			"list_of_nodes_layer" :["L2sw", "CE"],
			"not_allowed_edge":[{"source" : "CE", "not_allowed_des": ["OSHI-CR", "CE", "OSHI-PE", "OF Controller"]},
			{"source" : "L2sw", "not_allowed_des": ["OSHI-CR", "OSHI-PE", "L2sw", "OF Controller"]}],
			"changing_nodes_type": "false"
		}
#if __name__ == '__main__':
#	test = oshi('ciao')
#	print test.to_JSON()

