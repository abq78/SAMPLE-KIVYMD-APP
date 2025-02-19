from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
from requests import get
from kivy.core.clipboard import Clipboard

class MeuApp(App):
  def copiar(self):
    Clipboard.copy("http://127.0.0.1:7777/painel/index.html")
    return False
  def build(self):
    try:
      return Button(text="Clique aqui para copiar (http://127.0.0.1:7777/painel/index.html)",on_press=self.copiar)
    except:
      None

if __name__ == '__main__':
    MeuApp().run()
