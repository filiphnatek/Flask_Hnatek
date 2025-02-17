from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():  # Metoda pro routing indexu #
    return render_template('index.html')

@app.route('/abc')
def abc(): # Metoda pro routing abc #
    return render_template('abc.html')

@app.route('/heb')
def heb(): # Metoda pro routing heb #
    return render_template('heb.html')


@app.route('/azb')
def azb(): # Metoda pro routing azb #
    return render_template('azb.html')


@app.route('/base')
def base(): # Metoda pro routing base #
    return render_template('base.html')

@app.route('/alfa')
def alfa(): # Metoda pro routing alfa #
    return render_template('alfa.html')

# @app.route('/link')
#def link(): # Metoda pro routing alfa #
#    return render_template('link.html')



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

@app.route ("/odkaz", methods= ["GET", "POST"])
def odkaz():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        radio = request.form["radio"]
        return render_template("zkouska.html", username=username, password=password, radio=radio)
    return render_template("link.html")



if __name__== "__main__":
    app.run(debug=True)