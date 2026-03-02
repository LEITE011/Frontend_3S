from flask import Flask, render_template, url_for, flash, request, redirect, session
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'leite_gato'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_massage = 'Para visualizar essa pagina faça o login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/')
@login_required
def home():
    # havera processos aqui
    return render_template('home.html')


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/funcionarios')
@login_required
def funcionarios():
    func_sql = select(Funcionario)
    resultado = db_session.execute(func_sql).scalars().all()
    return render_template("Funcionarios.html",resultado=resultado)


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/Geometria')
def Geometria():
    return render_template("geometria.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("form_email")
        senha = request.form.get("form_senha")
        '''vericar unsando not
        if not email or not senha:
            flash('Por favor preencha todos os campos', 'alert-danger')
        return render_template('login.html')
        '''
        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                # se encontrado na base de dados
                if resultado_email.check_password(senha):
                    # login correto
                    login_user(resultado_email)
                    flash(f'login efetuado com sucesso', 'success')
                    print('logado com sucesso')
                    return redirect(url_for('home'))

                else:
                    # senha incorreta
                    flash('Senha incorreta', 'alert-danger')
                    return redirect(url_for('login'))
            else:
                # se nao encontrado
                flash(f'Email não encontrado', 'alert-danger')
                return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            soma = n1 + n2
            flash('Soma realizado com sucesso!', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar a Soma', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            subtrair = n1 - n2
            flash('Subtração realizado com sucesso!', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar a Subtração', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/Multiplicar', methods=['GET', 'POST'])
def Multiplicar():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Multiplicar = n1 * n2
            flash('Multiplicação realizado com sucesso!', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, Multiplicar=Multiplicar)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar a Multiplicação', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/Dividir', methods=['GET', 'POST'])
def Dividir():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Dividir = n1 / n2
            flash('Divisão realizado com sucesso!', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, Dividir=Dividir)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar a Divisão', 'alert-danger')
    return render_template("operacoes.html")


@app.route('/Triangulo', methods=['GET', 'POST'])
def Triangulo():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Triangulo = n1 * n2 / 2
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Triangulo=Triangulo)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Circulo', methods=['GET', 'POST'])
def Circulo():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Circulo = 3.14 * (n1 * n1)
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Circulo=Circulo)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Quadrado', methods=['GET', 'POST'])
def Quadrado():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Quadrado = n1 * n2
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n1, Quadrado=Quadrado)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Hexagono', methods=['GET', 'POST'])
def Hexagono():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Hexagono = n1 * n1 / 2 * 6
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Hexagono=Hexagono)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/TrianguloP', methods=['GET', 'POST'])
def TrianguloP():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            TrianguloP = n1 * 3
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, TrianguloP=TrianguloP)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Circulop', methods=['GET', 'POST'])
def Circulop():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            Circulop = n1 * 2 * 3.14
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, Circulop=Circulop)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Quadradop', methods=['GET', 'POST'])
def Quadradop():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            Quadradop = n1 * 4
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, Quadradop=Quadradop)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/Hexagonop', methods=['GET', 'POST'])
def Hexagonop():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            Hexagonop = n1 * 6
            flash('Calculo realizado com sucesso!', 'alert-success')
            return render_template("geometria.html", n1=n1, Hexagonop=Hexagonop)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('preencha o campo para realizar o Calculo', 'alert-danger')
    return render_template("geometria.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get("form_nome")
        data_nascimeto = request.form.get("form_data")
        cpf = request.form.get("form_cpf")
        email = request.form.get("form_email")
        senha = request.form.get("form_senha")
        cargo = request.form.get("form_cargo")
        salario = request.form.get("form_salario")
        if not nome or not email or not senha:
            flash('Por favor preencha todos os campos', 'danger')
            return render_template('cadastro.html')
        vericar_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(vericar_email).scalar_one_or_none()
        vericar_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
        existe_cpf = db_session.execute(vericar_cpf).scalar_one_or_none()
        if existe_email:
            flash(f'Email {email} ja existente', 'danger')
            return render_template('cadastro.html')
        if existe_cpf:
            flash(f'Email {cpf} ja existente', 'danger')
            return render_template('cadastro.html')
        try:
            novo_Funcionario = Funcionario(nome=nome, data_nascimeto=data_nascimeto, cpf=cpf, email=email, senha=senha, cargo=cargo, salario=salario)
            novo_Funcionario.set_password(senha)
            db_session.add(novo_Funcionario)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado com sucesso', 'success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar ususario', 'danger')
            print(f'Erro na base de dados: {e}')
            return redirect(url_for('cadastro_funcionario'))
        except Exception as e:
            flash(f'Erro ao cadastrar usuario', 'danger')
            print(f'Erro ao cadastrar: {e}')
            return redirect(url_for('cadastro_funcionario'))
    return render_template('cadastro.html')


@app.route("/logout")
def logout():
    logout_user()
    flash('Logout com sucesso', 'success')
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
