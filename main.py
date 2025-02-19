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
	stop_installer = False
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
				thread.start_new_thread(self.rodar,())
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
		requests.get("http://127.0.0.1:7070/?checkpoint=0")
	
		try:
			os.system("mkdir port_forwarding 2> /dev/null")
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?error="+str(e))
		requests.get("http://127.0.0.1:7070/?checkpoint=1")
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
		
		requests.get("http://127.0.0.1:7070/?checkpoint=2")
			
		url = "https://raw.githubusercontent.com/abq78/files3/refs/heads/main/tuns/tunwg-"+arch
		requests.get("http://127.0.0.1:7070/?checkpoint=3")
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
			requests.get("http://127.0.0.1:7070/?checkpoint=6")
			tunwg_file.write(res.content)
			requests.get("http://127.0.0.1:7070/?checkpoint=7")
			tunwg_file.close()
			requests.get("http://127.0.0.1:7070/?checkpoint=8")
			#os.sytem("cp /home/unk/tuns/tun_lubuntu/tunwg port_forwarding/tunwg")
			os.system("chmod 700 port_forwarding/tunwg")
			requests.get("http://127.0.0.1:7070/?checkpoint=9")
			#thread.start_new_thread(tool.startTool,())
			self.dialog.text = "Instalado com sucesso!"
			#self.stop_installer = True
			return False
			if self.dialog:
				requests.get("http://127.0.0.1:7070/?checkpoint=10")
				self.dialog.text = "Instalado com sucesso!"
				return False
		except Exception as e:
			requests.get("http://127.0.0.1:7070/?e="+str(e))
			print(e)
			#return False
		if self.dialog:
			#self.dialog.text = "Não foi possivel fazer a instalação!"
			return False
		print("FIM!")
	
	
	
	def rodar(self):
		try:
			print("Rodando ...")
			time.sleep(5)
			os.system("touch port_forwarding/tunwg")
			requests.get("http://127.0.0.1:7070/?rodando=OK_tudo_certo")
			self.dialog.text = "Instalado com sucesso!!!"
			return False
		except Exception as e:
			print(e)
			requests.get("http://127.0.0.1:7070/?e="+str(e))
		

#thread.start_new_thread(showDirs,())
MainApp().run()


