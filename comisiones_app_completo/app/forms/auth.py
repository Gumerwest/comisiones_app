from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, FileField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL, Optional
from app.models import Usuario

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Iniciar Sesión')

class RegistroForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    razon_social = StringField('Razón Social', validators=[DataRequired()])
    nombre_comercial = StringField('Nombre Comercial', validators=[DataRequired()])
    cargo = StringField('Cargo', validators=[DataRequired()])
    submit = SubmitField('Registrarse')
    
    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email ya está registrado. Por favor, utilice otro.')

class ComisionForm(FlaskForm):
    nombre = StringField('Nombre de la Comisión', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    imagen = FileField('Imagen (opcional)')
    submit = SubmitField('Guardar')

class TemaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    resumen = TextAreaField('Resumen', validators=[DataRequired()])
    situacion_actual = TextAreaField('Situación Actual')
    submit = SubmitField('Proponer Tema')

class PatrocinadorForm(FlaskForm):
    patrocinador = StringField('Nombre del Patrocinador', validators=[DataRequired()])
    logo = FileField('Logo del Patrocinador')
    enlace = StringField('Enlace Web', validators=[Optional(), URL()])
    submit = SubmitField('Guardar Patrocinador')

class ComentarioForm(FlaskForm):
    contenido = TextAreaField('Comentario', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class DocumentoForm(FlaskForm):
    nombre = StringField('Nombre del Documento', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    documento = FileField('Archivo', validators=[DataRequired()])
    submit = SubmitField('Subir')

class ReunionForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    fecha = DateTimeField('Fecha y Hora', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    duracion = IntegerField('Duración (minutos)', validators=[Optional()])
    lugar = StringField('Lugar', validators=[Optional()])
    enlace_virtual = StringField('Enlace de Reunión Virtual', validators=[Optional(), URL()])
    submit = SubmitField('Proponer Reunión')
