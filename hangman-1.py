import os.path
phon1=input("enter your phon==============>")        
phonlen1=len(phon1)

if ((phonlen1==11)) and (phon1.isdigit()==True):
    if os.path.isfile("D:\\"+phon1+".txt"):
        print("filemojod")
    else:
        file1=open("D:\\"+phon1+".txt","w")
    print("ok!")
phon2=input("enter your phon==============>")

phonlen2=len(phon2)
if ((phonlen2==11)) and (phon2.isdigit()==True):
    if os.path.isfile("F:\\"+phon2+".txt"):
        print("file2mojod")
    else:
      file2=open("F:\\"+phon2+".txt","w")
    print("ok!")

else:
    print("!!!!!!!error!!!!!!!!!")
    exit()    
emtyaz=1
playr1=input("enter word?")
guess=0
chrlist =[]
lenkalame=len(playr1)
m=lenkalame+5
for c in playr1:
    chrlist.append(c)
while guess<m:
    lelist=len(chrlist)
    if((lelist==0)):
        print(playr1)
        print(emtyaz)
        file2.write(str(emtyaz))
        file2.close()
        exit()
    playr2=input("enter yur chr?")
    if ((playr2 in chrlist)):
            print(playr2+" true")
            chrlist.remove(playr2)
    else:
            print(playr2+" false")
            guess+=1   
print(emtyaz)   
file1.write(str(emtyaz))
file1.close()   


        