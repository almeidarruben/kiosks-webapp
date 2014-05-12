from django.conf.urls import patterns, url

urlpatterns = patterns('paginas.views',
	url(r'^get/pagina/(?P<pagina>\d+)$', 'get_pagina', name='get_pagina'),
	url(r'^get/categoria/(?P<categoria>\d+)$', 'get_categoria', name='get_categoria'),
	url(r'^get/items/(?P<listagem>\d+)$', 'get_items', name='get_items'),
	url(r'^get/sliders/', 'get_sliders', name='get_sliders'),
	#FIXME: ver o que raio se passa com o url das bananas
)
