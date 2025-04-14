#Projeto-de-Envio-de-Mensagens-via-WhatsApp-com-Supabase-e-Twilio
Este projeto permite enviar mensagens em massa via WhatsApp utilizando a API do Twilio e dados armazenados no Supabase. Abaixo está o passo a passo completo de como configurar e rodar o projeto na sua máquina.

Pré-requisitos
Antes de começar, você precisa de:

Python 3.x instalado
Uma conta no Twilio
Uma conta no Supabase
Instalar as dependências do projeto


Passo 1: Criar uma Conta no Twilio

Acesse Twilio e crie uma conta gratuita.
Após criar a conta, faça login e vá até o painel do Twilio.
No painel, anote as seguintes informações:

Account SID: Este é o identificador da sua conta.
Auth Token: O token de autenticação necessário para realizar requisições.
WhatsApp Sandbox: Para contas gratuitas, o Twilio oferece um número de WhatsApp sandbox para testes. No painel do Twilio, encontre a opção "Programmable Messaging" e clique em "Try it Out" para obter o número do sandbox e configurar a verificação via WhatsApp.

Passo 2: Criar uma Conta no Supabase

Acesse Supabase e crie uma conta.
Crie um novo projeto no Supabase.
No painel do Supabase, acesse a opção SQL Editor e crie uma tabela chamada Contatos com os campos:

id: INT (Primary Key)
nome: VARCHAR
telefone: VARCHAR

No painel de configuração do projeto, anote as informações:

URL do Supabase: Encontre em API > Project URL.
Chave API do Supabase: Encontre em API > anon key.

Passo 3: Preparar o Arquivo .env
Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:


SUPABASE_URL=<URL_DO_SUPABASE>
SUPABASE_KEY=<SUPABASE_ANON_KEY>
TWILIO_ACCOUNT_SID=<TWILIO_ACCOUNT_SID>
TWILIO_AUTH_TOKEN=<TWILIO_AUTH_TOKEN>
TWILIO_PHONE_NUMBER=<NUMERO_DE_WHATSAPP_TWILIO>

Substitua os valores entre <...> pelos valores obtidos nas etapas anteriores.

SUPABASE_URL: A URL do seu projeto no Supabase.
SUPABASE_KEY: A chave da API do Supabase.

TWILIO_ACCOUNT_SID: O SID da sua conta no Twilio.
TWILIO_AUTH_TOKEN: O token de autenticação do Twilio.
TWILIO_PHONE_NUMBER: O número de WhatsApp fornecido pelo Twilio (sandbox ou número oficial).

Passo 4: Instalar as Dependências
No terminal, dentro da pasta do seu projeto, execute o seguinte comando para instalar as dependências necessárias:


pip install -r requirements.txt
O arquivo requirements.txt deve conter as seguintes bibliotecas:

requests
python-dotenv
supabase

Caso não tenha o arquivo requirements.txt, você pode instalar as dependências manualmente com:

pip install requests python-dotenv supabase

Passo 5: Rodar o Projeto
Certifique-se de que o arquivo .env está configurado corretamente.
Execute o código com o seguinte comando:

python main.py


O programa irá:

Conectar-se ao banco de dados Supabase para buscar os contatos.
Pedir para você inserir a mensagem que deseja enviar.
Enviar a mensagem via Twilio para todos os contatos.

Estrutura do Projeto
A estrutura do projeto deve ser similar a:

/projeto
  ├── .env
  ├── main.py
  ├── SupaBase_Client.py
  ├── ApiWPP.py
  └── requirements.txt

main.py: O arquivo principal que executa o envio de mensagens.
SupaBase_Client.py: Arquivo responsável por se conectar ao Supabase e buscar os contatos.
ApiWPP.py: Arquivo responsável por enviar mensagens via API do Twilio.

Tratamento de Erros
Se o envio de mensagens falhar, o sistema irá capturar o erro e mostrar uma mensagem de falha. Você pode ajustar o tratamento de erros no código para dar mais detalhes ou realizar tentativas adicionais.

Passo 6: Considerações Finais
Limites do Twilio: A conta gratuita do Twilio possui um limite diário de mensagens. Caso atinja esse limite, você receberá um erro informando que não pode enviar mais mensagens.
Uso Responsável: O envio de mensagens em massa deve ser feito com cautela e de acordo com as políticas de uso do WhatsApp e Twilio.
