import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json



BASE_URL = 'https://pje1gconsulta.tjrn.jus.br'

URL = f'{BASE_URL}/consultapublica/ConsultaPublica/listView.seam'
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver  =  webdriver.Firefox(options=options)


driver.get(URL)

cpf_box = driver.find_element(by=By.NAME, value="fPP:dpDec:documentoParte")
cpf_box.send_keys('111.111.111-11')
botao = driver.find_element(by=By.NAME, value="fPP:searchProcessos")
botao.click()


time.sleep(5)

tag_b = driver.find_elements(By.CSS_SELECTOR, "b.btn-block")
lista_a = []
for b in tag_b:
    a = b.find_element(By.XPATH, "..")
    lista_a.append(a)

url = re.search(r"'/consultapublica/[^']+\'", lista_a[3].get_attribute("onclick"))

if url:
    url = url.group(0).strip("'")

requisicao = requests.get(f'{BASE_URL}{url}')


data = {
    "partes":{},
    "movimentacoes":{}
}

soup = BeautifulSoup(requisicao.text, 'html.parser')


partes_envolvidas = soup.select('td.rich-table-cell > span > div > span.text-bold')     #find(class_="rich-table-cell")
movimentacoes = soup.select('td.text-left', limit=5)

if partes_envolvidas:
    for index, elemento in enumerate(partes_envolvidas):
        texto_desejado = elemento.text
        data["partes"][f"participante{index+1}"] = texto_desejado

if movimentacoes:
    for index, movimento in enumerate(movimentacoes):
        texto = movimento.text
        data["movimentacoes"][f"movimento{index+1}"] = texto
        
print(data)


json_string = json.dumps(data, indent=4, ensure_ascii=False)  # indent para formatar o JSON com recuo

# Especifique o nome do arquivo onde deseja salvar o JSON
nome_do_arquivo = "dados.json"

# Salve a string JSON em um arquivo
with open(nome_do_arquivo, "w") as arquivo_json:
    arquivo_json.write(json_string)



