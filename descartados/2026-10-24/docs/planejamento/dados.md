# Dados para o planejamento

Ferramenta local, sem API ou acesso ao jogo. A regra proposta é **2d6 + modificador**: até 6, falha; 7–9, resultado parcial; 10 ou mais, sucesso. Sem modificador: 15/36 falha, 15/36 parcial, 6/36 sucesso. Não há crítico automático. Alterar a regra, se necessário, antes de decidir um obstáculo.

Antes de rolar, escrever num JSON: id único, cena, objetivo, obstáculo, categoria e as três consequências. Modificadores de −3 a +3 precisam de justificativa. Não há ficha definitiva de Harry; não inventar bônus depois de ver os dados.

```powershell
python scripts/rolar_dados.py docs/planejamento/exemplo-obstaculo.json --validar
python scripts/rolar_dados.py docs/planejamento/exemplo-obstaculo.json --simular
```

O exemplo é apenas demonstração. Criar um JSON próprio para cada obstáculo aprovado. Para uma rolagem narrativa, executar sem as duas opções: o resultado, os dados e o plano integral ficam em `docs/planejamento/rolagens/<id>.json`. O mesmo id não pode ser rolado novamente. `--simular` não registra e nunca vale como decisão do livro. Os registros são editáveis como qualquer arquivo local; não são um sistema antifraude. Não apagar resultados desfavoráveis ou mudar de id para repetir uma tentativa igual.

## O que o dado pode decidir

Pode determinar se uma abordagem funciona, se a pista é obtida agora, se exige outra diligência, se um vínculo se desgasta ou se uma oportunidade se perde. A falha precisa ter efeito real; pistas secundárias podem não ser obtidas. Para pistas indispensáveis, prever uma rota alternativa plausível, sem oferecer automaticamente a mesma informação de graça.

O dado não muda o passado, a identidade do responsável, o conteúdo verdadeiro de um depoimento, batalhas reais ou a inteligência das pessoas. Um sucesso em entrevista não obriga alguém a contar algo que não sabe; uma falha não transforma um inocente em culpado. Não rolar tarefas rotineiras sem incerteza relevante. O sorteio da solução do caso é separado e continua pendente de alternativas e probabilidades definidas.

Variar obstáculos por necessidade da cena: localização de uma pessoa, reconstituição temporal, acesso legítimo a um documento, confiança, interpretação de uma evidência, conflito de agenda. Consultar o histórico antes de repetir a categoria. Não usar continuamente testemunhas hostis, arquivos perdidos, chuva ou respostas enigmáticas.

Cada resultado precisa caber no calendário. Custo de horas, dias, deslocamento ou relação deve ser definido no plano quando relevante; não deixar o dado adiar fatos fixos. Após a rolagem, registrar no planejamento como a consequência foi incorporada.
