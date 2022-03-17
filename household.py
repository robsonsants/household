from flask import Flask, jsonify, request, abort, request, render_template, make_response
from flask import current_app as app
from flask_login import LoginManager
from flask_login import login_user, logout_user, login_required, current_user


loginmanager = LoginManager

app = Flask(__name__)
app.secret_key = '123456'

#configuracao de plugins
loginmanager.init_app(app)

casas = []
reservas = []

class Usuario():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

#dicionario a preencher com o par id:usuario
# onde id é a chave inteira e usuario é instancia da classe usuario
usuarios = {}

@app.route('/home')
def inicio():
    return render_template('cad.html')

@app.route('/dois')
def dois():
    return render_template('filha2.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('telacadastro.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        for id in usuarios.keys():
            usuario = usuarios[id]
            if nome == usuario.nome:
                return 'Usuário já existe'
        novo = Usuario(nome, senha)
        usuarios[len(usuarios)+1] = novo

        return 'cadastro bem sucedido'

    else:
        return abort(405)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('telalogin.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        for id in usuarios.keys():
            usuario = usuarios[id]
            if nome == usuario.nome and senha == usuario.senha:
                resposta = make_response(render_template('logou.html'))
                resposta.headers['id_usuario'] = id
                return resposta
        return 'usuario ou senha incorretos'

@app.route('/teste')
def teste():
    return request.headers['id_usuario']

app.run()