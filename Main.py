from SupaBase_Client import busca_contatos
from ApiWPP import enviar_mensagem

contatos = busca_contatos()

# Listar contatos no Supabase
for c in contatos:
   print(f"- {c['nome']} ({c['telefone']})")
    

mensagem_base = input("\nDigite a mensagem que deseja enviar para todos os contatos: ")

enviados = []
falhas = []

# Enviar mensagem para cada contato
for contato in contatos:
    nome = contato["nome"]
    numero = contato["telefone"]  
    mensagem_final = f"Olá {nome}! {mensagem_base}"
    
    try:
        resposta = enviar_mensagem(numero, mensagem_final)
        print(f"[DEBUG] Resposta completa do Twilio para {numero}: {resposta}")

        # Verificando se a resposta é uma string (SID)
        if isinstance(resposta, str):
            print(f"✅ Mensagem enviada para {nome} ({numero})")
            enviados.append(nome)
        else:
            print(f"❌ Falha no envio para {nome} ({numero}): {resposta}")
            falhas.append(nome)

    except Exception as e:
        print(f"❌ Erro ao enviar para {nome} ({numero}): {e}")
        falhas.append(nome)

# Enviar a mensagem
print("\n📋 Relatório Final:")
print("✅ Enviados:", enviados)
print("❌ Falhas:", falhas)
