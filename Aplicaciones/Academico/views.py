from django.shortcuts import render, redirect
from .models import Curso
from django.views.generic import ListView


# Create your views here.

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'index.html', {'cursos': cursos})
    
class CursoListView(ListView):
    model = Curso
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Cursos'
        return context

def registrar_curso(request):
    nombre = request.POST['txtCurso']
    creditos = request.POST['numCreditos']
    curso= Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')

    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')

def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo' : 'Edición de Curso',
        'curso' : curso
    } 
    return render(request, 'edit.html', data)

def actualizar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtCurso']
    creditos = request.POST['numCreditos']

    curso= Curso.objects.get(id=id)
    curso.nombre=nombre
    curso.creditos=creditos
    curso.save()
    return redirect('/')

def contacto(request):
    return render(request, 'contacto.html')