from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import re
import time
import pandas as pd
import numpy as np
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

ua = UserAgent()
headers = {'User-Agent': ua.chrome}
response = requests.get(url, headers=headers) # evitar el error 403

service = Service(executable_path= "chromedriver.exe")
options = webdriver.ChromeOptions() # ajustes para posteriormente poder acceder a chrome

driver = webdriver.Chrome(service=service, options=options) # abrir chrome
driver.get(url) # abrir la página de imdb

all_li = driver.find_elements(By.CLASS_NAME, "sc-f30335b4-0.eefKuM.cli-children") # sacar el o los divs donde están todos los datos

# diferentes bucles for para sacar los datos:
#   este primero solo para sacar una lista con titulo y posición
lista = []
for x in all_li:
    lista.append(x.find_element(By.CLASS_NAME, "ipc-title__text").text)

#   este segundo para dividir los valores de la primera lista y añadirlo en forma de sublista a otra lista
sublista = []
for y in lista:
    sublista.append(y.split(". ", 1))

#   este para añadir los valores de las sublistas a las listas de "top" y "titulo"
top = [] 
titulo = []
for valor in sublista:
    top.append(valor[0])
    titulo.append(valor[1])

#   el siguiente para sacar una lista con sublistas en las que se encuentran los valores de año y duración
año_duracion = []
for y in all_li:
    año_duracion.append(y.find_elements(By.CLASS_NAME, "sc-f30335b4-7.jhjEEd.cli-title-metadata-item")) 

#   esta penúltima para sacar los textos de cada cadena en las sublistas y añadirlos a "año" y "duracion"
año = []
duracion = []
for w in año_duracion:
    año.append(w[0].text)
    duracion.append(w[1].text)

# este último para buscar y añadir los valores de puntuación
puntuacion = []
for z in all_li:
    puntuacion.append(z.find_element(By.CLASS_NAME, "ipc-rating-star--rating").text) 

# creación del dataframe
top250 = pd.DataFrame({"Top": top, "Título": titulo, "Año": año, "Duración": duracion, "Puntuación": puntuacion})

# convertirlo en un csv llamado TOP250
top250.to_csv("TOP250.csv")