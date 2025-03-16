import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do jogo',[validators.DataRequired(), validators.Length(min=1, max=50)] )
    categoria = StringField('Categoria',[validators.DataRequired(), validators.Length(min=1, max=40)] )
    console = StringField('Console',[validators.DataRequired(), validators.Length(min=1, max=20)] )
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nome de usuario', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_img(id):
    for nome_arq in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arq:
            return nome_arq
    return 'capa_padrao.jpg'