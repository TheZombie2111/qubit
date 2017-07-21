from main_app.views import main_app
from flask import Flask, send_from_directory, request, redirect, render_template, abort
import os
import sys

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.register_blueprint(main_app)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

app.secret_key = 'e514a9436619810e4b45398425210c6f'
app.run(host='0.0.0.0', port=8000)
