import os , sys 
import subprocess as ss
os.system(sys.argv[1])
print(".............")

a=os.system("ls")
print(a)
print("....................")

ss.call("ifconfig",shell=True)
print(".....................")

b=ss.getoutput("ip a")
print(b)
print("................")
