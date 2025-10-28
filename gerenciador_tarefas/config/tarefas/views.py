from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas(request):
    tarefas_salvas = Tarefa.objects.all()
    contexto = {"minhas_tarefas": tarefas_salvas}
    return render(request, 'tarefas/lista.html', contexto)
    
def detalhe_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html')

def alterar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404 (Tarefa, pk = tarefa_id)
    if request.method == 'post':
        tarefa.titulo = request.post.get('titulo')
        tarefa.descricao = request.post.get('descricao')
        tarefa.concluida = request.post.get('concluida') == 'on'
        tarefa.save()
        return redirect ('lista_tarefas')
    return render(request,'tarefa/from_tarefa.html', {'tarefa': tarefa})