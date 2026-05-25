class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{titulo}' emprestado com sucesso!")
                return
        print("Livro indisponível.")

    def listar_livros(self):
        for livro in self.livros:
            print(livro)