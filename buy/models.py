from django.db import models

from .validators import checking_positive_numbers


class Item(models.Model):
    """Модель Item"""
    name = models.CharField(max_length=100,
                            verbose_name='Наименование Item')
    description = models.CharField(blank=True,
                                   max_length=300,
                                   verbose_name='Описание Item')
    price = models.IntegerField(validators=[checking_positive_numbers],
                                default=0,
                                verbose_name='Стоимость Item')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.0f}".format(self.price / 100)

    def get_display_description(self):
        return f"{self.description}"
