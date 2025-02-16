from kivy.app import App
from kivy.uix.button import Button
from time import sleep
from requests import get

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
    req()
    MeuApp().run()
