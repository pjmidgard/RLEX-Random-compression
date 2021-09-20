from time import time
cvf=0
Portal=2
import os
import binascii

zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""


asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("c for compress or e for extract? ")
#@Author Jurijus pacalovas
class compression:
                
    def cryptograpy_compression(self):
                
                self.name = "Written: Jurijus pacalovas Price Protal 5 000 000 Euro cost Date: 16/09/2021 14:23 Deep 14.5 ERA"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2

                     
                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    
                    if nameas[nac-5:nac]==".docx":
                        Portal=1
                    if nameas[nac-4:nac]==".pdf":
                        Portal=3
                    if nameas[nac-4:nac]==".doc":
                        Portal=1
                    if nameas[nac-4:nac]==".png":
                        Portal=7
                    if nameas[nac-4:nac]==".jpg":
                        Portal=9
                    if nameas[nac-4:nac]==".mp4":
                        Portal=8
                      
                    if i==1:
                       
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=16
                    
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1
                    block2=0
                    block3=0
                    
                    

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()

                        
                

                        
                        if i==1:
                            if Portal==9 and data[0:3]!=b'\xff\xd8\xff':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==9 and data[0:3]==b'\xff\xd8\xff': 
                                    data=data[3:]
                            if Portal==7 and data[0:4]!=b'\x89\x50\x4e\x47' :
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==7 and data[0:4]==b'\x89\x50\x4e\x47' :             
                                    data=data[4:]
                            if Portal==8 and data[0:11]!=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==8 and data[0:11]==b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':             
                                    data=data[11:]
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                        assxq=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]


                                block2=0
                                if i==2:
                                        
                                    sda2=sda2[1:]
                                    lenf5=len(sda3)

                                    if sda2[lenf5-8:lenf5]=="10000000":

                                        sda2=sda2[:lenf5-8]

                                    elif sda2[lenf5-7:lenf5]=="1000000":

                                        sda2=sda2[:lenf5-7]

                                    elif sda2[lenf5-6:lenf5]=="100000":

                                        sda2=sda2[:lenf5-6]

                                    elif sda2[lenf5-5:lenf5]=="10000":

                                        sda2=sda2[:lenf5-5]


                                    elif sda2[lenf5-3:lenf5]=="100":

                                        sda2=sda2[:lenf5-3]

                                    elif sda2[lenf5-2:lenf5]=="10":

                                        sda2=sda2[:lenf5-2]

                                    elif sda2[lenf5-1:lenf5]=="1":

                                        sda2=sda2[:lenf5-1]

                                    
                                    lenf5=len(sda2)
                                    
                                    block2=0
                                    ei4=0
                                    ei5=15
                                    while sda2[ei4+14:ei5]=="1" or sda2[ei4+14:ei5]=="0":
                                                        
                                                        e4=sda2[ei4:ei5]
                                                        
                                                       
                                                        if e4=="000000000000001":
                                                            ei4=ei4+16
                                                            ei5=ei5+16
                                                            
                                                            e4=sda2[ei4:ei5]
                                                            sda4=sda4+e4

                                                        else:
                                                            sda4=sda4+e4+"0"
                                   
                                                        ei4=ei4+15
                                                        ei5=ei5+15

                                                        
             
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                    cvf1=1

                                   
                                                    
                               
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                    block2=0
                                    if i==1:
                                                 sda3=sda2
                                    
                                                 while ei5<lenf5*8:
                                                        e4b=sda3[ei4+14:ei5]
                                                        e4=sda3[ei4:ei5]
                                                        e4a=sda3[ei4:ei5-1]
                                                        
                                                        block2=block2+1
                                                       
                                                        if e4b=="00" or e4a!="000000000000001":
                                                            sda4=sda4+e4a+ei8

                                                        elif e4b=="10" or e4a!="000000000000001":
                                                            sda4=sda4+e4+ei8

                                                        elif e4b=="01" or e4a!="000000000000001":
                                                            sda4=sda4+"0000000000000010"+e4+ei8
                                                        elif e4b=="11" or e4a!="000000000000001":
                                                            sda4=sda4+"0000000000000010"+e4+ei8

                                                        elif e4a=="000000000000001":
                                                            sda4=sda4+e4a+e4+ei8
                                                        else:
                                                            sda4=sda4+"000000000000001"+e4+ei8

                                                        
                                                        
                                                        ei4=ei4+16
                                                        ei5=ei5+16
                                                        

                                                  

                                    
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    cvf1=1
                                   
                                                        
                                        
                                                    
                                    if cvf1==1:

                                                    if i==2:
                                                        wer=""
                                                        szx=""
                                                        wer=sda4

                                                    if i==1:
                                                        wer=""
                                                        wer=sda4
                                                        sda4=""
                                                        szx=""

                                                        wer="1"+wer+"1"
                                                        lenf=len(wer)
                                                        print(lenf)
                                                        xc=8-lenf%8
                                                        z=0
                                                        if xc!=0:
                                                            if xc!=8:
                                                                while z<xc:
                                                                    szx="0"+szx
                                                                    z=z+1
                                                        wer=wer+szx
                                                                                    
                                                    n = int(wer, 2)
                                                    qqwslenf=len(wer)
                                                    qqwslenf=(qqwslenf/8)*2
                                                    qqwslenf=str(qqwslenf)
                                                    qqwslenf="%0"+qqwslenf+"x"
                                                    jl=binascii.unhexlify(qqwslenf % n)
                                                    sssssw=len(jl)
                                                    data=jl
                                                    qqqwz=qqqwz+1
                                                    szxzzza=""
                                                    szxzs=""
                                                    assx=10
                                                    assxq=assxq+1
                                                    sda4=""
                                                    sda3=""
                                                    if assxq==1:
                                                       assx=10 
                                                    if assx==10:        
                                                        if i==2:
                                                            if Portal==7:
                                                                jl= b'\x89\x50\x4e\x47'+jl
                                                            if Portal==8:
                                                                jl=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34'+jl
                                                            if Portal==9:
                                                                jl=b'\xff\xd8\xff'+jl
                                                        f2.write(jl)
                                                        x2 = time()
                                                        x3=x2-x
                                                        return print(x3)

d=compression()

xw=d.cryptograpy_compression()
print(xw)
