
import re

# ALTERNEX-7 - Cifra de Substituição Alternada
# Desenvolvida pela Dupla A

DESLOCAMENTO = 7

# Pontuação proibida nesta versão
PONTUACAO = ".,!?;:"

def validar_texto(texto):
    if not isinstance(texto, str):
        raise ValueError("A mensagem deve ser um texto.")

    if not texto.strip():
        raise ValueError("A mensagem não pode estar vazia.")

    for caractere in texto:
        if caractere in PONTUACAO:
            raise ValueError("Pontuação não é permitida.")

        if caractere in "#@":
            raise ValueError("Os símbolos # e @ são reservados.")


def deslocar_letra(letra, posicoes):
    # Identifica letras maiúsculas e minúsculas
    if "A" <= letra <= "Z":
        inicio = ord("A")
    elif "a" <= letra <= "z":
        inicio = ord("a")
    else:
        # Números, acentos e outros caracteres
        return letra

    posicao = ord(letra) - inicio

    nova_posicao = (posicao + posicoes) % 26

    return chr(inicio + nova_posicao)


def criptografar(texto):
    validar_texto(texto)

    partes = re.split(r"(\s+)", texto)
    resultado = []
    contador = 0

    for parte in partes:
        if not parte:
            continue

        if parte.isspace():
            resultado.append(parte)
            continue

        if contador % 2 == 0:
            simbolo = "#"
            deslocamento = DESLOCAMENTO
        else:
            simbolo = "@"
            deslocamento = -DESLOCAMENTO

        palavra_cifrada = ""

        for letra in parte:
            palavra_cifrada += deslocar_letra(
                letra, deslocamento
            )

        resultado.append(simbolo + palavra_cifrada)
        contador += 1

    return "".join(resultado)


def descriptografar(texto):
    partes = re.split(r"(\s+)", texto)
    resultado = []
    contador = 0

    for parte in partes:
        if not parte:
            continue

        if parte.isspace():
            resultado.append(parte)
            continue

        simbolo_esperado = (
            "#" if contador % 2 == 0 else "@"
        )

        if not parte.startswith(simbolo_esperado):
            raise ValueError(
                "Marcador inválido na mensagem."
            )

        deslocamento = (
            -DESLOCAMENTO
            if simbolo_esperado == "#"
            else DESLOCAMENTO
        )

        palavra_original = ""

        for letra in parte[1:]:
            palavra_original += deslocar_letra(
                letra, deslocamento
            )

        resultado.append(palavra_original)
        contador += 1

    mensagem = "".join(resultado)
    validar_texto(mensagem)

    return mensagem

# Teste interativo da ALTERNEX-7
if __name__ == "__main__":
    print("=== ALTERNEX-7 ===")

    while True:
        mensagem = input(
            "\nDigite uma mensagem (ou SAIR): "
        )

        if mensagem.upper() == "SAIR":
            print("Programa encerrado.")
            break

        try:
            cifrada = criptografar(mensagem)
            original = descriptografar(cifrada)

            print("Original:", mensagem)
            print("Criptografada:", cifrada)
            print("Descriptografada:", original)

            if original == mensagem:
                print("TESTE APROVADO!")
            else:
                print("TESTE REPROVADO!")

        except ValueError as erro:
            print("ERRO:", erro)
