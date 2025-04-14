import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Carregar credenciais do Twilio
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

def enviar_mensagem(numero, mensagem):
    """
    Função para enviar mensagem via WhatsApp utilizando o Twilio.
    """
    client = Client(account_sid, auth_token)

    # Enviar a mensagem via WhatsApp
    message = client.messages.create(
        body=mensagem,
        from_=twilio_whatsapp_number,
        to=f"whatsapp:{numero}"
    )

    return message.sid  
