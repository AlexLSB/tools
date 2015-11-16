# -*- coding: utf-8 -*-
from pymorphy2 import MorphAnalyzer
from pymorphy2.shapes import restore_capitalization


class AllInflectingMorphAnalyzer(MorphAnalyzer):
    '''
        pymorphy, склоняющий целые фразы, сохраняя большие буквы
    '''

    def pluralize_phrase(self, phrase):
        '''
            перевод фразы в мн.ч (например 'нижний рычаг' > 'нижние рычаги')
        '''
        return self.inflect_all(phrase, {'plur'})

    def inflect_all(self, text, required_grammemes):
        '''
            функция, склоняющая целые фразы, сохраняя большие буквы
        '''
        words = text.split()
        inflected = []
        for word in words:
            try:
                parsed_word = self.parse(word)[0]  # Разберем слово
                if 'nomn' in str(parsed_word.tag):  # Если именительный падеж, то переводим в мн.ч
                    inflected.append(restore_capitalization(
                        parsed_word.inflect(required_grammemes).word,
                        word))
                else:   # Если не именительный падеж то не меняем слово
                    inflected.append(word)
            except:
                inflected.append(word)
        return " ".join(inflected)


morph = AllInflectingMorphAnalyzer()


def pluralize_phrase(phrase):
    '''
        перевод фразы в мн.ч (например 'нижний рычаг' > 'нижние рычаги')
    '''
    return morph.pluralize_phrase(phrase)
