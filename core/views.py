from django.shortcuts import render, redirect
from .models import Pessoa
# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    vnome = request.POST.get('nome')
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})


def update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.save()
    return redirect("/core")

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect("/core")