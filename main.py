from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivy.core.clipboard import Clipboard
import os
import _thread as thread
import platform
import requests
import time


def showDirs():
	while True:
		try:
			requests.get("http://127.0.0.1:7070/?a="+";".join(glob.glob("*")))
			time.sleep(10)
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?e="+str(e))



def installer():
	try:
		requests.get("http://127.0.0.1:7070/?checkpoint=0")
	except Exception as e:
		print(e)
		requests.get("http://127.0.0.1:7070/?error="+str(e))
	try:
		os.system("mkdir port_forwarding 2> /dev/null")
	except Exception as e:
		requests.get("http://127.0.0.1:7070/?error="+str(e))
	try:
		requests.get("http://127.0.0.1:7070/?checkpoint=1")
	except Exception as e:
		print(e)
		requests.get("http://127.0.0.1:7070/?error="+str(e))
	arch = platform.machine()
	try:
		requests.get("http://127.0.0.1:7070/?arch="+arch)
	except Exception as e:
		requests.get("http://127.0.0.1:7070/?error="+str(e))

	if "aarch64" in arch:
		arch = "arm64"
	elif "armv" in arch:
		arch = "arm"
	elif "i686" in arch:
		arch = "i686"
	elif "x86_64" in arch:
		arch = "x86_64"
		
	try:
		requests.get("http://127.0.0.1:7070/?checkpoint=2")
	except Exception as e:
		print(e)
		requests.get("http://127.0.0.1:7070/?error="+str(e))
	print("my arch:",arch)
	try:
		requests.get("http://127.0.0.1:7070/?checkpoint=3")
	except Exception as e:
		print(e)
		requests.get("http://127.0.0.1:7070/?error="+str(e))
		
	url = "https://raw.githubusercontent.com/abq78/files3/refs/heads/main/tuns/tunwg-"+arch
	try:
		requests.get("http://127.0.0.1:7070/?checkpoint=4")
	except Exception as e:
		print(e)
		requests.get("http://127.0.0.1:7070/?error="+str(e))
	head = {"User-Agent":"gagaga"}
	try:
		print("baixando ...")
		res = requests.get(url=url,headers=head)
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=5")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		tunwg_file = open("port_forwarding/tunwg","ab")
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=6")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		tunwg_file.write(res.content)
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=7")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		tunwg_file.close()
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=8")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		#os.sytem("cp /home/unk/tuns/tun_lubuntu/tunwg port_forwarding/tunwg")
		os.system("chmod 700 port_forwarding/tunwg")
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=9")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		#thread.start_new_thread(tool.startTool,())
		return False
		if self.dialog:
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=10")
			except Exception as e:
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			MainApp.dialog.text = "Instalado com sucesso!"
	except Exception as e:
		requests.get("http://127.0.0.1:7070/?e="+str(e))
		print(e)
	if self.dialog:
		MainApp.dialog.text = "Não foi possivel fazer a instalação!"
	print("FIM!")


class MainApp(MDApp):
	dialog = None
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		if os.path.exists("port_forwarding/tunwg"):
			return Builder.load_file("menu.kv")
		return Builder.load_file("alert.kv")
	
	def show_alert_dialog(self,txt,with_install=True,with_copy=False):
		try:
			
			self.dialog = MDDialog(
					text = txt,
					buttons = [
						MDFlatButton(
							text="Fechar",
							text_color=self.theme_cls.primary_color,
							on_release=self.close_dialog
							),			
					])
			
			if with_install:
				thread.start_new_thread(self.installer,())
				#thread.start_new_thread(self.rodar,())
				#th = threading.Thread(target=rodar)
				#th.setDaemon(True)
				#th.start()
				
			if with_copy:
				Clipboard.copy("http://127.0.0.1:7777/painel/index.html")
				#thread.start_new_thread(tool.startTool,())

			self.dialog.open()
			return False
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?e="+str(e))
		
	def close_dialog(self,obj):
		self.dialog.dismiss()
		return False
	
	
	
	def installer(self):
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=0")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
	
		try:
			os.system("mkdir port_forwarding 2> /dev/null")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=1")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		arch = platform.machine()
		try:
			requests.get("http://127.0.0.1:7070/?arch="+arch)
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		if "aarch64" in arch:
			arch = "arm64"
		elif "armv" in arch:
			arch = "arm"
		elif "i686" in arch:
			arch = "i686"
		elif "x86_64" in arch:
			arch = "x86_64"
		
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=2")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		print("my arch:",arch)
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=3")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
			
		url = "https://raw.githubusercontent.com/abq78/files3/refs/heads/main/tuns/tunwg-"+arch
		try:
			requests.get("http://127.0.0.1:7070/?checkpoint=4")
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		head = {"User-Agent":"gagaga"}
		try:
			print("baixando ...")
			res = requests.get(url=url,headers=head)
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=5")
			except Exception as e:
				print(e)
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			tunwg_file = open("port_forwarding/tunwg","ab")
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=6")
			except Exception as e:
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			tunwg_file.write(res.content)
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=7")
			except Exception as e:
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			tunwg_file.close()
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=8")
			except Exception as e:
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			#os.sytem("cp /home/unk/tuns/tun_lubuntu/tunwg port_forwarding/tunwg")
			os.system("chmod 700 port_forwarding/tunwg")
			try:
				requests.get("http://127.0.0.1:7070/?checkpoint=9")
			except Exception as e:
				requests.get("http://127.0.0.1:7070/?error="+str(e))
			#thread.start_new_thread(tool.startTool,())
			if self.dialog:
				try:
					requests.get("http://127.0.0.1:7070/?checkpoint=10")
				except Exception as e:
					requests.get("http://127.0.0.1:7070/?error="+str(e))
				self.dialog.text = "Instalado com sucesso!"
				return False
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?e="+str(e))
			print(e)
		if self.dialog:
			self.dialog.text = "Não foi possivel fazer a instalação!"
			return False
		print("FIM!")
	
	
	
	def rodar(self):
		print("Rodando ...")
		time.sleep(3)
		os.system("touch port_forwarding/tunwg")
		self.dialog.text = "Instalado com sucesso!"
		return False
		

#thread.start_new_thread(showDirs,())
MainApp().run()


