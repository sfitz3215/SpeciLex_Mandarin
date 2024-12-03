from transformers import MarianMTModel, MarianTokenizer
import nltk
from pypinyin import pinyin, Style
import jieba
import numpy as np
import torch


class TranslatorModel:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-zh-en"):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate_sentence(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        translated = self.model.generate(**inputs)
        translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text

    def split_sentence(self, sentence):
        words = list(jieba.cut(sentence))
        return words

    def translate_word(self, word_to_translate):
        inputs = self.tokenizer(word_to_translate, return_tensors="pt", padding=True, truncation=True)

        translated = self.model.generate(**inputs)

        translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)

        return translated_text

    def get_pinyin(self, characters):
        return pinyin(characters, style=Style.TONE)
