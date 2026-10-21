import re
from flask import Flask, render_template, request, redirect, url_for

# A cifra fica em cifra_propria.py (ao lado deste arquivo)
# ou dentro da pasta "criptografia".
try:
    from cifra_propria import criptografar
except ImportError:
    from criptografia.cifra_propria import criptografar

app = Flask(__name__)

# True  -> o terminal mostra também o texto original (bom para testar)
# False -> o terminal mostra só o texto criptografado
MOSTRAR_ORIGINAL = False

# Caracteres que a ALTERNEX-7 não aceita (ex.: o "@" e o "." do e-mail)
PROIBIDOS = r"[.,!?;:#@]+"


# ---------------------------------------------------------------
# PÁGINAS (cada uma aceita com e sem ".html", porque os links
# dos HTMLs usam "index.html", "contato.html" etc.)
# ---------------------------------------------------------------
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/espaco")
@app.route("/espaco.html")
def espaco():
    return render_template("espaco.html")


@app.route("/sobre")
@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")


@app.route("/agendamento")
@app.route("/agendamento.html")
def agendamento():
    return render_template("agendamento.html")


@app.route("/contato")
@app.route("/contato.html")
def contato():
    return render_template("contato.html")


# ---------------------------------------------------------------
# PONTE: formulário -> cifra -> terminal
# ---------------------------------------------------------------
def cifrar_campo(valor):
    """Criptografa um campo. Se tiver caracteres que a cifra recusa
    (como @ e . do e-mail ou : do horário), cifra só os pedaços de
    texto e mantém esses caracteres no lugar."""
    valor = valor.strip()

    if not valor:
        return "(vazio)"

    try:
        return criptografar(valor)
    except ValueError:
        partes = re.split(f"({PROIBIDOS})", valor)
        saida = []
        for parte in partes:
            if parte.strip() and not re.fullmatch(PROIBIDOS, parte):
                saida.append(criptografar(parte))
            else:
                saida.append(parte)
        return "".join(saida)


@app.route("/criptografia", methods=["POST"])
def criptografia():
    origem = request.referrer or "origem desconhecida"

    print("\n" + "=" * 60)
    print(f"FORMULÁRIO RECEBIDO ({origem})")
    print("=" * 60)

    for campo in request.form:
        if campo.startswith("_"):  # campos técnicos do formsubmit
            continue

        for valor in request.form.getlist(campo):
            print(f"{campo}:")
            if MOSTRAR_ORIGINAL:
                print(f"   original ......: {valor}")
            print(f"   criptografado .: {cifrar_campo(valor)}")

    print("=" * 60 + "\n")

    # volta para a mesma página, sem abrir página nova
    return redirect(request.referrer or url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)