# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class ListagemBottom(models.Model):

    titulo = models.CharField('Titulo',
        max_length=50,
        null=False,
        blank=False)

    PESO_OPTIONS = tuple([('%d' % i, '%d' % i) for i in range(1, 4)])

    peso = models.CharField('Peso',
        max_length=50,
        choices=PESO_OPTIONS,
        null=False,
        blank=False)

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Listagem Bottom'
        verbose_name_plural = 'Listagens Bottom'


class ItemBottom(models.Model):
    listagem = models.ForeignKey('ListagemBottom')

    titulo = models.CharField('Título',
        max_length=150)

    data = models.DateField('Data',
        null = True,
        blank = True)

    descricao = models.TextField('Descrição',
        null = True,
        blank = True)

    def __unicode__(self):
        return "%s" % self.titulo

    class Meta:
        verbose_name = 'Item de Listagem Bottom'
        verbose_name_plural = 'Items de Listagem Bottom'


admin.site.register(ListagemBottom)
admin.site.register(ItemBottom)
