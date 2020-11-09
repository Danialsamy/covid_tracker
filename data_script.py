import os
import requests
import json
import time

#ad ogni avvio scarica i dati
def getData():
    os.system('cmd /c "curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json > dati.json"')

getData()
time.sleep(2) #aggiungere un controllo e togliere questa funzione
data = json.load(open("dati.json"))


# ritorna i valori sotto forma di stringa
def data_giornaliera():
    for i in data:
        return(i['data'])
def casi_totali():
    for i in data:
        return(i['totale_casi'])
def nuovi_casi():
    for i in data:
        return(i['nuovi_positivi'])
def variazione_positivi():
    for i in data:
        return(i['variazione_totale_positivi'])
def deceduti():
    for i in data:
        return(i['deceduti'])
def tamponi_effettuati():
    for i in data:
        return(i['tamponi'])
def ricoverati():
    for i in data:
        return(i['ricoverati_con_sintomi'])
def terapia_intensiva():
    for i in data:
        return(i['terapia_intensiva'])
def isolamento_domiciliare():
    for i in data:
        return(i['isolamento_domiciliare'])
def guariti():
    for i in data:
        return(i['dimessi_guariti'])
def ricoverati_con_sintomi():
	for i in data:
		return(i['ricoverati_con_sintomi'])
def totale_positivi():
	for i in data:
		return(i['totale_positivi'])

 #fine programma

