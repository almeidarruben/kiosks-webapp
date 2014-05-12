# -*- coding: utf-8 -*-
from paginas.models import Pagina
from submenus.models import Submenus
from listagens.models import Listagem, ProjetoServico, ProtocoloPublicacao, Categoria
from contactos.models import Contacto
from sliders.models import Slider, SliderItem
from listagens_bottom.models import ListagemBottom, ItemBottom

from mezzanine.pages.models import Page
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
import json
from itertools import groupby

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
    elif Slider.objects.filter(pk=pagina):
        pagina_nova = Slider.objects.get(pk=pagina)
        css_class = 'slider'

    response_data = model_to_dict(pagina_nova)
    for item in ['status',
                 '_order',
                 'login_required',
                 'in_sitemap',
                 'page_ptr',
                 'short_url',
                 '_meta_title',
                 'expiry_date',
                 'publish_date',
                 'gen_description',
                 'keywords',
                 'in_menus']:
        if item in response_data:
            del response_data[item]

    response_data['slug'] = pagina_nova.slug.replace("/", "-")

    response_data={'pagina': response_data}
    response_data['class']=css_class

    if css_class == 'page':
        response_data['pagina']['imagem'] = \
                '%s' % response_data['pagina']['imagem']
        if pagina_nova.botoes_popup:
            response_data['pagina']['botoes_popup'] = {}
            for botao in pagina_nova.botoes_popup.all():
                response_data['pagina']['botoes_popup'][botao.pk] = model_to_dict(botao)
                response_data['pagina']['botoes_popup'][botao.pk]['ficheiro'] = \
                        '%s' % response_data['pagina']['botoes_popup'][botao.pk]['ficheiro']

    elif css_class == 'submenus':
    	response_data['botoes']={}
    	for botao in pagina_nova.botoes.all():
            response_data['botoes'][botao.pk]=model_to_dict(botao)
            slug_formated = botao.link_para.slug
            slug_formated = slug_formated.replace("/", "-")
            response_data['botoes'][botao.pk]['slug']=slug_formated

    elif css_class == 'contact':
        response_data['pagina']['mapa'] = \
                '%s' % response_data['pagina']['mapa']

    elif css_class == 'slider':
        response_data['items']={}
        for item in pagina_nova.items.all():
            response_data['items'][item.pk]=model_to_dict(item)
            response_data['items'][item.pk]['imagem'] = \
                        '%s' % response_data['items'][item.pk]['imagem']

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_categoria(request, categoria):
    cat = get_object_or_404(Categoria, pk=categoria)
    response_data = model_to_dict(cat)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_items(request, listagem):
    items = '', 
    response_data = {}
    if ProjetoServico.objects.filter(listagem=listagem):
        items = ProjetoServico.objects.filter(listagem=listagem).order_by('categoria')
        item_group = list(items)
        for key, group in groupby(item_group, lambda item: item.categoria):
            response_data['%s'%key] = {}
            for item in group:
                response_data['%s'%key][item.pk] = model_to_dict(item)
                response_data['%s'%key][item.pk]['candidatura'] = \
                        '%s' % response_data['%s'%key][item.pk]['candidatura']

    elif ProtocoloPublicacao.objects.filter(listagem=listagem):
        items = ProtocoloPublicacao.objects.filter(listagem=listagem)
        for item in items:
            response_data[item.pk] = model_to_dict(item)
            response_data[item.pk]['assinatura'] = \
                        '%s' % response_data[item.pk]['assinatura']
            response_data[item.pk]['termo'] = \
                        '%s' % response_data[item.pk]['termo']

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_sliders(request):
    items = SliderItem.objects.filter(slider__slug="/")

    response_data = {}
    for item in items:
        response_data[item.pk] = model_to_dict(item)
        response_data[item.pk]['imagem'] = \
            "%s" % response_data[item.pk]['imagem']

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_bottoms(request):
    listagens = ListagemBottom.objects.all().order_by('peso')

    response_data = {}
    response_data['tamanho'] = 3
    response_data['bottoms'] = {}

    if len(listagens) <= 3:
        response_data['tamanho'] = len(listagens)
        for listagem in listagens:
            response_data['bottoms']["%s"%listagem.titulo] = {'peso': listagem.peso}
            items = ItemBottom.objects.filter(listagem=listagem)
            for item in items:
                response_data['bottoms']["%s"%listagem.titulo][item.pk] = model_to_dict(item)
                response_data['bottoms']["%s"%listagem.titulo][item.pk]['data'] = \
                        '%s' % response_data["%s"%listagem.titulo][item.pk]['data']
                print response_data['bottoms']["%s"%listagem.titulo][item.pk]['data']
    else:
        i = 0
        for listagem in listagens:
            if i == 3:
                break
            response_data['bottoms']["%s"%listagem.titulo] = {'peso': listagem.peso}
            items = ItemBottom.objects.filter(listagem=listagem)
            for item in items:
                response_data['bottoms']["%s"%listagem.titulo][item.pk] = model_to_dict(item)
                response_data['bottoms']["%s"%listagem.titulo][item.pk]['data'] = \
                        '%s' % response_data['bottoms']["%s"%listagem.titulo][item.pk]['data']
                print response_data['bottoms']["%s"%listagem.titulo][item.pk]['data']
            i+=1
    print response_data

    return HttpResponse(json.dumps(response_data), content_type="application/json")
