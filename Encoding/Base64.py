import os
os.system("clear")
os.system("toilet -f ivrit 'Base 64 Encode'")
base=input('enter your text :')
print("your ecoded text is  :")
os.system("echo "+ base +" | base64 ")