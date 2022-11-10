# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)


produtos = [{'Camiseta': 'pequena', 'preco': 10.00},{'Camiseta': 'media', 'preco': 12.00},
{'Camiseta': 'grande', 'preco': 15.00}]

# http://127.0.0.1:5000/produtos
@app.route('/', methods=['GET'])
def retornar_todos_os_produtos():
    resp = produtos

    if 'X-nome-produto' in request.headers:
        nome = request.headers['X-nome-produto']
        for produto in produtos:
            if produto['nome'] == nome:
                resp = produto
    return jsonify(resp)

@app.route('/vendas', methods=['GET', 'POST'])
def vendas():

    if request.method == 'POST':
        pequena = request.form.get('pequena')
        media = request.form.get('media')
        grande = request.form.get('grande')

        valor = (float(pequena) * 10) + (float(media) * 12) + (float(grande) * 15)

        return '''
            <h2>Valor arrecadado: {}</h2>'''.format(valor)

    return '''
            <form method="POST">
                <div><label>Camisas pequenas vendidas: </label>
                <input type="number" id="pequena" name="pequena" min="0" max="500"></div>
                <div><label>Camisas medias vendidas: </label>
                <input type="number" id="media" name="media" min="0" max="500"></div>
                <div><label>Camisas grandes vendidas: </label>
                <input type="number" id="grande" name="grande" min="0" max="500"></div>
                <input type="submit" value="Enviar">
            </form>'''

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)


    
# venv_empresa\Scripts\Activate.ps1
# python main.py
# http://127.0.0.1:5000/
# deactivate
