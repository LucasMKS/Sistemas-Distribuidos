# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

# Retorne o salário bruto e o salário líquido dos funcionários de uma empresa. A empresa
# paga R$ 40,00 por hora normal trabalhada e R$50,00 por hora extra. O salário líquido é
# igual ao salário bruto descontando-se 10% de impostos.


@app.route('/', methods=['GET', 'POST'])
def vendas():

    if request.method == 'POST':
        normal = request.form.get('normal')
        extra = request.form.get('extra')

        salarioLiquido = (float(normal) * 40) + (float(extra) * 50)
        salarioBruto = salarioLiquido * 0.90

        return '''
            <h2>Salario liquido: {}</h2>
            <h2>Salario bruto: {}</h2>'''.format(salarioLiquido, salarioBruto)

    return '''
            <form method="POST">
                <div><label>Horas normais trabalhada: </label>
                <input type="number" id="normal" name="normal" min="0" max="500"></div>
                <div><label>Horas extras trabalhada: </label>
                <input type="number" id="extra" name="extra" min="0" max="500"></div>
                <input type="submit" value="Enviar">
            </form>'''

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)


    
# venv_empresa\Scripts\Activate.ps1
# python main.py
# http://127.0.0.1:5000/
# deactivate
