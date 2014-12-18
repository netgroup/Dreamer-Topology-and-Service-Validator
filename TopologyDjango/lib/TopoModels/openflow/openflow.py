import json
import pkgutil

class openflow():

	


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
	


	"""docstring for OpenFlow"""
	def __init__(self, arg):
		#super(oshi, self).__init__()
		
		self.model_name = 'openflow'

		self.list_of_all_node_types = ["OFL2sw", "Host", "OF Controller"]

		self.list_of_all_layer = ["Data",  "Control"]

		self.graph_parameters = {
			"tunneling": "",
			"testbed": "",
			"mapped": "",
			"vlan":"",
			"generated":""
		}

		self.nodes = {}

		self.nodes["OFL2sw"] = {
			"node_label" : 'ofl2sw',
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
            "multihoming": "false",

			"edges-properties": {
				"bw": ""
			  }
			}
		

		

		self.layer_constraints['Control'] = {
        	"list_of_nodes_layer":[
            	"OFL2sw",
            	"OF Controller"
         	],
            "changing_nodes_type":"false",
            "insert_new_node":"false"

		} 


#if __name__ == '__main__':
#	test = oshi('ciao')
#	print test.to_JSON()

