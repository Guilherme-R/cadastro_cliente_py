from flask import Flask, render_template, request, redirect, url_for, session, flash, url_for
from entities.Usuario import Usuario
from entities.Endereco import Endereco
from entities.Estados import estados

app= Flask(__name__)
app.secret_key = 'amoeba'

usuario1 = Usuario('Guilherme', 'guilherme', 'guilherme@live.com', Endereco('Rua Zélia, 510 - Jd. Madalena', 'São Paulo', 'São Paulo', '03567-032'))
usuario2 = Usuario('Pamela','pamela','pamela@live.com', Endereco('Rua Gazela, 6924 - Jd. Pock', 'Belo Horizonte', 'Minas Gerais', '01023-050'))


usuarios = { usuario1.email: usuario1,
             usuario2.email: usuario2 }

@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista Usuários', usuarios=usuarios, enumerate=enumerate)


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['email'] in usuarios:
        usuario = usuarios[request.form['email']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.nome
            flash(usuario.nome + ' Logou com sucesso!')
            proxima_pagina = request.form['proxima']
            print(proxima_pagina)
            return redirect(proxima_pagina)
        else:
            flash('Senha Inválida');
    else:
        flash('Não foi possivel realizar o login!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado!')
    return redirect(url_for('index'))


@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastro')))
    return render_template('cadastro.html', estados=estados, titulo='Cadastro Usuário')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    senha = request.form['senha']
    email = request.form['email']
    logradouro = request.form['logradouro']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cep = request.form['cep']

    usuario = Usuario(nome,senha,email, Endereco(logradouro, cidade, estado, cep))
    usuarios[usuario.email] = usuario

    return redirect(url_for('index'));

app.run(debug=True)
