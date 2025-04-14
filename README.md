# 📤 Disparador de Mensagens WhatsApp com Supabase e Twilio

Este projeto permite enviar mensagens em massa via WhatsApp utilizando a API do **Twilio** e dados armazenados no **Supabase**.

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter:

- ✅ Python 3.x instalado
- ✅ Conta no [Twilio](https://www.twilio.com/)
- ✅ Conta no [Supabase](https://supabase.com/)
- ✅ Variáveis de ambiente configuradas em um `.env`

---

## 🚀 Passo 1: Criar uma Conta no Twilio

1. Acesse o site do [Twilio](https://www.twilio.com/) e crie uma conta gratuita.
2. Após criar, vá até o **Console** do Twilio e anote:

   - `Account SID`
   - `Auth Token`

3. Vá até **"Messaging" > "Try it Out" > "Try WhatsApp"** e:
   - Siga o QR Code para verificar o número no **Sandbox do WhatsApp**
   - Use o número de sandbox fornecido no formato `whatsapp:+55...`

---

## 🛠️ Passo 2: Criar uma Conta no Supabase

1. Acesse [Supabase](https://supabase.com/) e crie uma conta.
2. Crie um novo projeto e acesse o painel.
3. No menu lateral, vá em **"SQL Editor"** e cole o seguinte código SQL:

   ```sql
   create table Contatos (
     id serial primary key,
     nome varchar,
     telefone varchar
   );
