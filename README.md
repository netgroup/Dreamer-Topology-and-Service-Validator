![Alt text](repo_data/dreamer-logo.png "Optional title")

Dreamer-Topology-and-Service-Validator
=======================================

Topology and Service Validator For Dreamer Project (GÉANT Open Call).

It is a [django](https://www.djangoproject.com/) app that stores the model/layer abstractions and their constraints, finally it is able to validate the topologies created through the [Dreamer-Topology-Designer](https://github.com/netgroup/Dreamer-Topology-Designer) project.

License
=======

This sofware is licensed under the Apache License, Version 2.0.

Information can be found here:
 [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

Tips
==============

Start the application according to the configuration set in your Dreamer-Topology-Designer instance.

#####Start the Dreamer-Topology-and-Service-Validator project:

		cd Dreamer-Topology-and-Service-Validator/
		python manage.py runserver 0.0.0.0:8001 


Topololgy and Service Validator Dependencies
=================================================

1) django 1.6 (pip)

2) networkx (pip)


