
# Debug Error Message Sorter

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este script em Python é responsável por ler um arquivo de entrada contendo erros e classificar os documentos correspondentes a cada tipo de erro. Os documentos separados por tipo de erro são salvos em um arquivo de saída.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. O script foi desenvolvido e testado usando o Python 3.

## Utilização

1. Coloque o arquivo de entrada contendo os erros no diretório `data` com o nome `Erros.txt`.
2. Execute o script `sorter.py` a partir da linha de comando ou de sua IDE preferida.
3. O script irá ler o arquivo de entrada, classificar os documentos e salvar o resultado no arquivo `output.txt` no diretório `data`.
4. Verifique o arquivo de saída para obter os documentos separados por tipo de erro e o total de arquivos com erro.

## Exemplo de entrada

O arquivo de entrada `Erros.txt` deve ter o seguinte formato:

```
1 - documento (1).pdf
Não foi detectado o tipo de comprovante. Verifique o documento
2 - documento (2).pdf
Não foi detectado o tipo de comprovante. Verifique o documento
3 - documento (3).pdf
Não foi detectado o tipo de comprovante. Verifique o documento
...
11 - documento (11).pdf
translation-not-found[Internal Server Error]
...
```

## Exemplo de saída

O arquivo de saída `output.txt` terá o seguinte formato:

```
Tipo de Erro Não foi detectado o tipo de comprovante. Verifique o documento:
"Não foi detectado o tipo de comprovante. Verifique o documento"
Arquivos:
- 1 - 1 - documento (1).pdf
- 2 - 2 - documento (2).pdf
- 3 - 3 - documento (3).pdf
...

===================================================================================

Tipo de Erro translation-not-found[Internal Server Error]:
"translation-not-found[Internal Server Error]"
Arquivos:
- 1 - 11 - documento (11).pdf

...

===================================================================================

Total de arquivos com erro: 50

===================================================================================
```

Certifique-se de preencher o arquivo de entrada com os erros apropriados antes de executar o script.

## Autor

* Thiago da Silveira Gentil

