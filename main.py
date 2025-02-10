from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abc')
def abc():
    return render_template('abc.html')

@app.route('/heb')
def heb():
    return render_template('heb.html')


@app.route('/azb')
def azb():
    return render_template('azb.html')


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/alfa')
def alfa():
    return render_template('alfa.html')


@app.route("/<jmeno>")
def hello(jmeno):
    return f"<h1>Hello, {jmeno}!</h1>"

def nasobeni(a, b):
    return a * b

@app.route("/nasobeni/<a>/<b>")
def nasobeni_route(a, b):
    try:
        return f"{int(a) * int(b)} toto je vysledek"
    except ValueError:
        return "nejsou cisla"

if __name__== "__main__":
    app.run(debug=True)