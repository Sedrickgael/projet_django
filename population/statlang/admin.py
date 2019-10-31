from django.contrib import admin
from .models import Population

@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    '''Admin View for Population'''

    list_display = ('nom','nb_hbts', 'pourcentage')
    