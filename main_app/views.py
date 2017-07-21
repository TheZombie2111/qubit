from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, abort, url_for,\
    redirect, abort
from main_app.models import *

main_app = Blueprint('main_app', __name__, template_folder='templates/')

@main_app.route('/')
@main_app.route('/<lang>/')
def index(lang=None):
    return pyvool.render('main_app/index.j2', lang, MAIN=True)