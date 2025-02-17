from kivy.app import App
from kivy.uix.label import Label
import _thread as thread
from time import sleep
import requests
import _thread as thread
import os
import platform
from pyjnius import autoclass

def open_url(url):
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    browserIntent = Intent()
    browserIntent.setAction(Intent.ACTION_VIEW)
    browserIntent.setData(Uri.parse(url))
    currentActivity = cast('android.app.Activity', mActivity)
    currentActivity.startActivity(browserIntent)


class MeuApp(App):
  def inicio(self):
    return Label(text="Bem vindo de volta!")

  def build(self):
    try:
      return inicio(self)
    except:
      None

if __name__ == '__main__':
  open_url("https://google.com")
  MeuApp().run()
