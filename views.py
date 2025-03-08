from flask import Flask, render_template, request, redirect, session, flash, url_for
from main import app,db
from models import Jogos,Usuarios

@app.route('/')
def home():
    lista = Jogos.query.order_by(Jogos.id)
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

    jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('home'))
    else:
        novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
        db.session.add(novo_jogo)
        db.session.commit()


    return redirect(url_for('home'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/auth', methods=['POST',])
def auth():

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()

    if usuario:
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