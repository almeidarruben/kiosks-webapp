# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.pages.models import Page
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from django.utils.translation import ugettext_lazy as _


class Listagem(Page):
    class Meta:
        verbose_name = _('Listagem')
        verbose_name_plural = _('Listagens')


class Protocolo(models.Model):
    listagem = models.ForeignKey('Listagem')

    entidade = models.CharField(_('Entidade'),
        max_length=150)

    financiamento = models.CharField(_('Entidade'),
        max_length=150,
        null = True,
        blank = True)

    objectivos = models.TextField(_('Objetivos'),
        null = True,
        blank = True)

    candidatura = models.DateField(_('Candidatura'),
        null = True,
        blank = True)

    assinatura = models.DateField(_('Assinatura'),
        null = True,
        blank = True)

    termo = models.DateField(_('Termo'),
        null = True,
        blank = True)

    unidade = models.CharField(_('Unidade'),
        max_length=150,
        null = True,
        blank = True)

    #TODO: link -> ver o que é isto na aplicação flash

    def __unicode__(self):
        return "%s" % self.entidade

    class Meta:
        verbose_name = _('Protocolo')
        verbose_name_plural = _('Protocolos')

admin.site.register(Listagem, PageAdmin)
admin.site.register(Protocolo)
