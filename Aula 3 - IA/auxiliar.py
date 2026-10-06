# Listas
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
numeros = [1, 2, 3, 4, 5]

# Pegar uma informação de uma lista
primeiro_nome = nomes[0] # Pega o primeiro elemento da lista (Ana)
print(primeiro_nome) # Mostra o primeiro nome (Ana)

terceiro_numero = numeros[2] # Pega o terceiro elemento da lista (3)
print(terceiro_numero) # Mostra o terceiro número (3)

nomes.append("Eduardo") # Adiciona um novo nome à lista
print(nomes) # Mostra a lista atualizada com o novo nome (['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'])

# Dicionários

# Tem um rotulo e um valor. 

pessoa = {"nome": "Ana", 
          "idade": 25, 
          "cidade": "São Paulo"
          } # Dicionário com informações de uma pessoa
print(pessoa["idade"]) # Mostra a idade da pessoa (Ana)




lista_mensagens = []

mensagem1 = {"role": "user", "content": "Olá, tudo bem?"}
# mensagem1 ={"quem enviou": "user", "conteudo": "Olá, tudo bem?"}
#  
mensagem2 ={"role": "assistant", "content": "Resposta da IA: Olá! Estou bem, obrigado por perguntar."}
# mensagem2 ={"quem enviou": "assistant", "conteudo": "Resposta da IA: Olá! Estou bem, obrigado por perguntar."}

lista_mensagens.append(mensagem1) # Adiciona a primeira mensagem à lista de mensagens
lista_mensagens.append(mensagem2) # Adiciona a segunda mensagem à lista de mensagens

print(lista_mensagens) # Mostra a lista de mensagens com as duas mensagens adicionadas