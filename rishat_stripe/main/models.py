from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        default=0
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_price_in_dollars(self):
        return "{0:.2f}".format(self.price / 100)
