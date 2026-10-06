# Passos

import streamlit as st
from openai import OpenAI # Importar a biblioteca openai (from...) para trabalhar com o chatbot de IA
import openai # Importar a biblioteca openai para trabalhar com o chatbot de IA
import time # Importar a biblioteca time para trabalhar com o chatbot de IA

modelo_ia = OpenAI(
    api_key="", 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    max_retries=3) # Criar modelo de IA (OpenAI) para trabalhar com o chatbot de IA. Passa a chave de acesso para o chatbot de IA e a url da API do chatbot de IA (gemini) e o número máximo de tentativas de conexão com o chatbot de IA (3)

# Título

st.write("# ChatBot IA") # Titulo. Quando tiver # o # no inicio, ele entende que é um titulo

# session_state = Memoria para armazenar as mensagens do chat
if not "lista_mensagens" in st.session_state: # Se não existir a lista de mensagens na sessão, cria uma lista vazia
    st.session_state["lista_mensagens"] = [] # Cria uma lista vazia para armazenar as mensagens do chat

# Campo de mensagens (input)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui") # Campo de mensagens (input)

# Quando o usuario enviar uma mensagem:

# print(mensagem_usuario) # Mostrar a mensagem na tela

for mensagem in st.session_state["lista_mensagens"]: # Para cada mensagem na lista de mensagens
    quem_enviou = mensagem["role"] # Pega quem enviou a mensagem (user -> usuario | assistant -> IA)
    texto_mensagem = mensagem["content"] # Pega o conteúdo da mensagem
    # exibir_mensagem
    st.chat_message(quem_enviou).write(texto_mensagem) # Mostrar a mensagem na tela. 'Quem esta mandando' (user -> usuario | assistant -> IA) e a mensagem

# Manter o histórico de mensagens (criar memória)
  
if mensagem_usuario:

    # Mostrar a mensagem na tela
    st.chat_message("user").write(mensagem_usuario) # Mostrar a mensagem na tela. 'Quem esta mandando' (user -> usuario | assistant -> IA) e a mensagem

    mensagem1 = {"role": "user", "content": mensagem_usuario} # Cria um dicionário com a mensagem do usuário 

    st.session_state["lista_mensagens"].append(mensagem1) # Adiciona a mensagem do usuário à lista de mensagens 

    # Lista de modelos por ordem de preferência
    modelos_disponiveis = ["gemini-2.5-flash", "gemini-1.5-flash-latest"]
    resposta_modelo = None

    for modelo in modelos_disponiveis: # Para cada modelo na lista de modelos por ordem de preferência
        try:
            # Mandar a mensagem para o modelo de IA responder
            resposta_modelo = modelo_ia.chat.completions.create(
                messages=st.session_state["lista_mensagens"], # Passa a lista de mensagens para o modelo de IA
                model=modelo # Modelo de IA
            )# Criar uma resposta para completar o chat
            break  # Sucesso: sai do loop de tentativas
        except openai.RateLimitError:
            # Cota excedida no modelo atual, passa para o próximo da lista
            print(f"Limite atingido para {modelo}. Tentando modelo alternativo...")
            time.sleep(1)  # Pequena pausa antes de tentar novamente
            continue
        except (openai.InternalServerError, openai.NotFoundError, openai.APIError) as e:
            print(f"Erro ao tentar o modelo {modelo}: {e}")
            continue  # Se der erro 503, 404 ou outro da API, tenta o próximo modelo da lista

    # Apenas tenta acessar .choices se a resposta NÃO for None
    if resposta_modelo is not None:

    # resposta_ia = resposta_modelo.choices[0].message.content # Pega a resposta da IA

        resposta_ia = resposta_modelo.choices[0].message.content # Pega a resposta da IA

        # Mostrar a resposta na tela
        st.chat_message("assistant").write(resposta_ia) # Mostrar a resposta na tela. 'Quem esta mandando' (user -> usuario | assistant -> IA) e a mensagem

        mensagem2 ={"role": "assistant", "content": resposta_ia} # Cria um dicionário com a resposta da IA
        st.session_state["lista_mensagens"].append(mensagem2) # Adiciona a resposta da IA à lista de mensagens
        print("Resposta do modelo de IA:", resposta_ia)
    else:
        # Se todos os modelos falharem por cota/erro
        st.error("Serviço temporariamente indisponível. Aguarde cerca de 1 minuto antes de enviar uma nova mensagem.")

