from django.shortcuts import render
from .models import MoveList, CharacterList, OptimalCombos, KeyMoves
from django.views.generic import DetailView
from django.http import Http404
from django.core.cache import cache

from .serializers import MoveListSerializer
from rest_framework import generics
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.filters import SearchFilter


# Create your views here.

# class CharacterDetailView(DetailView):
#     model = CharacterList
#     template_name = 'characters/character.html'
#     context_object_name = 'info'


def index(request):
    characters_cache = cache.get('characters_cache')
    if characters_cache:
        data = characters_cache
    else:
        data = CharacterList.objects.order_by('position')
        cache.set('characters_cache', data, 30)
    return render(request, 'characters/index.html', {'data': data})


def character_page(request, character):
    character_list = CharacterList.objects.order_by('position')
    if character not in [str(x) for x in character_list]:
        raise Http404
    else:
        data = MoveList.objects.filter(character_name = character).order_by('pk')
        combos = OptimalCombos.objects.filter(character_name = character).order_by('pk')
        key_moves = KeyMoves.objects.filter(character_name = character).order_by('pk')
        buttons = ['B', 'F', 'D', 'U', '1', '2', '3', '4', 'R1', 'R2', 'L1', 'L2', 'UF', 'UB', 'DF', 'DB']
        return render(request, 'characters/character.html', {'data': data, 'character': character, 'combos': combos, 'key_moves': key_moves, 'buttons': buttons})
    

class MoveListAPIView(generics.ListAPIView):

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            queryset = MoveList.objects.filter(character_name=name)
        else:
            queryset = MoveList.objects.all()
        return queryset
    
    serializer_class = MoveListSerializer
    # render_classes = [JSONRenderer]
    # parser_classes = [JSONParser]
    # queryset = MoveList.objects.all()
