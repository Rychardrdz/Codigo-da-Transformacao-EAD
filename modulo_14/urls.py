from django.urls import path

from . import views


urlpatterns = [

    path("", views.lista_produtos, name="lista"),

    path("cadastrar/", views.cadastrar_produto, name="cadastrar"),

    path("atualizar/<int:id>/", views.atualizar_produto, name="atualizar"),

    path("excluir/<int:id>/", views.excluir_produto, name="excluir"),
]