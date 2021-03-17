from tkinter import *
from tkinter import messagebox as mb
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Weather Snippet")
root.geometry('350x200')
root.resizable(False, False)

lbl = Label (root, text = "Digite o nome de uma cidade:")
lbl.grid(column=0, row=0)

txt = Entry (root, width = 20)
txt.grid(column=1, row=0)

label_location_text = StringVar()
lbl_location = Label (root, textvariable=label_location_text )
lbl_location.grid(column=0, row=1)

label_temperature_text = StringVar()
lbl_temperature = Label (root, textvariable=label_temperature_text)
lbl_temperature .grid(column=0, row=2)

label_weather_text = StringVar()
lbl_weather= Label (root, textvariable=label_weather_text)
lbl_weather.grid(column=0, row=3)

def clicked():

        try:

            city_input = str(txt.get())
            url = f'https://google.com/search?q=weather {city_input}'
            r = requests.get(url)
            s = BeautifulSoup(r.text, 'html.parser')

            location = s.find('span', class_='BNeawe').text
            weather = s.find('div', class_='BNeawe tAd8D AP7Wnd').text
            temperature = s.find('div', class_='BNeawe').text

            label_location_text.set(location)
            label_weather_text.set(weather)
            label_temperature_text.set(temperature)

        except:

            mb.showerror("Erro! :(", "Digite um nome válido!")


btn = Button(root, text = "Buscar", command=clicked)
btn.grid (column=1, row=2)


mainloop()
