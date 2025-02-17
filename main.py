from kivy.app import App
from kivy.uix.label import Label
import _thread as thread
from time import sleep
import requests
import _thread as thread
import os
import platform

def getIp():
  try:
    res = get(url="https://httpbin.org/ip")
    return res.text
  except:
    None

def changeMsg():
  try:
    sleep(7)
    MeuApp.main_label.text = "Mensagem alterada!"
  except:
    None

class MeuApp(App):
  msg = "Mensagem Padrão"
  main_label = Label(text=msg)
  def inicio(self):
    self.ip = getIp()
    sleep(4)
    return Label(text="Bem vindo de volta!")

  def build(self):
    try:
      return inicio(self)
    except:
      None

if __name__ == '__main__':
  thread.start_new_thread(changeMsg,())
  MeuApp().run()
