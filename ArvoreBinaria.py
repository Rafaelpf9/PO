class Noh:
    dado,esquerdo,direito = 0,None,None
    def __init__(self, dado):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
    def __str__(self):
        return "{",str(dado),"}"
 
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    def criaNoh(self, dado):
        return Noh(dado)
    def insere(self, raiz, dado):
        #insere elemento em arvore binária
        if raiz == None:
            return self.criaNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz
         
    def pesquisa(self, raiz, valor):
        #realiza pesquisa em arvore binária
        if raiz == None:
            return 0
        else:
            if valor == raiz.dado:
                return 1
            else:
                if valor < raiz.dado:
                    return self.pesquisa(raiz.esquerdo, valor)
                else:
                    return self.pesquisa(raiz.direito, valor)
    def PreOrdem(self, raiz):
        if raiz == None:
            pass
        else:
            print(raiz.dado,end=",")
            self.PreOrdem(raiz.esquerdo)
            self.PreOrdem(raiz.direito)
    def PosOrdem(self, raiz):
        if raiz == None:
            pass
        else:
            self.PreOrdem(raiz.esquerdo)
            self.PreOrdem(raiz.direito)
            print(raiz.dado, end=",")
    def EmOrdem(self,raiz):
        if raiz == None:
            pass
        else:
            self.EmOrdem(raiz.esquerdo)
            print(raiz.dado, end=",")
            self.EmOrdem(raiz.direito)
    def deleteArvore(self,raiz):
        if raiz == None:
            pass
        else:
            self.deleteArvore(raiz.esquerdo)
            self.deleteArvore(raiz.direito)
            del raiz
valorRaiz = int(input("Digite o valor raiz da arvore "))

ArvoreBin = ArvoreBinaria()

raiz = ArvoreBin.criaNoh(valorRaiz)
while True:
    print("Menu")
    print("<1> Inserir ")
    print("<2> Imprimir")
    print("<3> Pesquisar")
    print("<4> Sair")
    opcao = input("\nDigite a sua escolha e pressione ENTER ")
    if opcao == "4":
        break
    elif opcao == "1":
        dado = int(input("Digite o valor a ser inserido: "))
        ArvoreBin.insere(raiz, dado)
    elif opcao == "2":
        print("Pre-Ordem: ", end="")
        ArvoreBin.PreOrdem(raiz)
        print("\nEm Ordem: ", end="")
        ArvoreBin.EmOrdem(raiz)
        print("\nPos-Ordem: ", end="")
        ArvoreBin.PosOrdem(raiz)
        print("\n")
    elif opcao =="3":
        dado = int(input("\nDigite um valor para encontrar:  "))
        if ArvoreBin.pesquisa(raiz, dado):
            print("Valor encontrado")
        else:
            print("Valor nao encontrado")
        input("\nPressione ENTER para continuar ")

#remove nos da arvore
ArvoreBin.deleteArvore(raiz)
print("\nTodos os nos removidos")
