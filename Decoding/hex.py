import os
os.system("clear")
os.system("toilet -f ivrit 'hex Decode'")
hex=input('enter your text :')
print("your Decoded text is  :")
os.system("echo "+hex+" | xxd -p -r")