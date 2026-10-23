import json
import os

# A cifra fica em cifra_propria.py (ao lado deste arquivo)
# ou dentro da pasta "criptografia".
try:
    from cifra_propria import descriptografar
except ImportError:
    from criptografia.cifra_propria import descriptografar

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, "dados_criptografados.json")


def descriptografar_partes(partes):
    texto = ""

    for tipo, conteudo in partes:
        if tipo == "cifrado":
            texto += descriptografar(conteudo)
        else:
            texto += conteudo

    return texto


def main():
    try:
        with open(ARQUIVO, encoding="utf-8") as f:
            envios = json.load(f)
    except FileNotFoundError:
        print("Ainda não há dados. Envie um formulário pelo site primeiro.")
        return
    except json.JSONDecodeError:
        print("O arquivo dados_criptografados.json está danificado.")
        return

    if not envios:
        print("Ainda não há dados. Envie um formulário pelo site primeiro.")
        return

    print(f"\n{len(envios)} envio(s) encontrado(s).")

    for numero, envio in enumerate(envios, start=1):
        print("\n" + "=" * 60)
        print(f"ENVIO {numero} - {envio['data_hora']}")
        print(f"Página: {envio['pagina']}")
        print("=" * 60)

        for item in envio["campos"]:
            partes = item["partes"]
            cifrado = "".join(texto for _, texto in partes)

            try:
                original = descriptografar_partes(partes)
            except ValueError as erro:
                original = f"(erro ao descriptografar: {erro})"

            print(f"{item['campo']}:")
            print(f"   criptografado .....: {cifrado or '(vazio)'}")
            print(f"   descriptografado ..: {original or '(vazio)'}")

    print()


if __name__ == "__main__":
    main()