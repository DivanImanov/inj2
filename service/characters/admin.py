from django.contrib import admin
from .models import MoveList, CharacterList, OptimalCombos, KeyMoves

# Register your models here.

admin.site.register(MoveList)
admin.site.register(CharacterList)
admin.site.register(OptimalCombos)
admin.site.register(KeyMoves)

