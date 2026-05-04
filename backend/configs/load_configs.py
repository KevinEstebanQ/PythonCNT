from dotenv import load_dotenv
from pathlib import Path

def load_configs():
    dotenv_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(dotenv_path)