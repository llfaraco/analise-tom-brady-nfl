import pandas as pd
import numpy as np

# ==============================================================================
# 1. Definição e Criação do DataFrame Simulado
# Os dados representam as 22 temporadas de Tom Brady como QB titular na NFL.
# ==============================================================================

# 22 temporadas relevantes: 2001 a 2019 (Patriots, excluindo 2008) e 2020 a 2022 (Buccaneers)
anos_carreira = sorted(list(set(list(range(2001, 2008)) + [2009] + list(range(2010, 2020)) + list(range(2020, 2023)))))

# Resultados do Super Bowl (SB):
# 1 = Vitória do SB
# 0.5 = Derrota do SB
# 0 = Não chegou ao SB/Eliminado
sb_resultados = [
    1,    # 2001 (SB XXXVI - W)
    0,    # 2002
    1,    # 2003 (SB XXXVIII - W)
    1,    # 2004 (SB XXXIX - W)
    0,    # 2005
    0,    # 2006
    0.5,  # 2007 (SB XLII - L)
    0,    # 2009 (Retorno de lesão em 2008)
    0,    # 2010
    0.5,  # 2011 (SB XLVI - L)
    0,    # 2012
    0,    # 2013
    1,    # 2014 (SB XLIX - W)
    0,    # 2015
    1,    # 2016 (SB LI - W)
    0.5,  # 2017 (SB LII - L)
    1,    # 2018 (SB LIII - W)
    0,    # 2019
    1,    # 2020 (SB LV - W)
    0,    # 2021
    0     # 2022
]

# Vitórias na Temporada Regular
vitorias_regulares = [
    11, 9, 14, 14, 10, 12, 16, 10, 14, 13,
    13, 12, 12, 12, 12, 14, 13, 11, 12, 11, # Corrigido 2019 para 12 e 2020 para 11
    13, 8
]

dados_brady = {
    'Temporada': anos_carreira,
    'Super_Bowl_Resultado': sb_resultados,
    'Vitorias_Temporada_Regular': vitorias_regulares
}

df_brady = pd.DataFrame(dados_brady)

# ==============================================================================
# 2. Cálculos e Análise de Dominância
# ==============================================================================

# Métrica: Contagem de aparições no SB (vitória ou derrota)
df_brady['Aparencia_SB'] = df_brady['Super_Bowl_Resultado'].apply(lambda x: 1 if x > 0 else 0)

# Métrica: Cálculo Total
total_temporadas = len(df_brady)
total_super_bowls_disputados = df_brady['Aparencia_SB'].sum()
vitorias_super_bowls = df_brady[df_brady['Super_Bowl_Resultado'] == 1].shape[0]
total_vitorias_carreira = df_brady['Vitorias_Temporada_Regular'].sum()

# Métrica: Porcentagem de Sucesso
media_vitorias_regulares = df_brady['Vitorias_Temporada_Regular'].mean()

percentual_carreira_chegou_sb = (total_super_bowls_disputados / total_temporadas) * 100

# Evita divisão por zero
if total_super_bowls_disputados > 0:
    percentual_sb_vencidos = (vitorias_super_bowls / total_super_bowls_disputados) * 100
else:
    percentual_sb_vencidos = 0.0

# ==============================================================================
# 3. Geração e Impressão dos Resultados
# ==============================================================================

print("## 📊 Análise da Carreira de Tom Brady: Dominância na NFL")
print("----------------------------------------------------------\n")

# Dicionário de resultados para formatar a saída
dominancia = {
    'Total_Temporadas_Titular': total_temporadas,
    'Total_Super_Bowls_Disputados': total_super_bowls_disputados,
    'Total_Super_Bowls_Vencidos': vitorias_super_bowls,
    'Total_Vitorias_Temporada_Regular': total_vitorias_carreira,
    'Media_Vitorias_Regulares_Por_Ano': f"{media_vitorias_regulares:.2f}",
    'Percentual_Carreira_Chegou_SB': f"{percentual_carreira_chegou_sb:.2f}%",
    'Percentual_SB_Vencidos': f"{percentual_sb_vencidos:.2f}%"
}

df_dominancia = pd.DataFrame(list(dominancia.items()), columns=['Métrica', 'Valor'])

# Adicionando Contexto (para o README e apresentação)
df_dominancia['Contexto_NFL'] = [
    '22 temporadas de alto nível.',
    'Mais SBs disputados do que qualquer franquia da NFL.',
    'Mais SBs vencidos do que qualquer franquia da NFL (Steelers e Patriots têm 6).',
    'Acumulado histórico que representa quase 12 temporadas de vitórias para um QB médio.',
    'Média consistente e bem acima da média de 8-9 vitórias da liga.',
    'Quase 50% de probabilidade de chegar ao SB em qualquer ano de sua carreira.',
    'Taxa de sucesso (7-3) excelente para a pressão e dificuldade de um SB.'
]

print("### 📝 Tabela de Métricas Chave de Dominância\n")
# Uso de to_markdown para fácil visualização em GitHub/Jupyter
print(df_dominancia.to_markdown(index=False))

print("\n----------------------------------------------------------")
print("### 📈 Conclusão Analítica Corroborativa")
print("----------------------------------------------------------")
print(f"Tom Brady disputou **{dominancia['Total_Super_Bowls_Disputados']} Super Bowls** em **{dominancia['Total_Temporadas_Titular']} temporadas** como titular, o que significa que ele chegou à final em **{dominancia['Percentual_Carreira_Chegou_SB']}** de suas temporadas (quase 1 a cada 2 anos).")
print(f"Com **7 títulos**, sua taxa de conversão em Super Bowls disputados é de **{dominancia['Percentual_SB_Vencidos']}**.")
print(f"Essa combinação de longevidade, consistência (média de {dominancia['Media_Vitorias_Regulares_Por_Ano']} vitórias/ano) e sucesso em momentos decisivos é a evidência estatística da sua dominância sem precedentes na história da NFL.")
