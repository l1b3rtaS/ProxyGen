from tqdm import tqdm , tqdm_gui , trange
from colorama import Fore, Back, Style
print(Fore.RED + """ 	 _______  _______  _______                    _______  _______  _       
	(  ____ )(  ____ )(  ___  )|\     /||\     /|(  ____ \(  ____ \( (    /|
	| (    )|| (    )|| (   ) |( \   / )( \   / )| (    \/| (    \/|  \  ( |
	| (____)|| (____)|| |   | | \ (_) /  \ (_) / | |      | (__    |   \ | |
	|  _____)|     __)| |   | |  ) _ (    \   /  | | ____ |  __)   | (\ \) |
	| (      | (\ (   | |   | | / ( ) \    ) (   | | \_  )| (      | | \   |
	| )      | ) \ \__| (___) |( /   \ )   | |   | (___) || (____/\| )  \  |
	|/       |/   \__/(_______)|/     \|   \_/   (_______)(_______/|/    )_)
	                    ProxyList Generator                 By l1b3rta$
	 """)
print(Fore.YELLOW + "  Введите порт>>> ")
port = input("")
print (Fore.YELLOW + """  Выберите шаблон ip>>>
	1)10.000.000.000 (17 GB)
	2)100.000.0.000 (6 GB)
	3)100.000.0.0 (1 GB)
	4)100.00.0.0 (128 MB)
	5)10.0.0.0 (1 MB)""")
way = input("")
file = open("list.txt", "w")
if way == "1":
	t = 89999999999
	s = 10000000000
	for i in tqdm(range(t)):
		s = s + 1
		z = str(s)
		a = (z[0:2])
		b = (z[2:3])
		c = (z[3:4])
		d = (z[4:5])
		q = (a + "." + b + "." + c +"." + d)
		file.write(q + " " + (port) + "\n")
	file.close()
if way == "2":
	t = 8999999999
	s = 1000000000
	for i in tqdm(range(t)):
		s = s + 1
		z = str(s)
		a = (z[0:2])
		b = (z[2:3])
		c = (z[3:4])
		d = (z[4:5])
		q = (a + "." + b + "." + c +"." + d)
		file.write(q + " " + (port) + "\n")
	file.close()
if way == "3":
	t = 89999999
	s = 10000000
	for i in tqdm(range(t)):
		s = s + 1
		z = str(s)
		a = (z[0:2])
		b = (z[2:3])
		c = (z[3:4])
		d = (z[4:5])
		q = (a + "." + b + "." + c +"." + d)
		file.write(q + " " + (port) + "\n")
	file.close()
if way == "4":
	t = 8999999
	s = 1000000
	for i in tqdm(range(t)):
		s = s + 1
		z = str(s) 
		a = (z[0:3])
		b = (z[3:5])
		c = (z[5:6])
		d = (z[6:7])
		q = (a + "." + b + "." + c +"." + d)
		file.write(q + " " + (port) + "\n")
	file.close()
if way == "5":
	t = 89999
	s = 10000
	for i in tqdm(range(t)):
		s = s + 1
		z = str(s)
		a = (z[0:2])
		b = (z[2:3])
		c = (z[3:4])
		d = (z[4:5])
		q = (a + "." + b + "." + c +"." + d)
		file.write(q + " " + (port) + "\n")
	file.close()


#Designed by l1b3rta$
#My telegram channel - t.me/lamer_hotel



