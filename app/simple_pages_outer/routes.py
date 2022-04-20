from crypt import methods
from fileinput import filelineno
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.models.orders import Foto, Order
from app.extensions.database import db
from app.extensions.database import CRUDMixin


blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index(): 
    return render_template('simple_pages/index.html')

@blueprint.route('/receipt.txt')
def receipt(): 
    return send_file('static/downloads/receipt.txt', as_attachment = True)

""" NAV BAR """

@blueprint.route('/about')
def about(): 
    return render_template('simple_pages/about.html')

@blueprint.route('/street')
def street(): 
    all_fotos = Foto.query.all()
    return render_template('simple_pages/street.html', fotos = all_fotos)

@blueprint.route('/portrait')
def portrait(): 
    all_fotos = Foto.query.all()
    return render_template('simple_pages/portrait.html', fotos = all_fotos)


""" Special routes """

# Normal rendering of the simple_pages/ind.html
@blueprint.route('/street/<name>', methods=['GET', 'POST'])
@blueprint.route('/portrait/<name>', methods=['GET', 'POST'])
def ind(name):
    fotos = Foto.query.filter_by(name=name).first()

    # Create an order 
    order = Order(
        street = request.form.get('fstreet'), 
        city = request.form.get('fcity'),
        zip = request.form.get('fzip'),
        country = request.form.get('fcountry'),
        foto_id = request.form.get('ffoto_id')
    )
    order.save()

    return render_template('simple_pages/ind.html', fotos=fotos)



