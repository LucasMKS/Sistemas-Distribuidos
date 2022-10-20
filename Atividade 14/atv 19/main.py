# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)

produtos = [{'codigo': 1, 'nome': 'cachorro quente', 'preco': 12.00},
            {'codigo': 2, 'nome': 'sanduíche', 'preco': 23.89},
            {'codigo': 3, 'nome': 'pastel', 'preco': 3.98},
            {'codigo': 4, 'nome': 'refrigerante', 'preco': 5.72},
            {'codigo': 5, 'nome': 'suco', 'preco': 4.35}]

# Consultar todos os itens
# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    return jsonify({'produtos': produtos})

# Consultar item pelo codigo
# http://127.0.0.1:5000/produtos/3
@app.route('/produtos/<int:codigo>', methods=['GET'])
def retornar_dados_do_produto_informado(codigo):
    resp = {'codigo': None, 'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            resp = produto
    return jsonify(resp)

# Adicionar produto novo
# http://127.0.0.1:5000/produtos/6/coxinha/5.67
@app.route('/produtos/<int:codigo>/<string:nome>/<float:preco>', methods=['POST'])

def inserir_produto(codigo, nome, preco):
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco})
    return jsonify({'codigo': codigo, 'nome': nome, 'preco': preco})

# Atualizar preço pelo código
# http://127.0.0.1:5000/produtos/1/10.00
# http://127.0.0.1:5000/produtos/1/-10.00
@app.route('/produtos/<int:codigo>/<float(signed=True):preco>', methods=['PATCH'])
def alterar_preco_do_produto(codigo, preco):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['preco'] += preco
            resp = produto
    return jsonify(resp)

# Atualizar produto e preço pelo código
# http://127.0.0.1:5000/produtos/3/coxinha/5.00
@app.route('/produtos/<int:codigo>/<string:nome>/<float(signed=True):preco>', methods=['PATCH'])
def alterar_produto(codigo, nome, preco):
    resp = {'codigo': None, 'nome': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['preco'] = preco
            produto['nome'] = nome
            resp = produto
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/1
@app.route('/produtos/<int:codigo>', methods=['DELETE'])
def remover_produto(codigo):
    for i, produto in enumerate(produtos):
        if produto['codigo'] == codigo:
            del produtos[i]
    return jsonify({'produtos': produtos})

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)