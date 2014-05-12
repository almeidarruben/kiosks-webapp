from modeltranslation.translator import translator, TranslationOptions
from submenus.models import Botoes

class BotoesTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descricao',)

translator.register(Botoes, BotoesTranslationOptions)
