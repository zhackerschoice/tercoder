import os
os.system("clear")
os.system("toilet -f ivrit 'hex Encode'")
hex=input('enter your text :')
print("your ecoded text is  :")
os.system("echo "+hex+" | xxd -p")