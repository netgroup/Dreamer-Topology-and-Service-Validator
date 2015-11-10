import json
import pkgutil

class ciscoapic():

	


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
	
	def validate(self, topology):
		result = {}
		return result

	"""docstring for ciscoapic"""
	def __init__(self, arg):
		#super(oshi, self).__init__()
		
		self.model_name = 'ciscoapic'

		self.list_of_all_node_types = ["Host", "Switch", "Router"]

		self.list_of_all_layer = ["Data",  "Control"]

		self.graph_parameters = {
			"tunneling": "OPENVPN",
			"testbed": "MININET",
			"mapped": "",
			"vlan":"",
			"generated":""
		}

		self.nodes = {}

		self.nodes["Switch"] = {
			"node_label" : 'switch',
			"properties": {
			"custom_label" : "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				}
			}
		}

		self.nodes["Host"] = {
			"node_label" : 'host',
			"properties": {
			"custom_label" : "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				}
			}
		}

		self.nodes["Router"] = {
			"node_label" : 'router',
			"properties": {
			"custom_label" : "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
			}
		}

		self.layer_constraints = {}

		self.layer_constraints["Data"] = {
            "multihoming": "false",
            "not_allowed_edge":[
            	{"source" : "Router", "not_allowed_des": []},
            	{"source" : "OFL2sw", "not_allowed_des": []},
            	{"source" : "Host", "not_allowed_des": []}
            	],
			"edges-properties": {
				"bw": ""
			  }
		}
		

		

		self.layer_constraints['Control'] = {
        	"list_of_nodes_layer":[
            	"Router",
            	"Switch"
         	],
            "changing_nodes_type":"false",
            "insert_new_node":"false"

		} 


#if __name__ == '__main__':
#	test = oshi('ciao')
#	print test.to_JSON()

