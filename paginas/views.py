# -*- coding: utf-8 -*-
from paginas.models import Pagina
from submenus.models import Submenus
from listagens.models import Listagem, Item, ProjetoServico, ProtocoloPublicacao
from contactos.models import Contacto

from mezzanine.pages.models import Page
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json

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
    css_class = ''
    if Pagina.objects.filter(pk=pagina):
    	pagina_nova = Pagina.objects.get(pk=pagina)
    	css_class = 'page'
    elif Submenus.objects.filter(pk=pagina):
    	pagina_nova = Submenus.objects.get(pk=pagina)
        css_class = 'submenus'
    elif Listagem.objects.filter(pk=pagina):
        pagina_nova = Listagem.objects.get(pk=pagina)
        css_class = 'list'
    elif Contacto.objects.filter(pk=pagina):
        pagina_nova = Contacto.objects.get(pk=pagina)
        css_class = 'contact'

    #TODO: ver os fields necessários para cada um dos casos

    response_data = model_to_dict(pagina_nova)
    for item in ['status', '_order', 'login_required', 'in_sitemap', 'page_ptr', 'short_url', '_meta_title', 'expiry_date', 'publish_date', 'gen_description', 'keywords', 'in_menus']:
        if item in response_data:
            del response_data[item]

    response_data['slug'] = pagina_nova.slug.replace("/", "-")

    if css_class == 'list':
        response_data['items'] = ''
        #FIXME: corrigir o json dos items
        if pagina_nova.tipo == 'proj_serv':
            response_data['items'] = serializers.serialize("json", ProjetoServico.objects.filter(listagem=pagina_nova))
        elif pagina_nova.tipo == 'prot_pub':
            response_data['items'] = to_json(ProtocoloPublicacao.objects.filter(listagem=pagina_nova))
        print response_data['items']

    response_data={'pagina': response_data}
    response_data['class']=css_class
    if css_class == 'submenus':
    	response_data['botoes']={}
    	for botao in pagina_nova.botoes.all():
            response_data['botoes'][botao.pk]=model_to_dict(botao)
            print response_data['botoes'][botao.pk]
            slug_formated = botao.link_para.slug
            slug_formated = slug_formated.replace("/", "-")
            response_data['botoes'][botao.pk]['slug']=slug_formated

    return HttpResponse(json.dumps(response_data), content_type="application/json")
