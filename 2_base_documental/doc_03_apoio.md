doc_id: DOC03
titulo: Nota de apoio ao atendimento e anexo operacional Aurora
data_publicacao: 2026-11-17
tema: atendimento municipal de vacinação fictícia

# Nota de apoio ao atendimento

A coordenação da campanha Aurora reúne nesta nota informações complementares para orientar os atendentes e facilitar o acesso à unidade CENTRO. O texto acompanha o regulamento inicial e o comunicado de alteração de funcionamento. Todos os dados pertencem ao município fictício de Vila Serena e devem ser usados apenas na demonstração acadêmica. Não são mantidas listas de pacientes, prontuários, endereços de moradores ou dados pessoais dos usuários.

Os cidadãos devem ser orientados com linguagem simples. O atendimento administrativo é gratuito e o chatbot não realiza inscrições, agendamentos ou confirmação de estoque. Para situações individuais de saúde, a equipe presencial é o canal adequado. A programação informada não garante disponibilidade de doses e não permite decidir indicação clínica. O assistente deve reconhecer quando não possui informação suficiente, em vez de completar lacunas com suposições.

Durante a manutenção, o acesso com rampa à unidade CENTRO ocorre exclusivamente pelo portão lateral da Travessa do Ipê, número 12. A entrada principal possui degraus. Esse acesso lateral funciona nos mesmos horários de atendimento da campanha e pode ser utilizado também por acompanhantes. Essa orientação de acessibilidade complementa os documentos anteriores e não muda a faixa etária de cada modalidade.

O anexo abaixo é a representação estruturada dos horários, publicada para conferência e cálculo pelos sistemas de atendimento. Até 17/11 vale a primeira regra; a partir de 18/11 vale a segunda. O limite final de uma janela é exclusivo para início de sessão. O cálculo deve considerar o horário informado pelo usuário e nunca prometer funcionamento fora do período documentado. Se a unidade estiver fechada, informar o fechamento sem substituir automaticamente a escolha do usuário.

```json
{"validade_inicio":"2026-11-01","validade_fim":"2026-11-30","intervalo_minutos":30,"unidades":{"NORTE":{"regras":[{"inicio":"2026-11-01","fim":"2026-11-17","dias":[0,1,2,3,4],"abre":"08:00","fecha":"18:00","idade_minima":18}],"fechada_desde":"2026-11-18"},"CENTRO":{"regras":[{"inicio":"2026-11-01","fim":"2026-11-17","dias":[0,1,2,3,4],"abre":"08:00","fecha":"18:00","idade_minima":18},{"inicio":"2026-11-18","fim":"2026-11-30","dias":[0,1,2,3,4],"abre":"09:00","fecha":"16:00","idade_minima":18},{"inicio":"2026-11-18","fim":"2026-11-30","dias":[5],"abre":"09:00","fecha":"12:00","idade_minima":60}]}}}
```
