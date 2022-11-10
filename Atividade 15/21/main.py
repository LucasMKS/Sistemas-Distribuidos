# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)



ESCOLA = [{'matricula': 1, 'nome': 'Ana', 'nota': 72.00},
            {'matricula': 2, 'nome': 'Bruna', 'nota': 71.50},
            {'matricula': 3, 'nome': 'Carlos', 'nota': 68.50},
            {'matricula': 4, 'nome': 'Diogo', 'nota': 70.00},
            {'matricula': 5, 'nome': 'Ester', 'nota': 69.00}]

# http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def consulta_todos_registros():
    resp = ESCOLA
    if 'X-nome-produto' in request.headers:
        nome = request.headers['X-nome-produto']
        for escola in ESCOLA:
            if escola['nome'] == nome:
                resp = escola
    return jsonify(resp)

# http://127.0.0.1:5000/Ester
@app.route('/<string:nome>', methods=['GET'])
def consulta_isolada(nome):
    resp = {'valor': None}
    for escola in ESCOLA:
        if escola['nome'] == nome:
            resp = escola
    return jsonify(resp)

# http://127.0.0.1:5000/inserir/6/Lucas/72.55
@app.route('/inserir/<int:matricula>/<string:nome>/<float:nota>', methods=['GET','POST'])
def inserir_registro(matricula, nome, nota):
    ESCOLA.append({'matricula': matricula, 'nome': nome, 'nota': nota})
    return jsonify({'matricula': matricula, 'nome': nome, 'nota': nota})

# http://127.0.0.1:5000/atualizar/notas/5.0
# http://127.0.0.1:5000/atualizar/notas/-5.0
@app.route('/atualizar/notas/<float(signed=True):nota>',
methods=['GET','PATCH'])
def atualizar_totalmente(nota):
    resp = {'nota': '', 'nota': None}
    for notas in ESCOLA:
        notas['nota'] += nota
    return consulta_todos_registros()

# http://127.0.0.1:5000/atualizar/Bruna/10.00
# http://127.0.0.1:5000/atualizar/Diogo/-10.00
@app.route('/atualizar/<string:nome>/<float(signed=True):nota>',
methods=['GET','PATCH'])
def atualizar_parcialmente(nome, nota):
    resp = {'nota': '', 'nota': None}
    for notas in ESCOLA:
        if notas['nome'] == nome:
            notas['nota'] += nota
            resp = notas
    return jsonify(resp)

# http://127.0.0.1:5000/remover/1
@app.route('/remover/<int:matricula>', methods=['GET','DELETE'])
def remover_registro(matricula):
    for i, matri in enumerate(ESCOLA):
        if matri['matricula'] == matricula:
            del ESCOLA[i]
    return jsonify({'ESCOLA': ESCOLA})


if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)


    
# venv_empresa\Scripts\Activate.ps1
# python main.py
# http://127.0.0.1:5000/
# deactivate
