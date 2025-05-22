from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from app.models import Comision, Tema

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Mostrar página principal con listado de comisiones activas
    comisiones = Comision.query.filter_by(activa=True).all()
    
    # Obtener temas destacados (los más votados)
    temas_destacados = Tema.query.filter_by(estado='aprobado').order_by(Tema.votos.count().desc()).limit(5).all()
    
    return render_template('main/index.html', 
                          title='Comisiones de Trabajo Marinas de España',
                          comisiones=comisiones,
                          temas_destacados=temas_destacados)

@bp.route('/acerca')
def acerca():
    return render_template('main/acerca.html', title='Acerca de la Plataforma')

@bp.route('/contacto')
def contacto():
    return render_template('main/contacto.html', title='Contacto')
