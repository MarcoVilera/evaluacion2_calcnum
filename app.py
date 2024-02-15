from flask import Flask,render_template, request,jsonify
import numpy as np
import sympy as sym
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    print('Recieved data')
    print(request.json)
    #Método de la potencia simetrica
    matrix = np.array(request.json['matrix'])
    exp = request.json['exp']

    #Interpolación de Taylor
    x = sym.Symbol('x')
    if request.json['function'] == '1': function = sym.cos(x)

    if request.json['function'] == '2': function = sym.exp(x)*sym.cos(x) + 1

    if request.json['function'] == '3': function = sym.exp(x+2)*sym.sen(x+1) - 3

    PE = request.json['PE'] #Punto de Expansión

    PI = request.json['PI'] #Punto de Interpolación
    
    return jsonify({'result': 'ok'}) #TODO Modificar para que devuelva el resultado de las operaciones
if __name__ == '__main__':
    app.run(debug=True, port=5000)
