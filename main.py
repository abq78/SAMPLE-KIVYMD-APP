from kivy.app import App
from kivy.uix.button import Button
import _thread as thread
from time import sleep
from requests import get
from kivy.core.clipboard import Clipboard

class MeuApp(App):
	def copiar(self):
		Clipboard.copy("hahahaha")
		
	def build(self):
		try:
			return Button(text="copiar",on_press=self.copiar)
		except Exception as e:
			print(e)
	
if __name__ == '__main__':
	MeuApp().run()
