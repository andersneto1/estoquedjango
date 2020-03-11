from django.contrib import admin
from .models import Estoque, EstoqueItens


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nf','funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = ('created')

