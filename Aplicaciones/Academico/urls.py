from django.urls import path
from Aplicaciones.Academico.views import CursoListView
from .views  import *


urlpatterns = [
    path('', CursoListView.as_view(), name= 'gestion_cursos'),
    path('registrarcurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('actualizarCurso/', actualizar_curso),
    path('contacto', contacto),
    path('cursos/', CursoApi.as_view(), name= 'api_cursos'),
    path('cursos/<int:id>', CursoApi.as_view(), name= 'api_curso'),
]  
