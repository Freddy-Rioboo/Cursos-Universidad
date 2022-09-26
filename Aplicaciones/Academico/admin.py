from django.contrib import admin
from .models import Curso, Docente

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos',)
    list_display_links = ('nombre',)
    
    def datos(self, obj):
        return obj.nombre.upper()
    
    datos.short_description = "Cursos"
    datos.admin_order_field = 'nombre'

admin.site.register(Docente)

