from record import Record
from time import sleep
import datetime
import os

os.system("cls")

with open("DadosBrutos.txt", "r") as dados:
    dados_brutos = dados.readlines()

for list_linha in dados_brutos:
    linha = list_linha.split()
    timedate = f"{linha[0]} {linha[1]}"
    value = linha[-1].replace("%", "")
    id_sensor = '23'
    unit = '%'
    update_record = Record(timedate, value, id_sensor, unit)
    
    if(update_record.update()):
        print('Record inserido com sucesso.')
    else:
        print('Falha ao adicionar Record')
    
    sleep(.5)
    with open("DadosSalvos.txt", "a") as dados_salvos:
        dados_salvos.write(list_linha)
    now = datetime.datetime.now()  
    t = now.strftime("%d/%m/%Y %H:%M:%S")
    print("DadosSalvos.txt atualizado: " + t)