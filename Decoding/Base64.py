import os
os.system("clear")
os.system("toilet -f ivrit 'Base 64 Decode'")
base=input('enter the encoded text :')
print("the decoded text is  :")
os.system("echo "+ base +" | base64 --decode")
