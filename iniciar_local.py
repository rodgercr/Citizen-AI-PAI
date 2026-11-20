"""Inicia apenas o aplicativo; a avaliacao completa fica no notebook."""
import json, os, time
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
notebook=json.loads(Path('1_Notebook_GS2026_2.ipynb').read_text(encoding='utf-8'))
contexto={'__name__':'__main__'}
for celula in notebook['cells']:
    if celula['cell_type']!='code': continue
    codigo=celula['source']
    if codigo.startswith('evidencias_guardrails='): break
    if codigo.startswith('NAO_SEI ='):
        codigo=codigo.split('demonstracoes_rag=')[0].split('demonstracoes_rag =')[0]
    if codigo.startswith('def obter_unidade'):
        codigo=codigo.split('# O trace mostra')[0]
    print('Preparando aplicativo...',flush=True)
    exec(compile(codigo,'notebook','exec'),contexto)
print('Abra http://127.0.0.1:7860 no navegador. Mantenha esta janela aberta.',flush=True)
try:
    while True: time.sleep(30)
except KeyboardInterrupt:
    contexto['demo'].close()
