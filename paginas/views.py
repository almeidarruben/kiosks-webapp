# -*- coding: utf-8 -*-
from paginas.models import Pagina
from submenus.models import Submenus
from mezzanine.pages.models import Page
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.utils import simplejson

def to_json(queryset, fields = None):
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    if fields:
        json_serializer.serialize(queryset, fields=fields)
    else:
        json_serializer.serialize(queryset)
    return json_serializer.getvalue()


def get_pagina(request, pagina):
    pagina_nova = get_object_or_404(Page, pk=pagina)
    if Pagina.objects.filter(pk=pagina):
    	pagina_nova = Pagina.objects.get(pk=pagina)
    	print "é página"
    elif Submenus.objects.filter(pk=pagina):
    	pagina_nova = Submenus.objects.get(pk=pagina)
    	print "é submenu"
    print "pagina: ", pagina_nova

    #TODO: ver os fields necessários para cada um dos casos

    response_data = model_to_dict(pagina_nova)
    for item in ['status', '_order', 'login_required', 'in_sitemap', 'page_ptr', 'short_url', '_meta_title', 'expiry_date', 'publish_date', 'gen_description', 'keywords']:
        del response_data[item]

    response_data={'pagina': response_data}
    if Submenus.objects.filter(pk=pagina):
    	response_data['botoes']={}
    	for botao in pagina_nova.botoes.all():
    		response_data['botoes'][botao.pk]=model_to_dict(botao)

    return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
