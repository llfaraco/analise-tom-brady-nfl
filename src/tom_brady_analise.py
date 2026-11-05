"""Indicadores descritivos a partir de um resumo histórico com fonte explícita."""
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def analyze(record):
    keys=['career_seasons','super_bowl_appearances','super_bowl_wins','season_start','season_end']
    if any(type(record.get(k)) is not int for k in keys):raise ValueError('Métricas devem ser inteiros')
    seasons=record['career_seasons'];appearances=record['super_bowl_appearances'];wins=record['super_bowl_wins']
    if not 0<=wins<=appearances<=seasons or seasons<=0:raise ValueError('Totais históricos inconsistentes')
    if seasons!=record['season_end']-record['season_start']+1:raise ValueError('Período inconsistente')
    if not record.get('source_url','').startswith('https://'):raise ValueError('Fonte ausente')
    return {'player':record['player'],'career_seasons':seasons,'super_bowl_appearances':appearances,'super_bowl_wins':wins,
            'appearance_share_of_career_seasons':appearances/seasons,'win_share_of_super_bowl_appearances':wins/appearances if appearances else None,
            'source_url':record['source_url'],'scope':record['scope'],
            'interpretation':'Proporções descritivas do histórico; não são probabilidades de sucesso futuro nem medida causal de contribuição individual.'}

def run(input_path=ROOT/'data/career_summary.json',output=ROOT/'artifacts'):
    result=analyze(json.loads(Path(input_path).read_text()));output=Path(output);output.mkdir(parents=True,exist_ok=True)
    (output/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2));return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=ROOT/'data/career_summary.json');p.add_argument('--output',type=Path,default=ROOT/'artifacts');a=p.parse_args();run(a.input,a.output)
