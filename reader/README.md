# Leitor do Distrito 41

Na raiz do repositório, dê dois cliques em `ler-distrito41.cmd` (o atalho antigo `ler-caso-001.cmd` também funciona). O navegador abre automaticamente. Alternativamente:

```powershell
python scripts/read_book.py
```

Abra http://127.0.0.1:8041. Para encerrar, use Ctrl+C no terminal. Se a porta estiver ocupada: `python scripts/read_book.py --port 8042`.

O leitor oferece páginas animadas, índice, ajuste de fonte, modo noturno, leitura contínua e retomada automática da posição. Use as setas do teclado, os botões ou arraste os cantos. Em telas estreitas, o livro mostra uma página por vez. A preferência de movimento reduzido do sistema é respeitada.

Os capítulos são lidos de `main/casos/`, em ordem de nome, no formato `NN-titulo.md`. Enquanto não houver texto novo, o leitor informa que o projeto está em preparação. Atualize a página após editar o manuscrito ou adicionar um capítulo. A posição é salva no navegador por capítulo e trecho; edições grandes podem deslocar o ponto de retomada.

Não precisa de Node, instalação de pacotes nem conexão com a internet para ler: o servidor usa somente a biblioteca padrão do Python, e a biblioteca de animação está incluída. O servidor escuta apenas em `127.0.0.1` e serve exclusivamente os recursos desta pasta e o texto dos capítulos. Não consulta APIs do jogo.

## Biblioteca de animação

[StPageFlip, de Nodlik](https://github.com/Nodlik/StPageFlip), pacote `page-flip` **2.0.7**, licença MIT preservada em [vendor/LICENSE](vendor/LICENSE). Bundle obtido de `https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.js`. A paginação, o leitor e o servidor são específicos deste repositório.

## Verificação opcional

Com o servidor funcionando, `python tests/check_reader_browser.py` confere em Chromium a preservação integral do texto, ausência de transbordamento, navegação, ajustes, retomada e layout móvel. Apenas essa verificação exige `playwright` e seu Chromium: `python -m pip install playwright` e `python -m playwright install chromium`.
