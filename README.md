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
Acesse a aba API e copie:

- 'Project URL'
- 'anon key'

📝 Passo 3: Configurar o Arquivo .env
Crie um arquivo chamado .env na raiz do projeto e adicione:

SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-anon-key

TWILIO_ACCOUNT_SID=seu-sid-do-twilio
TWILIO_AUTH_TOKEN=seu-token-do-twilio
TWILIO_PHONE_NUMBER=whatsapp:+55xxxxxxxxxx

📦 Passo 4: Instalar as Dependências
No terminal, dentro da pasta do seu projeto, execute:

pip install -r requirements.txt

Se não tiver o requirements.txt, instale manualmente:

pip install requests python-dotenv supabase

▶️ Passo 5: Executar o Projeto
No terminal, com o .env configurado, execute:

python main.py

O sistema irá:

Buscar os contatos do Supabase

Pedir a mensagem a ser enviada

Enviar uma mensagem personalizada para cada contato

📁 Estrutura Sugerida do Projeto
bash
Copiar
Editar
/projeto
├── .env
├── main.py
├── SupaBase_Client.py
├── ApiWPP.py
└── requirements.txt
main.py: Lê os contatos e executa os envios

SupaBase_Client.py: Acesso ao Supabase

ApiWPP.py: Integração com a API do Twilio

⚠️ Tratamento de Erros
O sistema irá informar falhas de envio e registrar quais contatos tiveram erro.

Possíveis causas:

Erro no número do telefone

Limite diário da conta Twilio gratuita

🧠 Dicas Finais
Limite diário do Twilio: Contas gratuitas podem enviar até 10 mensagens/dia no Sandbox.

Envio responsável: Respeite a privacidade dos usuários e as políticas do WhatsApp.

NUNCA suba seu .env no GitHub! Use o .gitignore.

👀 Exemplo de .env.example para subir com segurança
env
Copiar
Editar
SUPABASE_URL=coloque_aqui_a_url_do_projeto
SUPABASE_KEY=sua_anon_key
TWILIO_ACCOUNT_SID=seu_sid
TWILIO_AUTH_TOKEN=seu_token
TWILIO_PHONE_NUMBER=whatsapp:+55xxxxxxxxxx
📌 Licença
Este projeto é de uso educacional. Fique à vontade para clonar, adaptar e utilizar!

