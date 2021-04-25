import os
import os 
os.system("clear")
os.system("toilet -f ivrit 'Encoder'")
print('Encode as')
print('    1.Base 64')
print('    2.Rot13')
print('    3.hex')
choise=input('Choose : ')
if choise=="1":
	os.system("python3 Encoding/Base64.py")
if choise=="2":
    os.system("python3 Encoding/Rot13.py")
if choise=="3":
	os.system("python3 Encoding/hex.py")
else :
	print("please enter a valid option")