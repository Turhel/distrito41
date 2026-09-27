# Coleta pública do War Era

O coletor `scripts/collect_warera.py` usa Python 3 e somente a biblioteca padrão.
Leia a chave de `.env` (`WARERA_API_KEY=...`) ou da variável de ambiente homônima.
Não grava nem imprime a chave. `.env` e os dados coletados estão no `.gitignore`.

```powershell
python scripts/collect_warera.py --max-pages 15 --country-id 6813b6d546e731854c7ac82f
python -m unittest discover -s tests
```

O comando coleta os países, artigos em português, eventos e batalhas do Brasil.
Para outros idiomas, use `--languages pt en es fr`. O filtro de idioma não
equivale a um filtro de nacionalidade: artigos portugueses e de outros países
também podem aparecer. Sem `--country-id`, coleta apenas países e artigos.

Cada execução cria uma pasta UTC em `data/warera/`. Ela contém:

- `raw/`: respostas JSON com endpoint, parâmetros, URL e horário UTC de coleta.
- `countries.json`: fotografia dos países no momento da consulta.
- `article.getArticlesPaginated.json`: conteúdo HTML original e metadados dos artigos.
- `event.getEventsPaginated.json` e `battle.getBattles.json`: registros paginados.
- `manifest.json`: contagens e indicação de conclusão por coleção.

`complete: false` significa que o limite de páginas foi atingido; o cursor
seguinte fica salvo no arquivo agregado.

Para retomar uma coleta limitada ou interrompida, repita os mesmos filtros e
adicione `--output caminho/da/pasta`; coleções concluídas são preservadas e as
parciais continuam a partir do cursor salvo.

A coleta não promete recuperar itens
apagados, privados ou fora do histórico que a API disponibiliza. Datas dos
registros e horário de coleta são informações diferentes. Preserve os arquivos
brutos para fundamentar a cronologia e trate afirmações dos artigos como relatos
de seus autores, não como confirmação automática dos eventos.

## Restrição de leitura

Todas as requisições são GET, sem corpo, para `https://api2.warera.io/trpc/`.
Uma lista explícita de endpoints impede chamadas arbitrárias. Redirecionamentos
são recusados. Não há login por sessão, POST, mutações nem acesso a endpoints
privados. Usa `X-API-Key`, intervalo entre chamadas e tentativas limitadas para
429 e erros temporários do servidor.

A [documentação oficial](https://api2.warera.io/docs/) diz que as chamadas são
GET, apesar das etiquetas POST do Swagger. O esquema consultado está salvo em
`openapi.json`. `article.getArticleById` está excluído porque a documentação
indica contagem de visualização; a listagem já fornece o conteúdo dos artigos.
O endpoint lite é permitido, mas não é necessário para a coleta padrão.

Os arquivos antigos de crônicas não são alterados pelo coletor.
