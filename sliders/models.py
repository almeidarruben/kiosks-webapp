# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _

class Slider(Page):
    items = models.ManyToManyField(
        'SliderItem',
        verbose_name=_('Items de Slider'),
        null=False, 
        blank=False)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Slider')


class SliderItem(models.Model):
    titulo = models.CharField(_('Título'),
        max_length=150,
        null=False,
        blank=False)

    subtitulo = models.CharField(_('Subtítulo'),
        max_length=150,
        null=False,
        blank=False)

    detalhes = models.TextField(_('Detalhes'),
        max_length=150,
        null=True,
        blank=True)

    texto = models.TextField(_('Texto'),
        null=False,
        blank=False)

    imagem = models.ImageField(_('Imagem'),
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='slider/imagens')

    PESO_OPTIONS = tuple([('%d' % i, '%d' % i) for i in range(1, 11)])

    peso = models.CharField(_('Peso'),
        max_length=50,
        choices=PESO_OPTIONS,
        null=False,
        blank=False)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        ordering = ['peso']
        verbose_name = _('Item de Slider')
        verbose_name_plural = _('Items de Slider')


admin.site.register(Slider, PageAdmin)
admin.site.register(SliderItem)
