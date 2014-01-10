# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.pages.models import Page
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from django.utils.translation import ugettext_lazy as _


class Contacto(Page):
    endereco = models.TextField(_('Endereço'),
        null = True,
        blank = True)

    email = models.EmailField(_('Email'),
        null = True,
        blank = True)

    telefone = models.CharField(_('Telefone'),
        max_length=100,
        null = True,
        blank = True)

    fax = models.CharField(_('Fax'),
        max_length=100,
        null = True,
        blank = True)

    website = models.TextField(_('Website'),
        null = True,
        blank = True)

    def __unicode__(self):
        return "%s" % self.entidade

    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')

admin.site.register(Contacto, PageAdmin)
