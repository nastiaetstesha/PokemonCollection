from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):

    title = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(
        upload_to='pokemon_images/',
        null=True,
        blank=True,
        verbose_name="Изображение"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name="Покемон"
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        default=now,
        verbose_name="Время появления"
    )
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        default=now,
        verbose_name="Время исчезновения"
    )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Уровень"
    )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Здоровье"
    )
    attack = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Атака"
    )
    defense = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Защита"
    )
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Выносливость"
    )

    def __str__(self):
        return f"{self.pokemon.title} ({self.lat}, {self.lon})"
