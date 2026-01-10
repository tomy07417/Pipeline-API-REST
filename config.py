import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
API_TOKEN = os.getenv('API_TOKEN')
API_BASE_URL = os.getenv('API_BASE_URL', 'https://iansaura.com/api')

if not API_TOKEN:
    raise ValueError("API_TOKEN no configurado. Creá un archivo .env")

if not EMAIL:
    raise ValueError("EMAIL no configurado. Creá un archivo .env")