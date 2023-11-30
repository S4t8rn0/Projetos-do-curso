class Notas:
    def __init__ (self, A):
        self.alun= A 
        self.alun_met=0
        return A

    def notas(self, n1, n2, n3):
        fin= n1+ n2+ n3/ 3
        self.alun_met= fin

    def Média(self, alvo):
        alvo= self.alun_met
        if alvo>= 6:
            print(f'O aluno {self.alun} está aprovado.')
        else:
            print(f'O aluno {self.alun} está em recuperação')

    print('Qual é o nome do aluno?')
    A= input()

    aluno= notas()
    aluno.notas(int(input('Digite a nota de Matemática: ')), int(input('Insira a nota Física: ')), int(input('Insira a nota de Química: ')))