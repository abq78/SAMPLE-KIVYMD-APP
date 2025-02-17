from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
import webbrowser

class MeuApp(App):
  def build(self):
    try:
      return Button(text="tudo certo",on_press=self.open_url)
    except:
      None
  def open_url():
    webbrowser.open("https://google.com")

if __name__ == '__main__':
    MeuApp().run()
