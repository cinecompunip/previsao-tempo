import requests
from tkinter import *
from pathlib import Path
import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\biel1\PycharmProjects\PrevisaoTempo\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

API_KEY = "a408abbecea77d727f8b03d755aafde2"
cidade = "limeira"
lang = "pt_br"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang={lang}&appid={API_KEY}&units=metric"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = int(requisicao_dic['main']['temp'])
cidade = requisicao_dic['name']


DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

data = datetime.date.today()
indice_da_semana = data.weekday()
dia_da_semana = DIAS[indice_da_semana]


window = Tk()

window.title("Previsão do Tempo")
window.geometry("402x519")
window.configure(bg = "#2EB6D1")


canvas = Canvas(
    window,
    bg = "#2EB6D1",
    height = 519,
    width = 402,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    19.999999999999886,
    32.00000000000001,
    anchor="nw",
    text=dia_da_semana,
    fill="#FCFCFC",
    font=("Poppins Bold", 40 * -1)
)

canvas.create_text(
    19.999999999999886,
    102.0,
    anchor="nw",
    text=data,
    fill="#FFFFFF",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_rectangle(
    19.999999999999886,
    94.0,
    79.99999999999989,
    102.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    19.999999999999886,
    359.0,
    anchor="nw",
    text=f"{temperatura}°C",
    fill="#FCFCFC",
    font=("Poppins Bold", 64 * -1)
)

canvas.create_text(
    19.999999999999886,
    441.0,
    anchor="nw",
    text=descricao,
    fill="#FCFCFC",
    font=("Poppins Bold", 32 * -1)
)

canvas.create_text(
    19.999999999999886,
    137.0,
    anchor="nw",
    text=cidade,
    fill="#FFFFFF",
    font=("Poppins Bold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
