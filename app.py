from datetime import date, datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "chave-demonstracao-ambiente-dev"

def classificar_pvps(data_validade_str: str) -> dict:
    validade = datetime.strptime(data_validade_str, "%Y-%m-%d").date()
    dias = (validade - date.today()).days
    if dias <= 7:
        return {"nivel": "URGENTE", "dias": dias, "cor": "danger", "icone": "⚠"}
    elif dias <= 15:
        return {"nivel": "ATENÇÃO", "dias": dias, "cor": "warning", "icone": "⏳"}
    return {"nivel": "NORMAL", "dias": dias, "cor": "success", "icone": "✔"}

@app.route("/")
def index():
    return render_template("estoque.html")

if __name__ == "__main__":
    app.run(debug=False)
