import json
teste= list()

with open('Curso\Adoção.json','r',encoding='utf-8') as ei:
    teste= json.load(ei)

print(teste)

Nome= input('Digite o nome: ')
Idade= input('Digite a idade: ')
Animal_de_interesse= input('Digite a espécie do pet: ')
Gênero=input('Digite o sexo do animal: ')
Nome_do_Animal= input('Digite o nome do pet: ')

teste.append (dict(Nome= Nome, Idade= Idade, Animal_de_interesse= Animal_de_interesse, Gênero= Gênero, Nome_do_Animal=Nome_do_Animal))

with open('Curso\Adoção.json','w', encoding= 'utf-8') as ei:
    teste= json.dump(teste, ei, ensure_ascii= False, indent= '\t')

print('Já foi constatado.')
    
