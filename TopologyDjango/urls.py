from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from TopologyDjango.lib.topoModelCtrl import ModelController

#mctrl = ModelController('prova')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TopologyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	url(r'^getSpecModel/$',"TopologyDjango.views.getSpecModel"),
	url(r'^getRandom/$',"TopologyDjango.views.getRandom"),
	url(r'^validateTopology$',"TopologyDjango.views.validate"),

)
