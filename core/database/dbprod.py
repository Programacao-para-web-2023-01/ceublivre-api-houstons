from deta import Deta
from dotenv import load_dotenv
import os
load_dotenv()

project_key = os.environ.get('project_key')
deta = Deta(project_key=project_key)
db = deta.Base("produtos")