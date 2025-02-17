from kivy.app import App
from kivy.uix.label import Label
import _thread as thread
from time import sleep
from requests import get
import _thread as thread

def getIp():
  try:
    res = get(url="https://httpbin.org/ip")
    return res.text
  except:
    None

class MeuApp(App):
  def inicio(self):
    self.ip = getIp()
    return Label(text="Ja ta instalado. IP: "+self.ip)

  def install(self):
    self.ip = getIp()
    open("status.txt","a")
    return Label(text="IP: "+self.ip)

  def build(self):
    try:
      status = open("status.txt","r").read()
      return self.inicio()
    except:
      return self.install()
if __name__ == '__main__':
    MeuApp().run()
