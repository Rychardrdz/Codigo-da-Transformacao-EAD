from django.shortcuts import render, redirect, get_object_or_404

from .models import Produto

from django.core.paginator import Paginator


def lista_produtos(request):

    busca = request.GET.get("busca")

    produtos = Produto.objects.all()

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    paginador = Paginator(produtos, 5)

    page = request.GET.get("page")

    produtos = paginador.get_page(page)

    return render(request, "lista.html", {
        "produtos": produtos
    })


def cadastrar_produto(request):

    if request.method == "POST":

        Produto.objects.create(
            nome=request.POST["nome"],
            descricao=request.POST["descricao"],
            preco=request.POST["preco"],
            quantidade=request.POST["quantidade"]
        )

        return redirect("lista")

    return render(request, "cadastrar.html")


def atualizar_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":

        produto.nome = request.POST["nome"]

        produto.descricao = request.POST["descricao"]

        produto.preco = request.POST["preco"]

        produto.quantidade = request.POST["quantidade"]

        produto.save()

        return redirect("lista")

    return render(request, "atualizar.html", {
        "produto": produto
    })


def excluir_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    produto.delete()

    return redirect("lista")