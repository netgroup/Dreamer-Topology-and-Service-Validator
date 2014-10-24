import json
import pkgutil

class oshi():

	


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
	


	"""docstring for Oshi"""
	def __init__(self, arg):
		#super(oshi, self).__init__()
		
		self.model_name = 'oshi'

		self.list_of_all_node_types = ["OSHI-CR", "OSHI-PE", "CE", "OF Controller"]

		self.list_of_all_layer = ["Data", "Vll", "Control"]

		self.graph_parameters = {
			"tunneling": "",
			"testbed": "",
			"mapped": "",
			"vlan":"",
			"generated":""
		}

		self.nodes = {}

		self.nodes["OSHI-CR"] = {
			"node_label" : 'cro',
			"properties": {
				"loopback": "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{
					"cluster_id": ""
				}

			}
		}

		self.nodes["OSHI-PE"] = {
			"node_label" : 'peo',
			"properties": {
				"loopback": "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{
					"cluster_id": ""
				}	
			}
		}

		self.nodes["CE"] = {
			"node_label" : 'cer',
			"properties": {
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{
					"cluster_id": ""
				}	
			}
		}

		self.nodes["OF Controller"] = {
			"node_label" : 'ctr',
			"properties": {
				"tcp_port": "",
				"vm":{
						"mgt_ip": "",
						"interfaces": ""
				},
				"domain-oshi":{
					"cluster_id": ""
				}
			}
		}

		self.layer_constraints = {}

		self.layer_constraints["Data"] = {
            "multihoming": "false",
			"not_allowed_edge":[
				{"source":"CE", 
					"not_allowed_des":[
						"OSHI-CR",  "OF Controller"] }, 
				{"source":"OSHI-CR", 
					"not_allowed_des":[
						"CE", "OF Controller"] }, 
				{"source":"OSHI-PE", 
					"not_allowed_des":[
						"CE", "OF Controller"] }, 
				{"source":"OF Controller", 
					"not_allowed_des":
						["OSHI-PE", "CE", "OF Controller"] } ]  }

		self.layer_constraints["Vll"] = {
         	"list_of_nodes_layer":["CE"],
         	"changing_nodes_type":'false',
         	"insert_new_node":'false' }

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
                	"not_allowed_des": ["OSHI-CR", "OSHI-PE", "CE", "OF Controller"] }
                	 ],
            "changing_nodes_type":"false",
            "insert_new_node":"false"} 


#if __name__ == '__main__':
#	test = oshi('ciao')
#	print test.to_JSON()

