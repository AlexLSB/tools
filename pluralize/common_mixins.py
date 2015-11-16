# -*- coding: utf-8 -*-
from django.db import models
from .morph_analyzer import AllInflectingMorphAnalyzer

morph = AllInflectingMorphAnalyzer()


class PluralTitleMixin(models.Model):
    '''
      Если title_plutal не заполнят, вернет обычный title
    '''
    class Meta:
        abstract = True

    title_plural = models.CharField(verbose_name=u"Название в множественном числе", max_length=255, blank=True)

    @property
    def plural_title(self):
        '''
            return plural title
        '''
        if self.title_plural:
            return self.title_plural
        else:
            return morph.pluralize_phrase(self.title)
