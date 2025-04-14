import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def busca_contatos():
    """
    Função para buscar contatos no Supabase.
    """
    response = supabase.table("contatos").select("*").execute()
    return response.data
