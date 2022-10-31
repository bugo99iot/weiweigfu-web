from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(os.getenv('ENV_FILE', 'env')))

trues = ['true', 't']

ENVIRONMENT = os.environ['ENVIRONMENT']
DEBUG = os.getenv('DEBUG').lower() if (os.getenv('DEBUG') and os.getenv('DEBUG') in trues) else False

ROOT_PATH = Path(__file__).parent.absolute()
DATA_PATH = os.path.join(ROOT_PATH, 'data')
APP_PATH = ROOT_PATH
APP_STATIC_PATH = os.path.join(APP_PATH, 'static')

FLASK_APP_SECRET_KEY = os.environ['FLASK_APP_SECRET_KEY']
