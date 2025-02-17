from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
import webbrowser
from jnius import autoclass
#This example is made in Pydroid3

Intent = autoclass("android.content.Intent")
#String = autoclass("java.lang.String")
Activity = autoclass('org.kivy.android.PythonActivity').mActivity


hola = Activity #Activity class object


# if you do it like this: hello = Activity () you will be calling the constructor which will give an error
def op():
  paquete = hola.getPackageManager().getLaunchIntentForPackage("com.db.adm")
  paquete.addCategory(Intent.CATEGORY_LAUNCHER)
  Activity.startActivity(paquete)

class MeuApp(App):
  def build(self):
    try:
      return Button(text="tudo certo",on_press=op)
    except:
      None
  def open_url():
    webbrowser.open("https://google.com")

if __name__ == '__main__':
    MeuApp().run()
