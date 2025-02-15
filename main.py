from kivy.app import App
from kivy.uix.button import Button
from requests import get
from time import sleep
import threading

class MeuApp(App):
    def build(self):
        return Button(text="Olá, Mundo!")

def req():
    while 1:
        try:
            sleep(3)
            response = get('http://localhost:8080/soueu')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    thread = threading.Thread(target=req)
    thread.daemon = True
    # Inicia a thread
    thread.start()
    # Espera pela thread terminar
    print("Thread principal finalizada")

    MeuApp().run()
