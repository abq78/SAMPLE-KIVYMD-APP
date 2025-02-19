from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
import requests
from kivy.core.clipboard import Clipboard
import tool

class MeuApp(App):
  def copiar(self,obj):
    Clipboard.copy("http://127.0.0.1:7777/painel/index.html")
    return False
 
  def rodar(self,obj):
  	thread.start_new_thread(tool.startTool,())
 
  def build(self):
    try:
      return Button(text="Clique aqui para copiar (http://127.0.0.1:7777/painel/index.html)",on_press=self.rodar)
    except:
      None

if __name__ == '__main__':
    MeuApp().run()
