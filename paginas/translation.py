# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from paginas.models import Pagina, BotoesPopup


class PaginaTranslationOptions(TranslationOptions):
    fields = ('title', 'texto', 'rodape',)


class BotoesPopupTranslationOptions(TranslationOptions):
	fields = ('titulo',)


translator.register(Pagina, PaginaTranslationOptions)
translator.register(BotoesPopup, BotoesPopupTranslationOptions)
