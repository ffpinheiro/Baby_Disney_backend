# [tutorial](https://github.com/ffpinheiro/Baby_Disney_backend/tree/main#instala%C3%A7%C3%A3o) <br>
# [tarefas](https://github.com/ffpinheiro/Baby_Disney_backend/tree/main#lista-de-tarefas-por-dupla)
# Sobre o projeto

Aplicação web em Flask que criptografa e descriptografa mensagens usando uma cifra própria. A aplicação não persiste dados.

## Estrutura do projeto

```
.
├── app.py              # Aplicação Flask (rotas)
├── requirements.txt    # Dependências
├── criptografia/       # Algoritmos de criptografia
├── static/             # CSS e JS
├── templates/          # HTML
└── testes/             # Testes automatizados
```

## Instalação

1. Instale o [Python 3.10+](https://www.python.org/downloads/). No Windows, marque **"Add Python to PATH"**.
2. Baixe o projeto (botão **Code → Download ZIP** no GitHub) e extraia, ou use `git clone <URL-DO-REPOSITORIO>`.
3. Abra o terminal dentro da pasta do projeto (onde está o `app.py`) e rode:

```bash
python -m pip install -r requirements.txt
```

## Executando

```bash
python -m flask run --debug
```

Abra no navegador: **http://127.0.0.1:5000**

Para parar o servidor, pressione `Ctrl + C`.

## Testes

```bash
python -m pytest testes/
```

> No Linux e no macOS, use `python3` no lugar de `python`.
> Se der o erro `externally-managed-environment`, crie um ambiente virtual:
> `python3 -m venv venv && source venv/bin/activate` e repita o passo 3.

***
# Lista de tarefas por dupla

## Dupla A: Cifra própria (Integrantes 2 e 3)

**Código**
- [ ] Definir as regras da cifra própria e como a chave funciona e é validada
- [ ] Acordar com a Dupla B a interface dos módulos de cifra (entradas, saídas e erros) antes de implementar
- [ ] Implementar a cifra própria, César e Transposição em `criptografia/`, com código comentado

**Texto**
- [ ] Revisão Teórica (dividida entre os dois, conforme o combinado)
- [ ] Desenvolvimento do módulo criptográfico: conceito, motivação, regras, chave, criptografia e descriptografia, com fluxograma ou pseudocódigo
- [ ] Exemplos práticos e limitações da cifra
- [ ] Reunir as referências da parte teórica

## Dupla B: Sistema e back-end (Integrantes 1 e 4)

**Código**
- [ ] Criar as rotas e conectar os módulos de `criptografia/`, devolvendo resultado e erros para a tela
- [x] Configurar o GitHub (branches, README com instruções de execução) e o `requirements.txt`

**Texto**
- [ ] Metodologia
- [ ] Desenvolvimento: arquitetura, estrutura de diretórios e fluxo do sistema, com diagramas (basta citar que a aplicação não persiste dados)
- [ ] Reunir a codificação completa em anexo

## Dupla C: Interface, testes e qualidade (Integrantes 5 e 6)

**Integrante 5, interface**
- [ ] Montar o projeto Flask, integrando o HTML em `templates/` e CSS e JS existentes em `static/`
- [ ] Escrever a seção de interface no Desenvolvimento, com capturas de tela

**Integrante 6, testes**
- [ ] Montar a estratégia e a tabela de casos de teste (criptografia, descriptografia, mensagens vazias, entradas e chaves inválidas, caracteres não suportados)
- [ ] Executar os testes, incluindo a integração com o Flask, e salvar os testes automatizados em `testes/`

**Texto da dupla**
- [ ] Conclusões e Recomendações (primeira versão)

# Trabalho escrito

| Seção                      | Conteúdo                                                                                                                                                                                                                           | Dupla |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Introdução                 | "Apresenta o tema, justificativa, objetivos (geral e específicos) e escopo do estudo, contextualizando o problema."<br>*Nota: Explicar sobre os tipos de criptografia (cifra de César, subtituição, transposição)*                       | C      |
| Revisão Teórica            | "Fundamentação teórica necessária para a compreensão do tema, incluindo conceitos, definições e referências bibliográficas."<br>*Nota: Explicar sobre a criptografia escolhida (criptografia que criamos para o projeto)*                | A     |
| Metodologia                | "Descrição dos métodos, ferramentas, materiais e procedimentos adotados."                                                                                                                                                          | B     |
| Desenvolvimento            | Parte principal do trabalho, contendo:<br>• Descrição do sistema ou projeto;<br>• Diagramas, esquemas e modelagens;<br>• Resultados obtidos e análise crítica.<br>• A codificação completa.<br>*Nota: Subcapítulo de resultados obtidos* | B      |
| Conclusão                  | "Síntese dos resultados, dificuldades, limitações e sugestões para trabalhos futuros."<br>*Nota: Resumo das dificuldades enfrentadas e como foram superadas*                                                                             | Todos      |
| Referências | "Listagem de obras, artigos, sites e normas técnicas consultados, seguindo normas ABNT."                                                                                                                                           | Todos      |
| Fichas                     | "Anexo das fichas individualizadas por aluno."                                                                                                                                                                                     | Individual      |
- [ ] Introdução
- [ ] Revisão Teórica
- [ ] Metodologia
- [ ] Desenvolvimento
- [ ] Conclusão
- [ ] Referências

# Itens sem dono

| Item | Responsável |
|---|---|
| Capa, Sumário, formatação ABNT e revisão final |  |
| Resumo e palavras-chave |  |
| Referências consolidadas |  |
| Fichas individuais | Individual |
| Slides e apresentação |  |
| Postagem no sistema da UNIP |  |
