import os 
os.system("clear")
os.system("toilet -f ivrit 'Decoder'")
print('What Type of encoded text you want to Decode.')
print('    1.Base 64')
print('    2.Rot13')
print('    3.hex')
choise=input('Choose : ')
if choise=="1":
	os.system("python3 Decoding/Base64.py")
if choise=="2":
    os.system("python3 Decoding/Rot13.py")
if choise=="3":
	os.system("python3 Decoding/hex.py")
else :
	print("please enter a valid option")
