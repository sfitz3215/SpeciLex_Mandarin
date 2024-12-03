from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, Http404
from django.db.models import Count
from django.http import JsonResponse
from .models import *
from .utils import *
from .forms import *
import re

TRANSLATOR = TranslatorModel()

# Create your views here.
def input_material(request):
    form = MaterialInput(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        request.session['text'] = text

        return redirect('text_reader')
    return render(request, 'input_text.html', {'form': form})


def text_reader(request):
    full_text = request.session['text']
    text_split = re.findall('.*?[.!\?。？！]|.+$', full_text)

    return render(request, 'text_reader.html', {'text': text_split})


def preprocess_text_view(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        text = data.get("text", "")

        words = TRANSLATOR.split_sentence(text)
        #pronunciation = TRANSLATOR.get_pinyin(text)
        sentence_translation = TRANSLATOR.translate_sentence(text)
        return JsonResponse({
            "words": words,
            #"pronunciation": pronunciation,
            "sentence_translation": sentence_translation
        })
    return JsonResponse({"error": "Invalid request"}, status=400)


def process_word_view(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        word = data.get("word", "")

        pronunciation = TRANSLATOR.get_pinyin(word)
        result = TRANSLATOR.translate_word(word)

        return JsonResponse({"message": result, "pronunciation": pronunciation})
    return JsonResponse({"error": "Invalid request"}, status=400)
