import os
from main import app


def recupera_img(id):
    for nome_arq in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arq:
            return nome_arq
    return 'capa_padrao.jpg'