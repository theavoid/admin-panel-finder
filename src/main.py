import requests;
import time
from colorama import Fore, Back, Style
import validators
import random

def checkConnection():
    r = requests.get("https://thavo.me")
    if r.status_code == 200:
        return True
    else:
        return False

print(Fore.BLUE + """
___________.__             ____   ____    .__ .___
\__    ___/|  |__   ____   \   \ /   /___ |__| __| _/
  |    |   |  |  \_/ __ \   \   Y   /  _ \|  |/ __ | 
  |    |   |   Y  \  ___/    \     (  <_> )  / /_/ | 
  |____|   |___|  /\___  >    \___/ \____/|__\____ | 
                \/     \/                         \/ 
""")
print("Checking internet connection...")
if not checkConnection():
    exit()
time.sleep(3)
print(Fore.RED + 'TheVoid - Admin Panel Finder v0.1')
time.sleep(2)
print(Fore.YELLOW + 'Admin Panel Finder starting...')
time.sleep(1)
site = input('Please input site (E.g.: https://google.com): ')
if not validators.url(site):
    print("Please enter in https://domain.com format.")
    exit()

list = ["/admin", "/wp-admin", "/modelsearch/login.asp", "/adminpanel.asp", "/admin.php", "/admin.asp", "/admin.html", "/controlpanel", "/controlpanel.php", "/controlpanel.asp", "/controlpanel.html", "/ur-admin.html", "/admin/index.php", "/admin.htm", "/admin.html", "/panel.php", "/panel.asp", "/panel.aspx","/panel.html", "/panel.htm", "/system", "/access", "/sysadm", "/manager", "/letmein", "/users", "/auth/admin", "/auth/admin.php", "/admin/users", "/admin/users.php", "/admin/user.aspx", "/authuser", "/authuser.php" ,"/authuser.asp", "/authuser.aspx", "/yonetim", "/yonetim.php", "/yonetim.aspx", "/yonetim.asp", "/yonetim.htm", "/yonetim.html", "/cp", "/cp/index.php", "/cp.php","/yonetici", "/yonetici.php", "/yonetici.aspx", "/yonetici.htm","/yonetici.htm", "/adminsite", "/adminsite.php", "/adminsite.aspx", "/adminsite.asp", "/adminsite.htm", "/adminsite.html", "/kpanel", "/kpanel.php", "/kpanel.asp", "/kpanel.aspx", "/kpanel.htm", "/kpanel.html", "/admin/posts", "/admin/posts.php", "/admin/posts.asp", "/admin/posts.aspx", "/admin/posts.html", "/admin/posts.html", "/cpanel", "/cpanel.php", "/admin/cpanel.php", "/admin/index.asp", "/admin/index.php", "/admin/giris", "/admin/giris.php", "/admin/giris.asp", "/admin/giris.aspx", "/admin/giris.html","/admin/giris.htm","/admin/login.php", "/admin/logout.php", "/admin/login.asp", "/admin/Login.asp", "/Admin/Login.asp", "/admin/login.aspx", "/Admin/Login.aspx", "/Admin/Logout.aspx", "/Admin/Logout.asp", "/Admin", "/admin2.php", "/admin2.asp", "/admin2.aspx", "/admin2.html", "/admin2.htm", "/admin2", "/Admin2.asp", "/Admin2.aspx", "/Admin2.php", "/ebadmin", "/siteadmin", "/siteadmin.php","/siteadmin.asp","/siteadmin.aspx","/siteadmin.html","/siteadmin.htm", "/admincontrolpanel","/admincontrolpanel.php","/admincontrolpanel.aspx","/admincontrolpanel.asp", "/admincontrolpanel.html","/admincontrolpanel.htm","/yonetici/index.php","/yonetici/users.php","/yonetici/logout.php","/yonetici/index.asp","/yonetici/users.asp","/yonetici/index.aspx","/yonetici/users.aspx","/yonetici/index.html","/yonetici/index.htm","/Admin/Index", "/Admin/Index.asp","/Admin/Index.php","/Admin/Index.aspx", "/kurum-giris","/kurum-girisi","/sube","/sube-girisi","/kurumsal"]
for fan in list:
    print(fan)

eta = int(len(list)) * 1
minutes = eta / 60
print(f'Average scan time: {minutes:.2f} minutes.')
time.sleep(4)
foundedPaths = 0;
absendPaths = 0;

for f in list:
    r = requests.get(site+f)
    if r.status_code == 200 or r.status_code == 202 or r.status_code == 302:
        print(Fore.GREEN + "FOUND: " + site + f)
        foundedPaths+= 1
    else:
        print(Fore.RED + "NOT FOUND: "+ site + f)
        absendPaths+= 1
    time.sleep(1)

print(Fore.BLUE + "SITE REPORT")
print(Fore.YELLOW + str(foundedPaths) + " paths found, " + str(absendPaths) + " paths not found.")
