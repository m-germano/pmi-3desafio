from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # ou o endereço do seu banco de dados MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcal2012'
app.config['MYSQL_DB'] = 'database_projeto4'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inscrever', methods=['POST'])
def inscrever():
    if request.method == 'POST':
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO inscricoes (email) VALUES (%s)", (email,))
        mysql.connection.commit()
        cur.close()
        return redirect('/#inscrito')
    else:
        return redirect('/')

@app.route('/html')
def html():
    return render_template('curso-html.html')

@app.route('/js')
def js():
    return render_template('curso-js.html')

@app.route('/python')
def python():
    return render_template('curso-python.html')

@app.route('/nodejs')
def nodejs():
    return render_template('curso-nodejs.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('curso-bootstrap.html')

@app.route('/curso-mysql')
def curso_mysql():
    return render_template('curso-mysql.html')

@app.route('/github')
def github():
    return redirect('https://www.github.com/m-germano/projetoAPI-horus')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/inscricoes')
def inscricoes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, email FROM inscricoes")
    data = cur.fetchall()
    cur.close()
    return render_template('inscricoes.html', inscricoes=data)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM inscricoes WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('inscricoes'))

if __name__ == "__main__":
    app.run(debug=True)
