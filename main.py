from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivy.core.clipboard import Clipboard
import os
import platform
import requests
import _thread as thread
import tool


class MainApp(MDApp):
	dialog = None
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		if os.path.exists("port_forwarding/tunwg"):
			return Builder.load_file("menu.kv")
		return Builder.load_file("alert.kv")
	
	def show_alert_dialog(self,txt,with_install=True,with_copy=False):
		if with_install:
			thread.start_new_thread(self.installer,())
		if with_copy:
			Clipboard.copy("http://127.0.0.1:7777/painel/index.html")
			#thread.start_new_thread(tool.startTool,())
		if not self.dialog:
			self.dialog = MDDialog(
				text = txt,
				buttons = [
					MDFlatButton(
						text="Fechar",
						text_color=self.theme_cls.primary_color,
						on_release=self.close_dialog
						),			
				])
				
		self.dialog.open()
		
		
	def close_dialog(self,obj):
		self.dialog.dismiss()
		
	def installer(self):
		os.system("mkdir port_forwarding 2> /dev/null")
		arch = platform.machine()
		if "aarch64" in arch:
			arch = "arm64"
		elif "armv" in arch:
			arch = "arm"
		elif "i686" in arch:
			arch = "i686"
		elif "x86_64" in arch:
			arch = "x86_64"
			
		print("my arch:",arch)
		
		url = "https://raw.githubusercontent.com/abq78/files3/refs/heads/main/tuns/tunwg-"+arch
		head = {"User-Agent":tool.ua}
		try:
			print("baixando ...")
			res = requests.get(url=url,headers=head)
			tunwg_file = open("port_forwarding/tunwg","ab")
			tunwg_file.write(res.content)
			tunwg_file.close()
			#os.sytem("cp /home/unk/tuns/tun_lubuntu/tunwg port_forwarding/tunwg")
			os.system("chmod 700 port_forwarding/tunwg")
			#thread.start_new_thread(tool.startTool,())
			if self.dialog:
				self.dialog.text = "Instalado com sucesso!"
		except Exception as e:
			print(e)
			if self.dialog:
				self.dialog.text = "Não foi possivel fazer a instalação!"
		print("FIM!")

MainApp().run()
