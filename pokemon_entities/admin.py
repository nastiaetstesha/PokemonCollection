from django.contrib import admin
from django import forms
from .models import Pokemon, PokemonEntity


class PokemonEntityForm(forms.ModelForm):
    class Meta:
        model = PokemonEntity
        fields = '__all__'
        widgets = {
            'appeared_at': forms.SplitDateTimeWidget(
                date_attrs={'type': 'date', 'placeholder': 'Date'},
                time_attrs={'type': 'time', 'placeholder': 'Time'},
            ),
            'disappeared_at': forms.SplitDateTimeWidget(
                date_attrs={'type': 'date', 'placeholder': 'Date'},
                time_attrs={'type': 'time', 'placeholder': 'Time'},
            ),
        }


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    form = PokemonEntityForm
    list_display = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at')
    list_filter = ('pokemon', 'appeared_at', 'disappeared_at')
