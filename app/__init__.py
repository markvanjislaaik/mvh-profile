from flask import Flask
import secrets

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key = secrets.token_hex(16)

from app import routes