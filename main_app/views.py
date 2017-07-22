from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, jsonify
from main_app.models import *

main_app = Blueprint('main_app', __name__, template_folder='templates/')

@main_app.route('/')
def index():
    return render_template('main_app/template.pug', type='choose')

@main_app.route('/frontend')
def frontend():
	return render_template('main_app/template.pug', type='frontend')

@main_app.route('/request', methods=['POST'])
def request():
	array = []
	alldata = Data.query.all()
	for i in alldata:
		tempObject = {
			'Imei': i.Imei,
			'CurrentDateTime': i.CurrentDateTime,
			'GPSDateTime': i.GPSDateTime,
			'Datatype': i.Datatype,
			'Address': i.Address,
			'Distance': i.Distance
		}
		array.append(tempObject)
	return jsonify(array)

@main_app.route('/backend')
def backend():
	alldata = Data.query.all()
	secondary = []
	for i in alldata:
		if i.Datatype == 1:
			prev = i.Distance
			prevTime = i.CurrentDateTime
		if i.Datatype == 2:
			newTime = i.CurrentDateTime - prevTime
			tempObject = {
				'CurrentDateTime': newTime,
				'Datatype': i.Datatype,
				'Address': i.Address,
				'Distance': i.Distance - prev
			}
			secondary.append(tempObject)
	return render_template('main_app/template.pug', data=alldata, secondary=secondary, type='backend')