from flask import Flask, render_template

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/home')
def home():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atalho')
    jog2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jog3 = Jogo('Mortal Combat', 'Luta', 'PS2')
    lista = [jogo1, jog2, jog3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
