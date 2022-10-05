from django.http import JsonResponse
from django.shortcuts import render, redirect
from pkg_resources import cleanup_resources
from .models import Curso
from django.views.generic import ListView
from django.views import View
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt





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


class CursoApi(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            cursos = list(Curso.objects.filter(id=id).values())
            if len(cursos) > 0:
                curso = cursos[0]
                data = {
                    'message': 'Success', 'curso': curso
                }
                return JsonResponse(data)
            else:
                data = {
                    'message': 'Curso not Found'
                }
                return JsonResponse(data)
        else: 
            cursos = list(Curso.objects.values())
            if len(cursos) > 0:
                data ={
                    'message': 'Success', 'curso': cursos
                }
                return JsonResponse(data)
            else:
                data = {
                    'message': 'Curso not Found'
                }
                return JsonResponse(data)
    

    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        Curso.objects.create(nombre=jd['nombre'], creditos=jd['creditos'])
        data = {
                'message': 'Success'
                }
        return JsonResponse(data)

    
    def put(self, request, id):
        jd = json.loads(request.body)
        cursos = list(Curso.objects.filter(id=id).values())
        if len(cursos) > 0:
            curso = Curso.objects.get(id=id)
            curso.nombre = jd['nombre']
            curso.creditos = jd['creditos']
            curso.docente_id = jd['docente_id']
            curso.save()
            data = {
                'message': 'Success'
                }
        else: 
            data = {
                    'message': 'Curso not Found'
                }
        return JsonResponse(data)


    def delete(self, request, id):
        curso = list(Curso.objects.filter(id=id).values())
        if len(curso) > 0:
            Curso.objects.filter(id=id).delete()
            data = {
                'message': 'Success'
                }
        else: 
            data = {
                    'message': 'Curso not Found'
                }
        return JsonResponse(data)
    


