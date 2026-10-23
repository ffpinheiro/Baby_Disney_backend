import json
import os
import re
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

# A cifra fica em cifra_propria.py (ao lado deste arquivo)
# ou dentro da pasta "criptografia".
try:
    from cifra_propria import criptografar
except ImportError:
    from criptografia.cifra_propria import criptografar

app = Flask(__name__)

# Arquivo onde os envios ficam guardados JÁ CRIPTOGRAFADOS.
# Para ler de volta, rode:  python descriptografar.py
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, "dados_criptografados.json")

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
# PONTE: formulário -> cifra -> terminal + arquivo
# ---------------------------------------------------------------
def cifrar_em_partes(valor):
    """Criptografa um campo e devolve uma lista de partes, para que
    depois dê para descriptografar sem erro.

    Cada parte é [tipo, texto]:
      ["cifrado", "#Thyph @Lbeot"]  -> texto passado pela ALTERNEX-7
      ["simbolo", "@"]              -> símbolo que a cifra não aceita
                                       (e-mail, horário...), mantido igual
    """
    partes = []

    for pedaco in re.split(f"({PROIBIDOS})", valor.strip()):
        if not pedaco:
            continue

        if re.fullmatch(PROIBIDOS, pedaco) or not pedaco.strip():
            partes.append(["simbolo", pedaco])
        else:
            partes.append(["cifrado", criptografar(pedaco)])

    return partes


def juntar(partes):
    """Junta as partes no texto criptografado que aparece no terminal."""
    return "".join(texto for _, texto in partes) or "(vazio)"


def salvar_envio(registro):
    """Guarda o envio (já criptografado) no arquivo JSON."""
    try:
        with open(ARQUIVO, encoding="utf-8") as f:
            envios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        envios = []

    envios.append(registro)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(envios, f, ensure_ascii=False, indent=2)


@app.route("/criptografia", methods=["POST"])
def criptografia():
    origem = request.referrer or "origem desconhecida"
    campos = []

    print("\n" + "=" * 60)
    print(f"FORMULÁRIO RECEBIDO ({origem})")
    print("=" * 60)

    for campo in request.form:
        if campo.startswith("_"):  # campos técnicos do formsubmit
            continue

        for valor in request.form.getlist(campo):
            partes = cifrar_em_partes(valor)
            campos.append({"campo": campo, "partes": partes})

            print(f"{campo}:")
            if MOSTRAR_ORIGINAL:
                print(f"   original ......: {valor}")
            print(f"   criptografado .: {juntar(partes)}")

    salvar_envio({
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "pagina": origem,
        "campos": campos,
    })

    print("-" * 60)
    print("Salvo em dados_criptografados.json")
    print("Para descriptografar, rode:  python descriptografar.py")
    print("=" * 60 + "\n")

    # volta para a mesma página, sem abrir página nova
    return redirect(request.referrer or url_for("index"))


if __name__ == "__main__":
    # abre o navegador sozinho em http://127.0.0.1:8080 (só uma vez)
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        import threading
        import webbrowser
        threading.Timer(
            1.5, lambda: webbrowser.open("http://127.0.0.1:8080/")
        ).start()

    app.run(host="0.0.0.0", port=8080, debug=True)