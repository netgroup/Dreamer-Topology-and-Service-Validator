import json
import pkgutil

class oshi():

	


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
	


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

