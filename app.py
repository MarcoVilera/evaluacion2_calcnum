from flask import Flask,render_template, request,jsonify
import numpy as np
import sympy as sym
from taylor_interpolation import TaylorInter
from PotenciaSim import PotenciaSim
app = Flask(__name__)

@app.route('/')
def index():
    """
    Esta función define una ruta para la URL raíz ("/") y devuelve la plantilla representada
    "index.html".
    :return: el resultado de la función `render_template`, que normalmente es un archivo HTML.
    """
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    """
    Endpoint de la API de Python que recibe datos, realiza cálculos de
    potencia simétricos en una matriz y realiza interpolación de Taylor en una función determinada.
    :return: un objeto JSON con las siguientes claves y valores:
    - 'resultado': Verdadero (lo que indica que la solicitud fue exitosa)
    - 'potSim': el resultado del cálculo de potencia simétrica
    - 'inter': el resultado del cálculo de interpolación de Taylor
    """
    print('Recieved data')
    print(request.json)
    #Método de la potencia simetrica
    matrix = np.array(request.json['matrix'])
    exp = request.json['exp']
    potencia = PotenciaSim(matrix, exp)
    potsim = potencia.pot_sym()
    #Interpolación de Taylor
    x = sym.Symbol('x')
    if request.json['function'] == '1': function = sym.cos(x)

    if request.json['function'] == '2': function = sym.exp(x)*sym.cos(x) + 1

    if request.json['function'] == '3': function = sym.exp(x+2)*sym.sin(x+1) - 3
    function = sym.lambdify(x, function, 'numpy') #Convierte la función simbólica a una función numérica
    PE = request.json['PE'] #Punto de Expansión

    PI = request.json['PI'] #Punto de Interpolación
    taylor = TaylorInter(function, PE, PI)
    interpolation = taylor.taylor_inter()

    return jsonify({'result': True,
                    'potSim':potsim,
                    'inter': interpolation}) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)
