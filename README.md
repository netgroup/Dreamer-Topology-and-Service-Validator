![Alt text](repo_data/dreamer-logo.png "Optional title")

Dreamer-Topology-and-Service-Validator
=======================================

Topology and Service Validator For Dreamer Project (GÉANT Open Call).

Overview
-----------
It is a [django](https://www.djangoproject.com/) app that stores the model/layer abstractions and their constraints, finally it is able to validate the topologies created through the [Dreamer-Topology-Designer](https://github.com/netgroup/Dreamer-Topology-Designer) project.

---------------------------

## Requires
-  django 1.6 
-  networkx ([can be found here](https://networkx.github.io/))

---------------------

Getting Started
---------------------

Assuming git installed:

```sh
$ git clone https://github.com/netgroup/Dreamer-Topology-and-Service-Validator.git
```

Start the application according to the configuration set in your Dreamer-Topology3D and Dreamer-Experiment-Handler instance

#####Start the Dreamer-Topology-and-Service-Validator project:
```sh
$ cd Dreamer-Topology-and-Service-Validator/
$ python manage.py runserver [host]:[port] 
```
#####for example:
```sh
$ python manage.py runserver 0.0.0.0:8001 
```

License
=======

This sofware is licensed under the Apache License, Version 2.0.

Information can be found here:
 [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).