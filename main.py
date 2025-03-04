from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atalho')
jog2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jog3 = Jogo('Mortal Combat', 'Luta', 'PS2')
lista = [jogo1, jog2, jog3]    

app = Flask(__name__)

app.secret_key = 'teste'

@app.route('/')
def home():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/add-jogo/')
def novo():
    return render_template('novo.html',titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST',])
def auth():
    if 'mestre' == request.form['senha']:
        session['logged_user'] = request.form['usuario']
        flash(request.form['usuario'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario não logado!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(debug=True)
