import os
os.system("clear")
os.system("toilet -f ivrit 'Rot13 Decode'")
Rot=input('enter your text :')
print("your Decoded text is  :")
os.system("echo "+Rot+ " | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
