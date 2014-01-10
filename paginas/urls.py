from django.conf.urls import patterns, url

urlpatterns = patterns('paginas.views',
	url(r'^get/pagina/(?P<pagina>\d+)$', 'get_pagina', name='get_pagina'),
	url(r'^get/categoria/(?P<categoria>\d+)$', 'get_categoria', name='get_categoria'),
	url(r'^get/items_by_categoria/(?P<listagem>\d+)$', 'get_items_by_categoria', name='get_items_by_categoria'),
)
