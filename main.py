from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self,nome,nickname,senha):
        self.nome = nome 
        self.nickname = nickname
        self.senha = senha

user1 = Usuario('nathalia', 'nath123', 'metre')    
user2 = Usuario('raphael', 'rphl123', '12345')  
user3 = Usuario('marie', 'marie20', '12345')   

usuarios = {
    user1.nickname : user1,
    user2.nickname : user2,
    user3.nickname : user3,
}

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
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', proxima=url_for('novo'))) 
    return render_template('novo.html',titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('home'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/auth', methods=['POST',])
def auth():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['logged_user'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            next_page = request.form['proxima']
            return redirect(next_page)
    else:
        flash('Usuario não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('home'))

app.run(debug=True)
