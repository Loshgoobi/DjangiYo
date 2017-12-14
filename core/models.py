from django.db import models


class Cards(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    effect = models.CharField(max_length=500)
    type = models.CharField(max_length=20)
    used = None

    CATEGORY = (
        ('M', 'Monster'),
        ('S', 'Spell'),
        ('T', 'Trap'),
    )
    CARD_FACE = (
        ('U', 'Face-Up'),
        ('D', 'Face-Down'),
    )
    CARD_STATE = (
        ('A', 'Attack'),
        ('D', 'Defence'),
    )
    CARD_TYPE = (
        ('Wa', 'Warrior'),
        ('Sp', 'Spellcaster'),
        ('Fa', 'Fairy'),
        ('Fi', 'Fiend'),
        ('Zo', 'Zombie'),
        ('Ma', 'Machine'),
        ('Aq', 'Aqua'),
        ('Py', 'Pyro'),
        ('Ro', 'Rock'),
        ('WB', 'Winged Beast'),
        ('Pl', 'Plant'),
        ('In', 'Insect'),
        ('Th', 'Thunder'),
        ('Dr', 'Dragon'),
        ('Be', 'Beast'),
        ('BW', 'Beast-Warrior'),
        ('Di', 'Dinosaur'),
        ('Fi', 'Fish'),
        ('Se', 'Sea Serpent'),
        ('Ps', 'Psychic'),
        ('DB', 'Divine-Beast'),
        ('CG', 'Creator God'),
        ('Wy', 'Wyrm'),
        ('Cy', 'Cyberse'),


    )
    ATTRIBUTE = (
        ('Ea', 'Earth'),
        ('Wa', 'Water'),
        ('Fi', 'Fire'),
        ('Wi', 'Wind'),
        ('Li', 'Light'),
        ('Da', 'Dark'),
        ('Di', 'Divine'),
    )

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    deck = models.ManyToManyField(Cards)
    #hand = models.ManyToManyField(Cards)

# Create your models here.
