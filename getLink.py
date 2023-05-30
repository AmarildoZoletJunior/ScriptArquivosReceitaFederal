from datetime import datetime
import shutil
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd,glob,time
from zipfile import ZipFile
from dateutil.parser import parse


#Variáveis
url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
url = 'http://200.152.38.155/CNPJ/'
destination_directory = 'dados-publicos-zip' # Diretório de destino para salvar os arquivos
destination_unzip = 'dados-publicos' #Diretório de destino descompactados
datas = []
lista_objeto = []
#Final variáveis


#Busca o html
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
#Final busca textos do html




##Função para baixar um arquivo
def GerarArquivoEDescompactar(link,nomeArquivo,tipo):
        href = link.get('href')
        if href and tipo in href.lower():
            if not href.startswith('http'):
                download_url = url + nomeArquivo
                print(nomeArquivo)
                print("Iniciando Download")
            else:
                download_url = nomeArquivo
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
                        # print(f"Progresso:  {percentual:.2f}%")
                print(f"Arquivo '{filename}' baixado com sucesso.")
                print('descompactando ' + filename)
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
#Final função





def verificar_pastas():
    if not os.path.exists(destination_directory):    #Verifica se pasta já existe.
        os.makedirs(destination_directory)

    if not os.path.exists(destination_unzip):#Verifica se pasta já existe.
        os.makedirs(destination_unzip)

def limpar_pastas():
    shutil.rmtree(destination_directory)
    verificar_pastas()
    

#Função que seleciona somente as datas, tirando tudo que não for data.
def verifica_data(string_data):
        teste = string_data[0:10]
        formato_data = "%Y-%m-%d"
        try:
            datetime.strptime(teste, formato_data)
            return True
        except ValueError:
            return False
#Final função  
        
        
#Popula a array de datas, colocando somente as datas disponíveis da lista
for teste in soup.find_all(align="right"):
    if(verifica_data(teste.string)):
             datas.append(teste.string[0:10])
#Final do for para popular um array de datas

#popula tabela com data e nome, pegando do array que foi populada no outro for
for index,link in enumerate(soup.find_all('a')): #download .zip empresa
    nome = link.string
    if "Empresas" in nome or "Estabelecimentos" in nome:
                lista_objeto.append({"Nome":nome,"Data":datas[index-5]})
#Final do for de popular um array da lista de objetos













##################Inicio do script para baixar empresas###############################################

for link in soup.find_all('a'): #Busca os link do site em format html <a>
    verificar_pastas()
    nomeObjeto = ''
    href = link.get('href')
    if href and 'empresas' in href.lower(): #Busca o href dos arquivos
        for objeto in lista_objeto:  ##Inicia busca com base no que puxou do html
            if objeto['Nome'] == href: ##Liga o nome do objeto com o nome do href
                nomeObjeto = objeto #Atribui a uma variável
                ObjetoEncontrado = False
                for arquivo in os.listdir(destination_unzip): ##Inicia um for puxando os arquivos existentes na pasta de arquivos
                    if href.replace(".zip","") == arquivo.split("_")[0]: ##Busca somente o objeto(Lista_objeto) que tenha o nome igual do arquivo
                            DataObjetoLista = nomeObjeto['Data'].split("-") ##Cria um array que separa todas os numeros da data do objeto
                            DataArquivoSeparada = arquivo.split("_")[1].replace(".CSV","") ##Atribui o valor da data do arquivo da pasta
                            DataArquivoArray = DataArquivoSeparada.split("-") ##Cria um array que separa cada número da data do arquivo da pasta
                            if datetime(int(DataObjetoLista[0]),int(DataObjetoLista[1]),int(DataObjetoLista[2])) > datetime(int(DataArquivoArray[0]),int(DataArquivoArray[1]),int(DataArquivoArray[2])): ##Verifica se a data é maior que a outra
                                os.remove(os.path.join(destination_unzip, arquivo))
                                GerarArquivoEDescompactar(link,href,'empresas')
                                limpar_pastas()
                                ObjetoEncontrado = True
                                break
                            else:
                                ObjetoEncontrado = True
                                break
                if not ObjetoEncontrado:
                    GerarArquivoEDescompactar(link,href,'empresas')
                    limpar_pastas()
                break                
                    
###############################################Final de script de baixar##############################
                    
                    
##################Inicio do script para baixar Estabelecimentos###############################################

for link in soup.find_all('a'): #Busca os link do site em format html <a>
    verificar_pastas()
    nomeObjeto = ''
    href = link.get('href')
    if href and 'estabelecimento' in href.lower(): #Busca o href dos arquivos
        for objeto in lista_objeto:  ##Inicia busca com base no que puxou do html
            if objeto['Nome'] == href: ##Liga o nome do objeto com o nome do href
                nomeObjeto = objeto #Atribui a uma variável
                ObjetoEncontrado = False
                for arquivo in os.listdir(destination_unzip): ##Inicia um for puxando os arquivos existentes na pasta de arquivos
                    if href.replace(".zip","") == arquivo.split("_")[0]: ##Busca somente o objeto(Lista_objeto) que tenha o nome igual do arquivo
                            DataObjetoLista = nomeObjeto['Data'].split("-") ##Cria um array que separa todas os numeros da data do objeto
                            DataArquivoSeparada = arquivo.split("_")[1].replace(".CSV","") ##Atribui o valor da data do arquivo da pasta
                            DataArquivoArray = DataArquivoSeparada.split("-") ##Cria um array que separa cada número da data do arquivo da pasta
                            if datetime(int(DataObjetoLista[0]),int(DataObjetoLista[1]),int(DataObjetoLista[2])) > datetime(int(DataArquivoArray[0]),int(DataArquivoArray[1]),int(DataArquivoArray[2])): ##Verifica se a data é maior que a outra
                                os.remove(os.path.join(destination_unzip, arquivo))
                                GerarArquivoEDescompactar(link,href,'estabelecimento')
                                limpar_pastas()
                                ObjetoEncontrado = True
                                break
                            else:
                                ObjetoEncontrado = True
                                break
                if not ObjetoEncontrado:
                    print(objeto)
                    GerarArquivoEDescompactar(link,href,'estabelecimento')
                    limpar_pastas()
                break  
            
            ###################################Fim###################