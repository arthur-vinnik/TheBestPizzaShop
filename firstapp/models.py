from django.db import models

# Create your models here
class PizzaShop(models.Model):
    name = models.CharField(max_length= 30, verbose_name ='Название')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default = 0 ,verbose_name ='Рейтинг')
    url = models.URLField(verbose_name='Интернет сылка на пицерию')

    def __str__(self):
        return self.name

