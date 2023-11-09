# Web Scrapping Judicial - Busca de Processos por CPF/CNPJ

Este é um script Python que permite a busca de processos judiciais por CPF ou CNPJ. Ele utiliza as seguintes bibliotecas:

- `selenium`: Para automação da interação com a página web.
- `requests`: Para fazer requisições HTTP ao site.
- `BeautifulSoup`: Para fazer o parsing do HTML da página.

## Pré-Requisitos

Antes de executar o script, certifique-se de instalar as dependências necessárias. Você pode fazer isso executando o seguinte comando:

```
pip install -r requeriments.txt
```

O arquivo `requeriments.txt` contém as bibliotecas necessárias.

## Uso

Para usar o script:

1. Certifique-se de ter o WebDriver do Mozilla Firefox. Você pode baixá-lo em [GeckoDriver](https://github.com/mozilla/geckodriver).

2. Execute o script.

3. O script automatiza a busca por processos judiciais. Você pode personalizar a entrada (CPF ou CNPJ) e a URL de destino conforme necessário.

4. Os dados do processo encontrado serão extraídos e salvos em um arquivo JSON chamado "dados.json".
