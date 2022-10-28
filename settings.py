from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(os.getenv('ENV_FILE', 'env')))

trues = ['true', 't']

DEBUG = os.environ['DEBUG'].lower() if os.environ['DEBUG'].lower() in trues else False
PORT = int(os.environ['PORT'])
HOST = os.environ['HOST']
