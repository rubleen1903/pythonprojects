import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/tabs/tab1')
    data = r.json()
    text = f'Confirmed Cases : {data [ "cases"]}\n Deaths : {data["deaths"]} \n Recoveredv: {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=20)
        time.sleep(60)

update()