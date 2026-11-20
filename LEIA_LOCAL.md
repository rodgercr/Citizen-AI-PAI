# Executar no computador

Esta alternativa usa Ollama local com `qwen2.5:7b`, após a Ollama Cloud recusar chamadas com erro 402. Não precisa de chave nem de créditos. A troca foi solicitada pela dupla e não comprova o requisito de execução no Colab com Ollama Cloud.

Neste computador, abra `ABRIR_NESTE_PC.cmd` e aguarde aparecer o endereço `http://127.0.0.1:7860`. Mantenha a janela aberta enquanto usa o aplicativo. Se a interface já estiver funcionando, não abra outra instância.

Em outro computador, instale Python 3.11 e Ollama, baixe o modelo com `ollama pull qwen2.5:7b`, crie um ambiente Python, instale `requirements.txt` e execute `python iniciar_local.py`. O arquivo `.cmd` usa o ambiente já preparado no computador de Rodger e não é portátil.

Para reproduzir todas as evidências, execute `1_Notebook_GS2026_2.ipynb` em Jupyter com o mesmo ambiente Python e a pasta `2_base_documental` ao lado. O notebook também executa as oito perguntas do RAGAS. O aplicativo isolado não repete a avaliação a cada abertura.

O juiz da avaliação também é `qwen2.5:7b` local. As métricas são resultados desse juiz pequeno, não equivalem às de um juiz forte. Valores ausentes permanecem nulos; não são substituídos por notas inventadas.
