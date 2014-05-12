from django.conf.urls import patterns, url

urlpatterns = patterns('paginas.views',
	url(r'^get/pagina/(?P<pagina>\d+)$', 'get_pagina', name='get_pagina'),
	url(r'^get/categoria/(?P<categoria>\d+)$', 'get_categoria', name='get_categoria'),
	url(r'^get/categorias/(?P<listagem>\d+)$', 'get_categorias', name='get_categorias'),
	url(r'^get/unidades/(?P<listagem>\d+)$', 'get_unidades', name='get_unidades'),
	url(r'^get/items/(?P<listagem>\d+)$', 'get_items', name='get_items'),
	url(r'^get/sliders', 'get_sliders', name='get_sliders'),
	url(r'^get/bottoms', 'get_bottoms', name='get_bottoms'),
)
