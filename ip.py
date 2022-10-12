#Assalamu wlaikum
#Code By H0rn3t sp1d3rs
#team bads security researchers
import socket
x='''\033[1;36;40m
██╗██████╗░
██║██╔══██╗
██║██████╔╝
██║██╔═══╝░
██║██║░░░░░
╚═╝╚═╝░░░░░

███████╗██╗███╗░░██╗██████╗░
██╔════╝██║████╗░██║██╔══██╗
█████╗░░██║██╔██╗██║██║░░██║
██╔══╝░░██║██║╚████║██║░░██║
██║░░░░░██║██║░╚███║██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░
'''
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")
print(x)
print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")

print("\033[1;33;40mCODE NAME: H0rn3t Sp1d3rs  ")
print("\033[1;33;40mAuthor : Mad Hackers Community")
print("GITHUB : HTTPS://GITHUB.COM/H0rn3t-Sp1d3rs")
print("Website : https://www.h0rn3t-sp1d3rs.tk")

print("\033[1;34;40m=============================================")
print("\033[1;33;40m|     DEVELOPED BY MAD HACKERS COMMUNITY    |")
print("\033[1;34;40m=============================================")

file = open('url.txt').read().split()
for url in file:
    domain = url.split('//')[1].replace('www.', '').replace('/', '')
    try :
        ipadrre = socket.gethostbyname(domain)
        
        print("\033[1;32;40m ")
        print(ipadrre)
        
       
    except:
        pass

