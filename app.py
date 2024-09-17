from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
import secrets


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes