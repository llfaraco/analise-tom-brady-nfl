# Tom Brady | Exercício de análise esportiva com Python

**Projeto de estudo · pandas · Dados definidos manualmente · Em revisão**

## Objetivo

Praticar a construção de um DataFrame e o cálculo de indicadores de temporadas, participações em Super Bowl e proporções de resultados.

O interesse em futebol americano conecta este exercício à minha trajetória de projetos, incluindo a [Yardline](https://yardlinefantasyfootball.com).

## Arquivos e dependências

- `src/tom_brady_analise.py`: listas manuais, DataFrame, agregações e saída em Markdown.
- Dependências: pandas, NumPy e tabulate.

## Estado atual

A construção do DataFrame está bloqueada por uma inconsistência: a lista de temporadas e a lista de resultados de Super Bowl têm **21 elementos**, enquanto a lista de vitórias tem **22**.

Por isso, os números apresentados na versão anterior do README não são mantidos como resultados validados. A base precisa ser alinhada por temporada e conferida com uma fonte histórica antes de qualquer conclusão.

## Preparação do ambiente

```bash
git clone https://github.com/llfaraco/analise-tom-brady-nfl.git
cd analise-tom-brady-nfl
python -m pip install pandas numpy tabulate
```

Após corrigir e validar os dados, o ponto de entrada é:

```bash
python src/tom_brady_analise.py
```

O comando falha na criação do DataFrame enquanto a inconsistência permanecer.

## Aprendizados e evolução

Alinhar cada observação a uma temporada, distinguir vitórias da equipe de vitórias atribuídas ao jogador, documentar fontes e evitar interpretar proporções históricas como probabilidades futuras. A prioridade é uma base coerente antes de uma conclusão atraente.

## Contato

[Lucas Faraco](https://www.linkedin.com/in/lucasrfaraco) · [E-mail](mailto:lucas.rfaraco@gmail.com) · [Perfil e portfólio](https://github.com/llfaraco)
