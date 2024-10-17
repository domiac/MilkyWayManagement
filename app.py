from flask import Flask
from os import getenv
import secrets

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes