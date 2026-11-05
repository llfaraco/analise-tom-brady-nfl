# Tom Brady | Indicadores históricos com fonte explícita

**Python · Validação de dados · Métricas descritivas**

Exercício de análise esportiva com um resumo de carreira documentado. A versão anterior misturava listas de 21 e 22 elementos e não construía o DataFrame. A revisão substitui essa estrutura por um snapshot histórico e remove métricas de vitórias por temporada que não tinham uma base reconciliada.

## Executar

Somente biblioteca padrão do Python; validado com Python 3.12.

```bash
python src/tom_brady_analise.py
python -m unittest discover -s tests
```

## Resultados

| Métrica | Resultado |
| --- | ---: |
| Temporadas na carreira, 2000–2022 | 23 |
| Participações em Super Bowl | 10 |
| Títulos de Super Bowl | 7 |
| Participações / temporadas de carreira | 43,48% |
| Títulos / participações | 70% |

São proporções históricas, não probabilidades futuras. O denominador de 23 inclui 2000 e 2008; não é chamado de temporadas completas como titular.

[Dados e fonte](data/career_summary.json) · [Saída calculada](artifacts/summary.json)

## Fonte e escopo

Resumo conferido em 05/11/2026 na [publicação oficial dos Buccaneers de 01/02/2023](https://www.buccaneers.com/news/tom-brady-career-stats-records-nfl-2000-2022-patriots-bucs), que informa 23 temporadas, 10 Super Bowls e 7 títulos. O projeto transcreve apenas esses totais e calcula duas proporções; não apresenta uma base jogo a jogo nem uma comparação estatística completa com outros quarterbacks.

Os testes verificam o snapshot, totais incoerentes e ausência de participações. Quando não há participações, a conversão é indisponível, em vez de um zero enganoso.

Revisão implementada com assistência de IA. O objetivo é demonstrar uma pergunta bem delimitada, definição de denominadores e validação antes da conclusão.

[Portfólio](https://github.com/llfaraco)
