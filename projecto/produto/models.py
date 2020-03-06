from django.db import models

# Create your models here.

class Produto(models.Model):
    importado = models.BooleanField(default=True)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço',max_digits=7, decimal_places=2)
    estoque = models.PositiveIntegerField('estoque actual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    
    class Meta:
        ordering=('produto',)
        
    def __str__(self):
        return self.produto
    
    
    