from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/mysql')
def mysql():
    return render_template('curso-mysql.html')

@app.route('/github')
def github():
    return redirect('https://www.github.com/m-germano/projetoAPI-horus')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')
   

    


if __name__ == "__main__":
    app.run(debug=True)
