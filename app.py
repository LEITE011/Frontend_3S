from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/Geometria')
def Geometria():
    return render_template("geometria.html")




@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)

    return render_template("operacoes.html")

@app.route('/Multiplicar', methods=['GET', 'POST'])
def Multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Multiplicar = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, Multiplicar=Multiplicar)


@app.route('/Dividir', methods=['GET', 'POST'])
def Dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Dividir = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, Dividir=Dividir)

@app.route('/Triangulo', methods=['GET', 'POST'])
def Triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Triangulo = n1 * n2 / 2
            return render_template("geometria.html", n1=n1, n2=n2, Triangulo=Triangulo)



@app.route('/Circulo', methods=['GET', 'POST'])
def Circulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Circulo = 3.14 * (n1 * n1)
            return render_template("geometria.html", n1=n1, n2=n2, Circulo=Circulo)


@app.route('/Quadrado', methods=['GET', 'POST'])
def Quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Quadrado = n1 * n2
            return render_template("geometria.html", n1=n1, n2=n1, Quadrado=Quadrado)



@app.route('/Hexagono', methods=['GET', 'POST'])
def Hexagono():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            Hexagono = n1 * n1 / 2 * 6
            return render_template("geometria.html", n1=n1, n2=n2, Hexagono=Hexagono)


@app.route('/TrianguloP', methods=['GET', 'POST'])
def TrianguloP():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            TrianguloP = n1 * 3
            return render_template("geometria.html", n1=n1, TrianguloP=TrianguloP)



@app.route('/Circulop', methods=['GET', 'POST'])
def Circulop():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            Circulop = n1 * 2 * 3.14
            return render_template("geometria.html", n1=n1, Circulop=Circulop)



@app.route('/Quadradop', methods=['GET', 'POST'])
def Quadradop():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            Quadradop = n1 * 3
            return render_template("geometria.html", n1=n1, Quadradop=Quadradop)


@app.route('/Hexagonop', methods=['GET', 'POST'])
def Hexagonop():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            Hexagonop = n1 * 3
            return render_template("geometria.html", n1=n1, Hexagonop=Hexagonop)

#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)