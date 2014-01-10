# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from listagens.models import Listagem, Protocolo

class ListagemTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProtocoloTranslationOptions(TranslationOptions):
	fields = ('entidade', 'financiamento', 'objectivos', 'unidade')


translator.register(Listagem, ListagemTranslationOptions)
translator.register(Protocolo, ProtocoloTranslationOptions)
