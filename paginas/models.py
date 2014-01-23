# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage

class Pagina(Page):
    texto = models.TextField(_('Texto'),
        null=False,
        blank=False)

    rodape = models.TextField(_('Rodapé'), 
        max_length=150,
        null=True,
        blank=True)

    imagem = models.ImageField(_('Imagem'),
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='paginas/imagens')

    botoes_popup = models.ManyToManyField('BotoesPopup',
        verbose_name=_('Botões Popup'),
        null=True,
        blank=True)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('Página')
        verbose_name_plural = _('Páginas')


class BotoesPopup(models.Model):
    titulo = models.CharField(_('Título'), 
        max_length=100)

    ficheiro = models.FileField(_('Ficheiro'),
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='botoes_popup')

    TIPO_CHOICES = (('imagem', 'Imagem'),
                    ('video', 'Vídeo'))

    tipo = models.CharField('Tipo',
        max_length=10,
        choices=TIPO_CHOICES,
        null=False,
        blank=False)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name = _('Botão Popup')
        verbose_name_plural = _('Botões Popup')


admin.site.register(Pagina, PageAdmin)
admin.site.register(BotoesPopup)