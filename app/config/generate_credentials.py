from os import environ
import json

def generate_credentials():
    credentials = json.loads(environ.get('CREDENTIALS'))
    with open('./credentials.json', mode='w', encoding='utf-8') as f:
         f.write(json.dumps(credentials))
