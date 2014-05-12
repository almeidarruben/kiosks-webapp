# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.pages.models import Page
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
#TODO: from mezzanine.core.fields import RichTextField


class Listagem(Page):
    TIPO_CHOICES = (('proj_serv', 'Projetos / Serviços'),
                    ('prot_pub', 'Protocolos / Publicações'))
    tipo = models.CharField('Tipo',
        max_length=50,
        choices=TIPO_CHOICES,
        null=False,
        blank=False)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Listagem'
        verbose_name_plural = 'Listagens'


class Categoria(models.Model):
    nome = models.CharField('Categoria',
        max_length=150)

    def __unicode__(self):
        return "%s" % self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Item(models.Model):
    listagem = models.ForeignKey('Listagem')

    titulo = models.CharField('Título',
        max_length=150)

    unidade = models.CharField('Unidade',
        max_length=150,
        null = True,
        blank = True)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        abstract = True


class ProjetoServico(Item):
    categoria = models.ForeignKey('Categoria',
        null=True,
        blank=True)

    candidatura = models.DateField('Candidatura',
        null = True,
        blank = True)

    financiamento = models.CharField('Financiamento',
        max_length=150,
        null = True,
        blank = True)

    responsavel = models.CharField('Responsável',
        max_length=150,
        null = True,
        blank = True)

    class Meta:
        verbose_name = 'Projeto / Serviço'
        verbose_name_plural = 'Projetos / Serviços'


class ProtocoloPublicacao(Item):
    objectivos = models.TextField('Objetivos',
        null = True,
        blank = True)
    
    assinatura = models.DateField('Assinatura',
        null = True,
        blank = True)

    termo = models.DateField('Termo',
        null = True,
        blank = True)

    class Meta:
        verbose_name = 'Protocolo / Publicação'
        verbose_name_plural = 'Protocolos / Publicações'


admin.site.register(Listagem, PageAdmin)
admin.site.register(Categoria)
admin.site.register(ProjetoServico)
admin.site.register(ProtocoloPublicacao)
