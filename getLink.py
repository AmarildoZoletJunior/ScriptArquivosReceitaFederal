import requests
import os
from bs4 import BeautifulSoup
import pandas as pd, glob, time
import os, sys
from zipfile import ZipFile



url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
url = 'http://200.152.38.155/CNPJ/'
destination_directory = 'dados-publicos-zip' # Diretório de destino para salvar os arquivos
destination_unzip = 'dados-publicos' #Diretório de destino descompactados
arquivos_zip = list(glob.glob(os.path.join(destination_directory,r'*.zip')))
arquivos_unzip = list(glob.glob(os.path.join(destination_unzip,r'*.EMPRECSV')))
count = 0
countador = 0

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'): #download .zip empresa
    href = link.get('href')
    if href and 'empresas' in href.lower():
        if not href.startswith('http'):
            download_url = url + href
            print("Iniciando Download")
        else:
            download_url = href
            print("Download Fail")

        response = requests.get(download_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        progress_size = 0

        if response.status_code == 200:
            filename = download_url.split('/')[-1]
            file_path = os.path.join(destination_directory, filename)
            with open(file_path, 'wb') as file:
                for dados in response.iter_content(chunk_size=1024):
                    file.write(dados)
                    progress_size += len(dados)
                    percentual = (progress_size / total_size) * 100
                    print(f"Progresso:  {percentual:.2f}%")
            print(f"Arquivo '{filename}' baixado com sucesso.")
            print(time.asctime(), 'descompactando ' + filename)
            filelocal = os.path.join(destination_directory, filename)
            with ZipFile(filelocal, 'r') as zip_ref:
                zip_ref.extractall(destination_unzip)         
        else:
            print(f"Falha ao baixar o arquivo '{download_url}'.")

filelocal = os.path.join(destination_directory, filename)
with ZipFile(filelocal, 'r') as zip_ref:
    zip_ref.extractall(destination_unzip)


    for count in range(10): 
        for file in os.listdir(destination_unzip):
            if file.endswith('.EMPRECSV'):
                filerename = os.path.join(destination_unzip, file)
                new_name = f'empresas{count}.CSV'
                new_name_path = os.path.join(destination_unzip, new_name)
                os.rename(filerename, new_name_path)
                print(f"Arquivo renomeado: {file} -> {new_name}")
                break  # Para o loop após renomear um arquivo
    count += 1


for link in soup.find_all('a'): #download .zip estabelecimento
    href = link.get('href')
    if href and 'estabelecimento' in href.lower():
        if not href.startswith('http'):
            download_url = url + href
            print("Iniciando Download")
        else:
            download_url = href
            print("Download Fail")

        response = requests.get(download_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        progress_size = 0

        if response.status_code == 200:
            filename = download_url.split('/')[-1]
            file_path = os.path.join(destination_directory, filename)
            with open(file_path, 'wb') as file:
                for dados in response.iter_content(chunk_size=1024):
                    file.write(dados)
                    progress_size += len(dados)
                    percentual = (progress_size / total_size) * 100
                    print(f"Progresso:  {percentual:.2f}%")
            print(f"Arquivo '{filename}' baixado com sucesso.")
            print(time.asctime(), 'descompactando ' + filename)
            filelocal = os.path.join(destination_directory, filename)
            with ZipFile(filelocal, 'r') as zip_ref:
                zip_ref.extractall(destination_unzip)         
        else:
            print(f"Falha ao baixar o arquivo '{download_url}'.")

filelocal = os.path.join(destination_directory, filename)
with ZipFile(filelocal, 'r') as zip_ref:
    zip_ref.extractall(destination_unzip)


    for count in range(10): 
        for file in os.listdir(destination_unzip):
            if file.endswith('.EMPRECSV'):
                filerename = os.path.join(destination_unzip, file)
                new_name = f'estabelecimentos{count}.CSV'
                new_name_path = os.path.join(destination_unzip, new_name)
                os.rename(filerename, new_name_path)
                print(f"Arquivo renomeado: {file} -> {new_name}")
                break  # Para o loop após renomear um arquivo
    count += 1