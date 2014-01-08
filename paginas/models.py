# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from copy import deepcopy
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage
from mezzanine.core.admin import BaseDynamicInlineAdmin, TabularDynamicInlineAdmin


#TODO: adicionar helptext

class Pagina(Page):
    texto = models.TextField(_('Texto'),
        null=False,
        blank=False)

    rodape = models.TextField(_('Rodapé'), 
        max_length=150,
        null=True,
        blank=True)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = _('Página')
        verbose_name_plural = _('Páginas')


class BotoesPopup(models.Model):
    pagina = models.ForeignKey('Pagina',
        verbose_name=_('Botão Popup'),
        null=False,
        blank=False)

    titulo = models.CharField(_('Título'), 
        max_length=100)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name = _('Botão Popup')
        verbose_name_plural = _('Botões Popup')


class BotoesPopupImagem(BotoesPopup):
    imagem = models.ImageField(_('Imagem'), storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='botoes_popup/imagens')


class BotoesPopupVideo(BotoesPopup):
    video = models.FileField(_('Video'), storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='botoes_popup/videos')


class BotoesPopupImagemInline(admin.TabularInline):
    model = BotoesPopupImagem

class BotoesPopupVideoInline(admin.TabularInline):
    model = BotoesPopupVideo


pagina_extra_fieldsets = ((None, {"fields": ("titulo",)}),)

class PaginaAdmin(PageAdmin):
    inlines = (BotoesPopupImagem, BotoesPopupVideo,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + pagina_extra_fieldsets

    class Meta:
        max_num = 1


admin.site.register(Pagina, PageAdmin)
admin.site.register(BotoesPopupImagem)
admin.site.register(BotoesPopupVideo)