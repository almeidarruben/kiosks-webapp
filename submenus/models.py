# -*- coding: utf-8 -*-

from django.db import models
from mezzanine.pages.models import Page
from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class Submenus(Page):
    botoes = models.ManyToManyField(
        'Botoes',
        verbose_name=_('Botões'),
        null=False, 
        blank=False)

    class Meta:
        verbose_name = _('Submenu')
        verbose_name_plural = _('Submenus')


class Botoes(models.Model):
    titulo = models.CharField(_('Título'), 
        max_length=100)

    descricao = models.TextField(_('Descrição'), 
        max_length=300,
        null=True,
        blank=True)

    link_para = models.ForeignKey('pages.Page')

    #TODO: adicionar campo de peso unique_togueter com o titulo para ordenar os botões

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name = _('Botão')
        verbose_name_plural = _('Botões')


admin.site.register(Submenus, PageAdmin)
admin.site.register(Botoes)