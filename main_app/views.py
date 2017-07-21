from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, abort, url_for,\
    redirect, abort
from main_app.models import *

main_app = Blueprint('main_app', __name__, template_folder='templates/')

@main_app.route('/')
def index():
    alldata = Data.query.all()
    return render_template('main_app/template.pug', context=alldata)