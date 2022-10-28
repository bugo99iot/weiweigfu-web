from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(os.getenv('ENV_FILE', 'env')))

trues = ['true', 't']

ENVIRONMENT = os.environ['ENVIRONMENT']
DEBUG = os.getenv('DEBUG').lower() if (os.getenv('DEBUG') and os.getenv('DEBUG') in trues) else False
