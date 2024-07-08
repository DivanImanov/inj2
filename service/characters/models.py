from django.db import models

# Create your models here.

class MoveList(models.Model):
    character_name = models.CharField(max_length=20, blank=True, null=False)
    move_name = models.CharField(max_length=30, blank=True, null=False)
    move_input = models.CharField(max_length=30, blank=True, null=True)
    move_type = models.CharField(max_length=20, blank=True, null=True)
    move_level = models.CharField(max_length=15, blank=True, null=True)
    damage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    block_damage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    start_up = models.SmallIntegerField(blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    recover = models.SmallIntegerField(blank=True, null=True)
    block_adv = models.SmallIntegerField(blank=True, null=True)
    hit_adv = models.SmallIntegerField(blank=True, null=True)
    cancel = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return ' '.join((self.character_name, self.move_name))

    class Meta:
        verbose_name = 'Move'
        verbose_name_plural = 'Move List'


class CharacterList(models.Model):
    position = models.SmallIntegerField(blank=True, null=True, unique=True)
    character_name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    # slug = models.SlugField(max_length=30, unique=True, db_index=True)
    character_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.character_name
    
    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'


class OptimalCombos(models.Model):
    character_name = models.CharField(max_length=20, blank=True, null=False)
    combo_number = models.SmallIntegerField(blank=True, null=True)
    combo_name = models.CharField(max_length=30, blank=True, null=False)
    combo_input = models.TextField(blank=True, null=True)
    combo_bars = models.SmallIntegerField(blank=True, null=True)
    side_switch = models.BooleanField(blank=True, null=True)
    corner = models.BooleanField(blank=True, null=True)
    difficulty = models.SmallIntegerField(blank=True, null=True)
    combo_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return ' '.join((self.character_name, self.combo_name))
    
    class Meta:
        verbose_name = 'Tip'
        verbose_name_plural = 'Tips & Combos'


class KeyMoves(models.Model):
    character_name = models.CharField(max_length=20, blank=True, null=True)
    move_number = models.SmallIntegerField(blank=True, null=True)
    move_name = models.CharField(max_length=30, blank=True, null=True)
    move_input = models.TextField(blank=True, null=True)
    move_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Move'
        verbose_name_plural = 'Key Moves'

