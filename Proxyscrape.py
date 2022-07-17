# Api: https://www.proxy-list.download/api/v1/
# Website: https://www.proxy-list.download
# Developed by @Pandaxyz

import requests,time,random,os,json
banner = """ 


██████╗░██████╗░░█████╗░██╗░░██╗██╗███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝██╔════╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░██║█████╗░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░██║██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗██║███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░
"""
menu = """ 

          ╔══════════════╗
          | Proxy Types  |
          |--------------|
          | [1] HTTP     |
          | [2] SOCKS4   |
          | [3] SOCKS5   |
          ╚══════════════╝

"""
os.system("cls")
print(banner)
print(menu)
select = int(input("[>>] "))
if select == 1:
	http_selection = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
	http_result = http_selection.text
	os.system("cls")
	print(banner+"\n")
	print(http_result)
elif select == 2:
	socks4_selection = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
	socks4_result = socks4_selection.text
	os.system("cls")
	print(banner+"\n")
	print(socks4_result)
elif select == 3:
	socks5_selection = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
	socks5_result = socks5_selection.text
	print(banner+"\n")
	print(socks5_result)


