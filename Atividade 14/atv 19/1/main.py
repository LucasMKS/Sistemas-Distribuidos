# Importar a classe Flask e o objeto request:
from flask import Flask, request
from math import pow, sqrt
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/teste/1
# Aceita requisições com os métodos GET e POST.
# GET: gera um formulário em HTML para o usuário
# enviar dados para o servidor.
# POST: lê os dados enviados pelo usuário através
# do furmulário HTML.
@app.route('/teste/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():
# Trata a requisição com método POST:
    if request.method == 'POST':
        abscissas1 = request.form.get('abscissas1')
        abscissas2 = request.form.get('abscissas2')
        ordenadas1 = request.form.get('ordenadas1')
        ordenadas2 = request.form.get('ordenadas2')

        contaab = float(abscissas2) - float(abscissas1)
        contaor = float(ordenadas2) - float(ordenadas1)
        potab = pow(contaab, 2)
        potor = pow(contaor, 2)
        resul = potab + potor
        d = sqrt(resul)

        return '''
            <h3>Valor da 1° abscissa: {}</h3>
            <h3>Valor da 2° abscissa: {}</h3>
            <h3>Valor da 1° ordenada: {}</h3>
            <h3>Valor da 2° ordenada: {}</h3>
            <h1>A distância entre eles é de: <b>{:.2f}</b></h1>'''.format(abscissas1, abscissas2, ordenadas1, ordenadas2, d)

# Caso contrário, trata a requisição com método GET:
    return '''
            <form method="POST">
                <div><label>Informe o 1° abscissas</label>
                <input type="number" id="abscissas1" name="abscissas1" min="1" max="100"></div>

                <div><label>Informe o 2° abscissas</label>
                <input type="number" id="abscissas2" name="abscissas2" min="1" max="100"></div>

                <div><label>Informe o 1° ordenadas</label>
                <input type="number" id="ordenadas1" name="ordenadas1" min="1" max="100"></div>

                <div><label>Informe o 2° ordenadas</label>
                <input type="number" id="ordenadas2" name="ordenadas2" min="1" max="100"></div>

                <input type="submit" value="Enviar">
            </form>'''

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)


    
# venv_empresa\Scripts\Activate.ps1
# python main.py
# http://127.0.0.1:5000/
# deactivate
