from dataclasses import dataclass
from copy import deepcopy
import pilhaProva as PEA

#a seguir, variáveis de controle do status de operação
ArvoreVazia = 1
ArvoreCheia = 2
ItemExistente = 3
ItemInexistente = 4
ItemInserido = 5
ItemRemovido = 6
ItemAtualizado = 7

  
@dataclass
class tipoItem:
    """
    Representa um item da árvore.
    """
    nome: str = "Inexistente"
    CPF: str = "000.000.000-00"
    idade: int = 0

@dataclass
class _tipoNo:
    item = tipoItem()
    esquerda: '_tipoNo' = None
    direita: '_tipoNo' = None
    bal: int = 0
    """
    Os atributos/campos Esquerda e Direita servem para apontar/referenciar as 
    subárvoresda esquerda e da direita, respectivamente, ou seja, os nós raizes
    dessas subárvores, que são nós filhos. São iniciados com None para indicar
    que inicialmente não referenciam nenhum outro nó.
    """

class arvoreAVLRecursiva():
    """
    Implementa uma Árvore Binária de Busca Recursiva dinâmica e encadeada.
    """

    def __init__(self):
        """
        Construtor de inicialização: cria uma árvore vazia.
        """
        self._numItens: int = 0
        self._raiz: _tipoNo = None
        self._opSt: int = ArvoreVazia #status inicial
        self._cresceu: bool = False
        self._diminuiu: bool = False
        self._item: tipoItem()
        

    def vazia(self) -> bool:
        """
        Método que retorna True se a árvore esta vazia, caso contrário False.
        """
        return self._raiz==None #ou self._numItens==0

    def cheia(self) -> bool:
        """
        Retorna True se a árvore esta cheia, caso contrário False.
        """
        return False

    def opStatus(self) -> int:
        """
        Retorna o status da ultima operação que registra o status: insere,
        remove, consulta, atualiza e mostra. Os possiveis status são:
        ArvoreVazia
        ArvoreCheia
        ItemExistente
        ItemInexistente
        ItemInserido
        ItemRemovido
        ItemAtualizado
        """
        return self._opSt

    def totalItens(self) -> int:
        """
        Retorna o numero de itens da árvore.
        """
        return self._numItens

    def _balanceiaDirIns(self, raiz: _tipoNo) -> _tipoNo:
        """
        """

    def _balanceiaEsqIns(self, raiz: _tipoNo) -> _tipoNo:
        """ 
        """

        
    def _insereAVL2(self, raiz: _tipoNo, item: tipoItem) -> _tipoNo:
        """ 
        """        
        
    def insereAVL(self, item: tipoItem) -> None:
        """ 
        """

    def _balanceiaDirRem(self, raiz: _tipoNo) -> _tipoNo:
        """ 
        """       

    def _balanceiaEsqRem(self, raiz: _tipoNo) -> _tipoNo:
        """ 
        """
    
    def _menorDosMaioresAVL(self, raiz: _tipoNo) -> _tipoNo:
        """
        """

    def _maiorDosMenoresAVL(self, raiz: _tipoNo) -> _tipoNo:
        """
        """
        
    def _removeAVL2(self, raiz: _tipoNo, nome: str) -> _tipoNo:
        """
        """                          
        
    def removeAVL(self, nome: str) -> tipoItem:
        """
        """                 
        
    def _mostraEmOrdem2(self, raiz: _tipoNo) -> None:
        if raiz is not None:
            self._mostraEmOrdem2(raiz.esquerda)
            print(raiz.item.nome, end=' ')
            self._mostraEmOrdem2(raiz.direita)

    def mostraEmOrdem(self) -> None:
        """
        Mostra no vídeo todos os elementos da árvore no caminhamento em-ordem.
        """

        if self.vazia():
            print('Árvore vazia')
        else:
            print('\nElementos da Árvore em ordem: ')
            self._mostraEmOrdem2(self._raiz)
            print()
            
        
if __name__ == "__main__":

    print("\nTestador de TAD Arvore Binaria de Busca AVL Recursiva\n")
    arv=arvoreAVLRecursiva()
    arv.mostraEmOrdem()
    
    item=tipoItem("RON","178.763.238-55",58)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("ANA","145.583.148-77",50)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("BEN","049.343.648-23",25)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("BER","456.432.863-90",35)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("XER","451.761.098-32",30)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("AAR","023.453.984-89",48)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("BEA","189.982.345-10",38)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()
    
    item=tipoItem("CAR","786.340.671-39",22)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("SER","340.456.671-93",29)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("PAU","544.999.761-00",32)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("DAN","111.222.347-78",42)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("CAI","339.983.456-13",19)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("XIN","538.720.912-44",31)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("BAR","123.432.455-66",80)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("BEP","338.320.312-34",12)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    arv.mostraEmOrdem()

    item=tipoItem("XES","518.721.911-41",1)
    print("\nInserindo: ", item.nome)
    arv.insereAVL(item)
    
    arv.mostraEmOrdem()

    print("\nRemovendo: ", end="")
    item: tipoItem=arv.removeAVL("SER")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("BER")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("RON")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("ANA")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("PAU")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("BEN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("CAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("CAI")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("DAN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("AAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("XER")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("BEA")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("BEP")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("XIN")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("BAR")
    print(item.nome)
    arv.mostraEmOrdem()

    print("\nRemovendo: " , end="")
    item: tipoItem=arv.removeAVL("XES")
    print(item.nome)
    arv.mostraEmOrdem()
