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
    sleep(5)
    MeuApp.msg = "Mensagem alterada!"
  except:
    None

class MeuApp(App):
  msg = "Mensagem Padrão"
  def inicio(self):
    self.ip = getIp()
    return Label(text="Inicio :"+self.msg)

  def first(self):
    try:
      return Label(text="First: "+self.msg)
    except:
      None

  def build(self):
    try:
      status = open("status.txt","r").read()
      return self.inicio()
    except:
      return self.install()

if __name__ == '__main__':
  thread.start_new_thread(changeMsg,())
  MeuApp().run()
