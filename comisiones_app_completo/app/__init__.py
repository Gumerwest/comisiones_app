from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    csrf.init_app(app)
    
    login.login_view = 'auth.login'
    login.login_message = 'Por favor, inicie sesión para acceder a esta página.'
    
    # Registrar blueprints
    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.routes.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from app.routes.comisiones import bp as comisiones_bp
    app.register_blueprint(comisiones_bp, url_prefix='/comisiones')
    
    from app.routes.temas import bp as temas_bp
    app.register_blueprint(temas_bp, url_prefix='/temas')
    
    # Registrar página de inicio
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Gestor de errores
    from app.routes.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    return app

from app import models
