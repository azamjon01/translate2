from dataclasses import field, fields
from modeltranslation.translator import register, TranslationOptions
from .models import TranslatePage

@register(TranslatePage)
class MalumotTranslationOptions(TranslationOptions):
    fields = ('name', 'title', )