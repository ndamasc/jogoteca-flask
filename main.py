from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    lista = ['Tetris', 'Skyrim', 'Clash']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
