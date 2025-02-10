from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # Metoda pro routing indexu #
    return render_template('index.html')

@app.route('/abc')
def abc(): # Metoda pro routing indexu #
    return render_template('abc.html')

@app.route('/heb')
def heb(): # Metoda pro routing indexu #
    return render_template('heb.html')


@app.route('/azb')
def azb(): # Metoda pro routing indexu #
    return render_template('azb.html')


@app.route('/base')
def base(): # Metoda pro routing indexu #
    return render_template('base.html')

@app.route('/alfa')
def alfa(): # Metoda pro routing indexu #
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