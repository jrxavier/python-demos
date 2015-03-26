__author__ = 'zerix'


print("Hello there")

#Entrada de dados para Phyton 3.x
# value = input('Entre com uma letra: ')

# print(value)



#Identidade de objetos

nome = 'Jose Ricardo'
print ( id(nome))
print (type(nome))

#Mutabilidade dos objetos

# 1 Objetos Imutaveis

idade = 45
print ("ID do Objeto Inteiro (Idade): " + str(id (idade)))
idade = idade + 1
print ("ID do Objeto Inteiro (Idade): " + str(id (idade)))

# 2 Objetos Mutaveis

nomes = []
print ("ID do Objeto Nomes (Lista): " + str (id (nomes)))
nomes.append("Jose")
print ("ID do Objeto Nomes (Lista): " + str (id (nomes)))


