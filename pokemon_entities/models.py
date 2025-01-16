from django.db import models  # noqa F401


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

