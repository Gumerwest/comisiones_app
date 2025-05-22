from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import db
from app.models import Usuario
from app.forms.auth import LoginForm, RegistroForm

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Email o contraseña incorrectos', 'danger')
            return redirect(url_for('auth.login'))
        
        if not user.activo:
            flash('Su cuenta aún no ha sido activada. Por favor, espere la aprobación de un administrador.', 'warning')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        user.ultimo_acceso = datetime.utcnow()
        db.session.commit()
        
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        
        return redirect(next_page)
    
    return render_template('auth/login.html', title='Iniciar Sesión', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistroForm()
    if form.validate_on_submit():
        user = Usuario(
            email=form.email.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            telefono=form.telefono.data,
            razon_social=form.razon_social.data,
            nombre_comercial=form.nombre_comercial.data,
            cargo=form.cargo.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('¡Gracias por registrarse! Su cuenta está pendiente de aprobación por un administrador.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/registro.html', title='Registro', form=form)

@bp.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    # Implementar edición de perfil
    return render_template('auth/perfil.html', title='Mi Perfil')
