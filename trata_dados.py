from record import Record
from time import sleep
import datetime
import os

os.system("cls")

with open("DadosBrutos.txt", "r") as dados:
    dados_brutos = dados.readlines()

list_records = []

for list_linha in dados_brutos:
    linha = list_linha.split()
    timedate = f"{linha[0]} {linha[1]}"
    value = linha[-1].replace("%", "")
    id_sensor = '23'
    unit = '%'
    record = Record(timedate, value, id_sensor, unit)
    list_records.append(record.obj)


if(record.update(list_records)):
    print('Records inserido com sucesso.')
else:
    print('Falha ao adicionar Records')
