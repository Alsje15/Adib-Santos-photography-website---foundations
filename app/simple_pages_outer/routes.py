from fileinput import filelineno
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.models.orders import Foto


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

@blueprint.route('/street/<slug>')
@blueprint.route('/portrait/<slug>')
def ind(slug):
    foto = Foto.query.filter_by(slug=slug).first()
    return render_template('simple_pages/ind.html', foto=foto)

@blueprint.route('/checkout')
def new(): 
    return render_template('simple_pages/new.html')


"""
@blueprint.route('/shop')
def shop():
    page_number = request.args.get('page', 1, type=int)
    fotos_pagination = Foto.query.paginate(page_number, current_app.config['FOTOS_PER_PAGE']) 
    return render_template('shop/index.html', fotos_pagination = fotos_pagination)

@blueprint.route('/shop/<slug>') 
def ind(slug): 
    foto = Foto.query.filter_by(slug=slug).first_or_404()    
    return render_template('/shop/ind.html', foto = foto)
"""


