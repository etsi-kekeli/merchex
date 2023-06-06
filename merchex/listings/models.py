from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

def get_current_year():
    return date.today().year

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        AFRO_BEAT = 'AB'
        RNB = 'RNB'

    name = models.fields.CharField(max_length=100)
    genre = models.CharField(max_length=5, choices=Genre.choices, default=Genre.RNB)
    biography = models.CharField(max_length=1000, null=True)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(get_current_year)],
        default=get_current_year
                    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    # like_new = models.fields.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'

    
class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHES = 'CLO'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MISC'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='')
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True, validators=[MaxValueValidator(get_current_year)])
    type = models.CharField(max_length=5, choices=Type.choices, default=Type.MISCELLANEOUS)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    