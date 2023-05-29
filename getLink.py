from datetime import datetime
import shutil
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd, glob, time
import os, sys
from zipfile import ZipFile
from dateutil.parser import parse



url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
url = 'http://200.152.38.155/CNPJ/'
destination_directory = 'dados-publicos-zip' # Diretório de destino para salvar os arquivos
destination_unzip = 'dados-publicos' #Diretório de destino descompactados
arquivos_zip = list(glob.glob(os.path.join(destination_directory,r'*.zip')))
arquivos_unzip = list(glob.glob(os.path.join(destination_unzip,r'*.EMPRECSV')))
count = 0
countador = 0

if not os.path.exists(destination_directory):     #Verifica se pasta já existe.
    os.makedirs(destination_directory)
else:
    shutil.rmtree("dados-publicos-zip")
    os.makedirs(destination_directory)

    

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
nomes = []
datas = []
lista_objeto = []



def verifica_data(string_data):
        teste = string_data[0:10]
        formato_data = "%Y-%m-%d"
        try:
            datetime.strptime(teste, formato_data)
            return True
        except ValueError:
            return False
        





for link in soup.find_all('a'): #download .zip empresa
    print(link)
    href = link.get('href')
    if href and 'empresas' in href.lower():
        for teste in soup.find_all(align="right"):
            if(verifica_data(teste.string)):
             datas.append(teste.string[0:10])
        for index,link in enumerate(soup.find_all('a')): #download .zip empresa
            nome = link.string
            if "Empresas" in nome or "Estabelecimentos" in nome:
                lista_objeto.append({"Nome":nome,"Data":datas[index-5]})

        if not href.startswith('http'):
            download_url = url + href
            print("Iniciando Download")
        else:
            download_url = href
            print("Download Fail")

        response = requests.get(download_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        progress_size = 0
        print(lista_objeto)
        if response.status_code == 200:
            filename = download_url.split('/')[-1]
            file_path = os.path.join(destination_directory, filename)
            with open(file_path, 'wb') as file:
                for dados in response.iter_content(chunk_size=1024):
                    file.write(dados)
                    progress_size += len(dados)
                    percentual = (progress_size / total_size) * 100
                    # print(f"Progresso:  {percentual:.2f}%")
            print(f"Arquivo '{filename}' baixado com sucesso.")
            print(time.asctime(), 'descompactando ' + filename)
            filelocal = os.path.join(destination_directory, filename)
            with ZipFile(filelocal, 'r') as zip_ref:
                zip_ref.extractall(destination_unzip)
                lista = zip_ref.namelist()
                for index,file in enumerate(os.listdir(destination_unzip)):
                        if file == lista[0]:
                            filerename = os.path.join(destination_unzip, file)
                            new_name = f'{filename.split(".")[0]}_{lista_objeto[index].get("Data", "")}.CSV'
                            new_name_path = os.path.join(destination_unzip, new_name)
                            os.rename(filerename, new_name_path)
                            print(f"Arquivo renomeado: {file} -> {new_name}")
                            break  # Para o loop após renomear um arquivo
        else:
            print(f"Falha ao descompactar o arquivo '{download_url}'.")


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
                lista = zip_ref.namelist()
                for file in os.listdir(destination_unzip):
                        if file == lista[0]:
                            filerename = os.path.join(destination_unzip, file)
                            new_name = f'{filename.split(".")[0]}_.CSV'
                            new_name_path = os.path.join(destination_unzip, new_name)
                            os.rename(filerename, new_name_path)
                            print(f"Arquivo renomeado: {file} -> {new_name}")
                            break  # Para o loop após renomear um arquivo         
        else:
            print(f"Falha ao descompactar o arquivo '{download_url}'.")




                                # comando para colocar no código
        #         for teste in soup.find_all(align="right"):
        #      if(verifica_data(teste.string)):
        #          datas.append(teste.string)
        #          print(teste.string)
        # for index,link in enumerate(soup.find_all('a')): #download .zip empresa
        #         nome = link.string
        #         if "Empresas" in nome or "Estabelecimentos" in nome:
        #             lista_objeto.append({"Nome":nome,"Data":datas[index-5]})