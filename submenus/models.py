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

    PESO_OPTIONS = tuple([('%d' % i, '%d' % i) for i in range(1, 51)])

    peso = models.CharField(_('Peso'),
        max_length=50,
        choices=PESO_OPTIONS,
        null=False,
        blank=False)

    link_para = models.ForeignKey('pages.Page')

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        ordering = ['peso']
        verbose_name = _('Botão')
        verbose_name_plural = _('Botões')


admin.site.register(Submenus, PageAdmin)
admin.site.register(Botoes)