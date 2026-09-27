# Contexto da guerra: Fac7ion e GiuGiu

Apuração de 26/09/2026 para enriquecer o Distrito 41. Datas abaixo em UTC−3. Foram recuperados **21 artigos de Fac7ion e 48 de GiuGiu**, sem filtro de idioma, com paginação concluída. O catálogo inclui traduções e assuntos fora da guerra: são 69 publicações, não 69 relatos distintos. Foram lidos os textos relevantes para o período; imagens, quadrinhos e comentários não foram apurados.

## Arquivo e método

- [Arquivo de Fac7ion](../../data/warera/autores-20260926/Fac7ion/article.getArticlesPaginated.json), usuário `6a77ec7ac4249a39be79cea4`.
- [Arquivo de GiuGiu](../../data/warera/autores-20260926/GiuGiu/article.getArticlesPaginated.json), usuário `6a064ba2a072838902047d27`.
- Textos extraídos em `data/warera/autores-20260926/{Fac7ion,GiuGiu}/text/`. O JSON preserva o HTML original.
- Boletins brasileiros **5 a 11**, ligados pelos artigos de GiuGiu, preservados em `data/warera/autores-20260926/GiuGiu/boletins/`, com HTML, texto e metadados de origem. [Site público dos boletins](https://giugiu-br.github.io/BR-Boletim/).

A coleta usou exclusivamente **GET**: API2 pública para artigos e perfis, páginas públicas estáticas para os boletins. Nenhuma API3 ou superior. Não foi usado o endpoint de artigo completo que contabiliza visualizações. Os dados locais continuam ignorados pelo Git.

## O que acrescenta à narrativa

**Antes de Belém, já havia uma São Paulo defendida.** GiuGiu publicou em **13/08, 23h22** uma vitória brasileira por 2–1 em São Paulo. É um episódio anterior à batalha que abre o livro, distinto da posterior perda da região e da retomada de 23/08. Pode sustentar o contraste entre confiança inicial e desgaste, sem misturar as três batalhas. [Relato](https://app.warera.io/article/6a7e796eb04953350ab23868).

**O colapso tinha uma dimensão econômica vivida.** A sequência de Fac7ion acompanha frentes simultâneas, mercenários, perda de regiões, exaustão financeira e moral. Serve especialmente para a atmosfera de 14 a 22/08: notícias desencontradas, sensação de cerco e dificuldade de enxergar o quadro inteiro. Sua série mistura deliberadamente ficção e acontecimentos; falas, agentes secretos, cenas de banco e situações cômicas não devem virar registros históricos atribuídos a jogadores reais. [Episódio V](https://app.warera.io/article/6a80df660821752082f4f813), [VII](https://app.warera.io/article/6a83d56a96c06426d1fde2ea), [IX](https://app.warera.io/article/6a8a200836e26ed4611f8e1f).

**O ecomode também era apresentado como contribuição à guerra.** Em **21/08, 13h48**, GiuGiu pediu resistência militar, mas também contribuição econômica de quem não podia combater. É um contexto contemporâneo muito bom para a escolha de Harry de abandonar o warmode naquele dia e financiar mercenários. O artigo não documenta a decisão pessoal de Harry nem os valores de 2.000 e 200 moedas; esses continuam sendo testemunho do autor. [Ocupado, mas não acabado](https://app.warera.io/article/6a88814b6da00532d957339d).

**São Paulo abriu o caminho para Brasília.** O artigo publicado em **25/08, 22h02** associa a vitória paulista ao corte de passagem e à recuperação da capital, destacando Igor. Corrobora o contexto estratégico contado pelo autor. Não confirma participação pessoal de Harry nessa batalha; a correção sobre sua saída do warmode em 21/08 permanece válida. A publicação ocorreu depois da recuperação de Brasília, registrada às 02h08 de 25/08. [Brasília é nossa](https://app.warera.io/article/6a8e3b011296031db6862d48).

**A ajuda de Suriname e o trabalho de Braboss aparecem na imprensa.** GiuGiu descreve apoio surinamês à defesa de Brasília em **20/08, 00h02**, incluindo uma alegação de mais de 50 milhões de dano que ainda precisa de conferência por participantes da batalha. Em **26/08, 23h12**, registra o humor de Braboss junto de campanhas, doações e organização. Dá material para sua presença no livro além da festa de 25/09. [Suriname](https://app.warera.io/article/6a86693f9d715a83e0fb27d1), [Braboss](https://app.warera.io/article/6a8f9cc3af76e718c3d277b6).

**A crise de 20/09 saiu do bastidor.** GiuGiu publicou às **10h16** uma opinião sobre impeachment e discordâncias políticas. O Boletim 11 preserva uma transcrição de comunicado do governo: a recusa parlamentar em eliminar o front de Bissau teria mantido três batalhas simultâneas, aumentado os gastos e motivado um pedido de doações para pagar mercenários. Essa é uma ligação concreta entre diplomacia, Congresso, tesouro e front. A transcrição é preservada pelo boletim, não um original imutável recuperado da API; não documenta todos os termos da negociação. Harry esclareceu que **não houve processo de impeachment**: houve conversa informal no chat, revolta de alguns jogadores e posterior compreensão da posição de Staff. Segundo ele, manter a região implicava revoluções recorrentes e desperdício de recursos, com cerca de quatro a cinco fronts já exigindo atenção. A referência do comunicado a três batalhas simultâneas e a lembrança de quatro a cinco fronts têm escopos ou momentos possivelmente distintos; não uniformizar os números sem apuração. [Artigo](https://app.warera.io/article/6aafdcb340654a059f6f5c3c), [Boletim 11](https://giugiu-br.github.io/BR-Boletim/br-boletim-11.html).

## Divergências e perguntas abertas

- Fac7ion anuncia alguns resultados antes do encerramento registrado ou apresenta versões incompatíveis com outras fontes. O episódio IV, por exemplo, fala de devolução da Amazônia colombiana antes do horário final da batalha. Os horários da API prevalecem para resultados; o texto serve como retrato da informação que circulava.
- A alegação de silêncio governamental no episódio VIII precisa ser confrontada com comunicações de Rafael já presentes no arquivo. Não transformar uma crítica editorial em ausência factual de comunicação.
- Os textos genéricos de GiuGiu sobre não agressão ajudam a compreender sua posição diplomática, mas não provam a assinatura de tratados específicos.
- Os boletins apontam para a [batalha `6aa064b358bb5aaf58c178fd`](https://app.warera.io/battle/6aa064b358bb5aaf58c178fd). A API identifica Venezuela contra Guiné-Bissau, vitória venezuelana por 2–0 em **09/09, 05h00**. Existe também um evento de transferência entre Venezuela e Brasil em 15/09. **Harry corrigiu sua resposta anterior e confirmou a compra brasileira à Venezuela em 15/09 por um valor simbólico de 67 moedas.** O relato esclarece o campo `amount: 67` do evento e a origem da ocupação brasileira. [Consulta da batalha](../../data/warera/autores-20260926/bissau-conquest.json).

**La Paz foi uma operação econômica acordada.** Segundo Harry, o Brasil alugou a região boliviana pelo recurso natural local e atacou para efetivar esse controle. A batalha de 07 a 08/09 não deve ser narrada como evidência de ruptura diplomática. O recurso específico e as condições do aluguel ainda precisam ser esclarecidos.

## Como usar na escrita

A espinha cronológica já permite avançar. A pesquisa adicional deve acompanhar cada capítulo: conferir a batalha retratada, ler as notícias publicadas naquele momento e perguntar ao autor pelos bastidores que não aparecem nos registros. Fac7ion ajuda sobretudo com a experiência pública do caos; GiuGiu acrescenta comunicados, mobilização econômica e debates políticos. A ficção pode dar corpo a essas experiências sem copiar suas invenções como fatos.

## Catálogo das publicações recuperadas

Datas são de publicação, não necessariamente do acontecimento. Traduções são mantidas para rastreabilidade.

### Fac7ion

- **11/08/2026 19:59**: [The War Behind the War - History (EN/PT)](https://app.warera.io/article/6a7ba95edfbc8ed903f0c1a4)
- **11/08/2026 20:52**: [The War Behind the War - History Part II (EN/PT)](https://app.warera.io/article/6a7bb5a3ebafa0c65b00994c)
- **12/08/2026 01:27**: [The War Behind the War - Comic (EN/PT)](https://app.warera.io/article/6a7bf62e4280ad120182658d)
- **12/08/2026 01:29**: [The War Behind the War - Comic Part II (EN/PT)](https://app.warera.io/article/6a7bf6a5b2ef4accf61c62be)
- **13/08/2026 19:48**: [The War Behind the War - Part III (Comic & History) (EN/PT)](https://app.warera.io/article/6a7e49b8ce6f4870aaba138d)
- **14/08/2026 23:48**: [The War Behind the War - Part IV (Comic & History) (EN/PT)](https://app.warera.io/article/6a7fd37e811a189b4650b32e)
- **15/08/2026 18:51**: [The War Behind the War - Part V (Comic & History) (EN/PT)](https://app.warera.io/article/6a80df660821752082f4f813)
- **16/08/2026 23:32**: [The War Behind the War - Part VI (Comic & History) (EN/PT)](https://app.warera.io/article/6a8272c459defd8b19e8f813)
- **18/08/2026 00:45**: [The War Behind the War - Part VII (Comic & History) (EN/PT)](https://app.warera.io/article/6a83d56a96c06426d1fde2ea)
- **20/08/2026 18:35**: [The War Behind the War - Part VIII (Comic & History) (EN/PT)](https://app.warera.io/article/6a8773208d14efa92d21e7bb)
- **22/08/2026 19:18**: [The War Behind the War - Part IX (Comic & History) (EN/PT)](https://app.warera.io/article/6a8a200836e26ed4611f8e1f)
- **22/08/2026 19:47**: [The War Behind the War - FINAL (Comic & History) (EN/PT)](https://app.warera.io/article/6a8a26f0af59d164a7b7f987)
- **04/09/2026 10:00**: [Minha Primeira Candidatura Oficial ao Congresso (PT)](https://app.warera.io/article/6a9ac0de7f8bfddf086be920)
- **05/09/2026 19:31**: [Um Simples Guia - De Um Iniciante Para Outro Iniciante (PT)](https://app.warera.io/article/6a9c9835785d640288ef324a)
- **06/09/2026 21:10**: [Discurso de Posse - Congressista do Brasil (PT)](https://app.warera.io/article/6a9e00ebf550de360d551d48)
- **07/09/2026 16:30**: [GAZETA DA AMÉRICA LATINA: 7 de Setembro (PT)](https://app.warera.io/article/6a9f10ca516c2d7babd93268)
- **07/09/2026 16:34**: [GACETA DE AMÉRICA LATINA: 7 de Septiembre (ES)](https://app.warera.io/article/6a9f11c745373e813c43dba9)
- **15/09/2026 14:30**: [Atualização v.026.0 (PT)](https://app.warera.io/article/6aa980bd96844a284b4d5e1d)
- **16/09/2026 09:35**: [Building the Future: Brazil's Limestone Revolution is Here. (EN)](https://app.warera.io/article/6aaa8d0e654c7d7585661d6f)
- **16/09/2026 09:39**: [Construyendo el Futuro: La Revolución del Limestone en Brasil ya está aquí. (ES)](https://app.warera.io/article/6aaa8e18e14a6ee51fea2f42)
- **16/09/2026 09:45**: [Construindo o Futuro: A Revolução do Calcário no Brasil começou. (PT)](https://app.warera.io/article/6aaa8f6932f4a42e7eb189e5)

### GiuGiu

- **05/07/2026 00:50**: [GIUGIU PARA O CONGRESSO BRASILEIRO](https://app.warera.io/article/6a49d4484779015c698c33b9)
- **14/07/2026 22:40**: [BR Boletim #1 (Protótipo)](https://app.warera.io/article/6a56e4c4e4bf313e78e6dcae)
- **17/07/2026 14:54**: [Qualified Majority does not require closing the vote](https://app.warera.io/article/6a5a6c5b20dcc85828adc47a)
- **18/07/2026 00:15**: [Entrar é Público. Sair Não.](https://app.warera.io/article/6a5aefb51078c16094245b6c)
- **18/07/2026 00:20**: [Unirse es Público. Irse No.](https://app.warera.io/article/6a5af0ea1e131ac760c0dc68)
- **18/07/2026 00:27**: [Joining Is Public. Leaving Isn't.](https://app.warera.io/article/6a5af2aeb01fb297518ee753)
- **18/07/2026 00:32**: [Der Beitritt ist Öffentlich. Der Austritt Nicht.](https://app.warera.io/article/6a5af3b2778a982b70b68fb6)
- **18/07/2026 00:34**: [Adhérer est Public. Partir Ne l'est Pas.](https://app.warera.io/article/6a5af44df1f62530c543cfbb)
- **19/07/2026 19:15**: [Se acaba la Era Messi, comienza la Era dorada de Yamal](https://app.warera.io/article/6a5d4c9a44d254e8716e284c)
- **20/07/2026 11:39**: [BR Boletim #2](https://app.warera.io/article/6a5e332be4c9a8ecef77ca48)
- **21/07/2026 11:10**: [O Futuro do PRB](https://app.warera.io/article/6a5f7dc91a45007e67422e09)
- **26/07/2026 21:02**: [NOTA OFICIAL DO PRB - ELEIÇÃO PRIMÁRIA](https://app.warera.io/article/6a66a02525cc3dc563afba55)
- **27/07/2026 00:16**: [BR Boletim #3](https://app.warera.io/article/6a66cd89b13243762938e4e2)
- **31/07/2026 15:14**: [Modus Operandi Petequinha](https://app.warera.io/article/6a6ce5febee4b521d0c3ad68)
- **03/08/2026 00:30**: [BR Boletim #4](https://app.warera.io/article/6a700b3b5b3ced106efcd864)
- **03/08/2026 18:55**: [Carta aberta ao candidato GabrielPang](https://app.warera.io/article/6a710e3434efdce30dac5bee)
- **04/08/2026 18:05**: [Congresso: Uma voz que continua](https://app.warera.io/article/6a725425d950f6985c867be0)
- **10/08/2026 00:10**: [BR Boletim #5](https://app.warera.io/article/6a794135e4445a1f24899a7c)
- **10/08/2026 22:22**: [Resposta ao Marx_Jorge_Jr](https://app.warera.io/article/6a7a7964f19996f8b4af2929)
- **11/08/2026 21:55**: [O BRASIL PRECISA DE VOCÊ NO WARMODE! - MCom](https://app.warera.io/article/6a7bc27b75f7e0a849031b65)
- **13/08/2026 01:38**: [A BATALHA DE WESTERN LIBERIA](https://app.warera.io/article/6a7d4a2d69124c83cc6f8905)
- **13/08/2026 01:55**: [THE BATTLE OF WESTERN LIBERIA](https://app.warera.io/article/6a7d4e438205c4e3796e30c9)
- **13/08/2026 02:03**: [LA BATALLA DE LIBERIA OCCIDENTAL](https://app.warera.io/article/6a7d501de07880820e6f47b9)
- **13/08/2026 23:22**: [SÃO PAULO RESISTIU!](https://app.warera.io/article/6a7e796eb04953350ab23868)
- **13/08/2026 23:22**: [SÃO PAULO STOOD STRONG!](https://app.warera.io/article/6a7e7a3f006a168bfe378c2e)
- **13/08/2026 23:23**: [¡SÃO PAULO RESISTIÓ!](https://app.warera.io/article/6a7e7bc261965ba14ea8a16d)
- **14/08/2026 23:03**: [BELÉM: UMA BATALHA PARA A HISTÓRIA](https://app.warera.io/article/6a7fc79f072639fe7a0e5e73)
- **14/08/2026 23:03**: [BELÉM: UNA BATALLA POR LA HISTORIA](https://app.warera.io/article/6a7fc81d361c685f653badfa)
- **14/08/2026 23:03**: [BELÉM: A BATTLE FOR HISTORY](https://app.warera.io/article/6a7fc8cdce6f4870aab60966)
- **16/08/2026 02:20**: [TRÊS FRONTS. UM SÓ BRASIL.](https://app.warera.io/article/6a8148a675f7e0a8490fbc26)
- **17/08/2026 00:24**: [BR Boletim #6](https://app.warera.io/article/6a827ee261965ba14e279b95)
- **17/08/2026 14:34**: [Mudança no Ministério da Defesa do Brasil](https://app.warera.io/article/6a834635e89f1e08f2f08a28)
- **20/08/2026 00:02**: [A ARMA SECRETA DO SURINAME](https://app.warera.io/article/6a86693f9d715a83e0fb27d1)
- **20/08/2026 15:35**: [Um PRB para os novos desafios](https://app.warera.io/article/6a8748d01867076b1564bcdb)
- **21/08/2026 13:48**: [OCUPADOS, MAS NÃO ACABADOS](https://app.warera.io/article/6a88814b6da00532d957339d)
- **24/08/2026 00:01**: [BR Boletim #7](https://app.warera.io/article/6a8bb4052c4f69d045779ae2)
- **25/08/2026 22:02**: [BRASÍLIA É NOSSA!](https://app.warera.io/article/6a8e3b011296031db6862d48)
- **26/08/2026 23:12**: [COM TODO RESPEITO, BRABOSS...](https://app.warera.io/article/6a8f9cc3af76e718c3d277b6)
- **27/08/2026 14:05**: [A NÃO arte de negociar um NAP](https://app.warera.io/article/6a906e6afc33e58cab0fbf7a)
- **27/08/2026 14:07**: [The NON-art of negotiating a NAP](https://app.warera.io/article/6a906d8c23ee88d06810c9d7)
- **27/08/2026 23:17**: [POSICIONAMENTO DO GOVERNO BRASILEIRO À CMB](https://app.warera.io/article/6a90efaad887a93c7fc9e423)
- **30/08/2026 16:14**: [NOTA OFICIAL ELEITORAL DO PRB](https://app.warera.io/article/6a947ce9cfeffe3638dc950d)
- **31/08/2026 00:38**: [BR Boletim #8](https://app.warera.io/article/6a94f7355b36fbefecb1f347)
- **06/09/2026 22:00**: [Aproveitando o feriado em Bons Ares](https://app.warera.io/article/6a9e082b437cae4d11c5243c)
- **07/09/2026 01:06**: [BR Boletim #9](https://app.warera.io/article/6a9e384e46a0179eb3b47390)
- **14/09/2026 00:19**: [BR Boletim #10](https://app.warera.io/article/6aa76778310b0dd9b53c0c2c)
- **20/09/2026 10:16**: [Processo de Impeachment](https://app.warera.io/article/6aafdcb340654a059f6f5c3c)
- **21/09/2026 00:01**: [BR Boletim #11](https://app.warera.io/article/6ab09de963f4be814385d6c8)
