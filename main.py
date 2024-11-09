
###TAKS ENGINES
##TASKS programmes
#LINE
#ALPHA     

spc=f'''
    


    '''   
a=f'''
░█████╗░
██╔══██╗
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝
'''
b=f'''
██████╗░
██╔══██╗
██████╦╝
██╔══██╗
██████╦╝
╚═════╝░
'''
c=f'''    
░█████╗░
██╔══██╗
██║░░╚═╝
██║░░██╗
╚█████╔╝
░╚════╝░
'''
d=f'''
██████╗░
██╔══██╗
██║░░██║
██║░░██║
██████╔╝
╚═════╝░    
'''
e=f'''
███████╗
██╔════╝
█████╗░░
██╔══╝░░
███████╗
╚══════╝  
'''

f=f'''  
███████╗
██╔════╝
█████╗░░
██╔══╝░░
██║░░░░░
╚═╝░░░░░
'''
g=f'''
░██████╗░
██╔════╝░
██║░░██╗░
██║░░╚██╗
╚██████╔╝
░╚═════╝░
'''
h=f'''
██╗░░██╗
██║░░██║
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝
'''
i=f''' 
██╗
██║
██║
██║
██║
╚═╝
'''
j=f'''
░░░░░██╗
░░░░░██║
░░░░░██║
██╗░░██║
╚█████╔╝
░╚════╝░
'''
k=f'''
██╗░░██╗
██║░██╔╝
█████═╝░
██╔═██╗░
██║░╚██╗
╚═╝░░╚═╝
'''          
l=f'''
██╗░░░░░
██║░░░░░
██║░░░░░
██║░░░░░
███████╗
╚══════╝ 
'''
m=f'''
███╗░░░███╗
████╗░████║
██╔████╔██║
██║╚██╔╝██║
██║░╚═╝░██║
╚═╝░░░░░╚═╝
'''
n=f'''
███╗░░██╗
████╗░██║
██╔██╗██║
██║╚████║
██║░╚███║
╚═╝░░╚══╝ 
'''
o=f''' 
░█████╗░
██╔══██╗
██║░░██║
██║░░██║
╚█████╔╝
░╚════╝░
'''
p=f'''
██████╗░
██╔══██╗
██████╔╝
██╔═══╝░
██║░░░░░
╚═╝░░░░░
'''
q=f'''
░██████╗░
██╔═══██╗
██║██╗██║
╚██████╔╝
░╚═██╔═╝░
░░░╚═╝░░░
'''
r=f'''
██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝
''' 
s=f'''
░██████╗
██╔════╝
╚█████╗░
░╚═══██╗
██████╔╝
╚═════╝░             
'''
t=f'''
████████╗
╚══██╔══╝
░░░██║░░░
░░░██║░░░
░░░██║░░░
░░░╚═╝░░░
'''
u=f'''
██╗░░░██╗
██║░░░██║
██║░░░██║
██║░░░██║
╚██████╔╝
░╚═════╝░  
'''
v=f'''
██╗░░░██╗
██║░░░██║
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░╚═╝░░░
'''
w=f'''
░██╗░░░░░░░██╗
░██║░░██╗░░██║
░╚██╗████╗██╔╝
░░████╔═████║░
░░╚██╔╝░╚██╔╝░
░░░╚═╝░░░╚═╝░░
'''
x=f'''
██╗░░██╗
╚██╗██╔╝
░╚███╔╝░
░██╔██╗░
██╔╝╚██╗
╚═╝░░╚═╝
'''
y=f'''
██╗░░░██╗
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░██║░░░
░░░╚═╝░░░ 
'''       
z=f'''
███████╗
╚════██║
░░███╔═╝
██╔══╝░░
███████╗
╚══════
'''  
d={
"A":a,
"B":b,
"C":c,
"D":d,
"E":e,
"F":f,
"G":g,
"H":h,
"I":i,
"J":j,
"K":k,
"L":l,
"M":m,
"N":n,
"O":o,
"P":p,
"Q":q,
"R":r,
"S":s,
"T":t,
"U":u,
"V":v,
"W":w,
"X":x,
"Y":y,
"Z":z,
" ":spc} 
def gp():
    print(" ")
def onlynum(n):
    num=[]
    numo=n.split(" ")
    for i in numo:
        if i.isdigit():
            num.append(i)
            v=int(num[0])
            return v
import sys
import time
def bt():
    bt=f"{bot} is typing....."
    for v in bt:
        sys.stdout.write(v)
        time.sleep(0.02)
        
def Cesar(condition,user_input):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z',' ']
    shift = int(input("Enter shifting number :"))
    answer = ""
    for char in user_input:
        if char in alpha:
            posi = alpha.index(char)
            if condition == "enc":
                answer = answer + alpha[(posi + shift) % ((len(alpha))-1)]
            else:
                answer = answer + alpha[(posi - shift) % ((len(alpha))-1)]
    return "".join(answer)

#capital
def cap(n):
    z=n.upper()
    return z
def fini():
    bg()
    gp()
    print(f"{bot}: !!!! Game over !!!!")
#MOUNTAIN GENERATOR
def m(username):
    z=len(username)
    for i in range(z):
        print(username[0:(i+1)])#1 cycle
    for i in range(z):   
          print(username[0:(z-i)])
    for i in range(z):
        print(username[0:(i+1)])#2 cycle
    for i in range(z):   
          print(username[0:(z-i)])
    for i in range(z):
        print(username[0:(i+1)])#3 cycle
    for i in range(z):   
          print(username[0:(z-i)])
    for i in range(z):
        print(username[0:(i+1)])#4 cycle
    for i in range(z):   
          print(username[0:(z-i)])
    for i in range(z):
        print(username[0:(i+1)])#1 cycle
    for i in range(z):   
          print(username[0:(z-i)])
#number mountian
def nm(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(j, end=' ')
        print("")

#Bot typing and gap function:
def bg1():
    gp()
    bt()
def bg():
    bg1()
    gp()   


#string reverse
def strrev(n):
    print(n)
    z=len(n)
    for i in range(1,z+1):
        print(n[z-i],end="")
    

def l():
    print(('=')*45)     
pass
#PYRAMID
def pyd():
    bg()
    gp()
    print(f"{bot} 🤖 :Ok {username},so u want to have ur pyramid build with which character?")
    l()
    n=str(input(f"{user} 🤠 :"))*2
    l()
    size=15
    m=2*(size-1)
    bg()
    gp()
    print(f"{bot} 🤖 :There u go {username} :)")
    gp()
    for i in range(size):
        for j in range(0,m):
                print(end=" ")
        m=m-1
        for j in range(0,i+1):
                print(n,end="")
        print(" ")
    gp()       
pass
#PERCENTAGE
def per():
    l()
    n=int(input(f"{user} 🤠 :"))
    bg()
    gp()
    print(f"{bot}: What will be the denominator {username}")
    gp()
    of=int(input(f"{user}: "))
    gp()
    l4=[]
    for i in range(1,n+1):
        c1=int(input(f"{user} 🤠 :  Sub{i}->"))
        l4.append(c1)
    l()
    c=len(l4)
    gp()
    print(l4)
    v=(sum(l4)/(c)*of)/100
    bg() 
    gp()  
    print(f"{bot} 🤖 :{username},The percentage is {v} %")
def r():
    bg()
    gp()
    print(f"{bot} 🤖 :{username},")
    
import random
from logging import exception


def game(comp,n):
        if comp==n:
            return None
        elif comp=='stone':
            if n=='paper':
               return True
            elif n=='cissor':
                False
        elif comp=='paper':
            if n=='stone':
               return False
            elif n=='cissor':
               return True
        elif comp=='cissor':
            if n=='paper':
               return False
            elif comp=='stone':
                return True
            pass
def sps():
    print(f"      | STONE PAPER SCISSOR |")
    bg()
    gp()
    print(f"{bot} 🤖 :(Shakes hand) stone,paper,scissor.")
    ran=random.randint(1,3)
    if ran==1:
        comp='stone'
    elif ran==2:
        comp='paper'
    elif ran==3:
        comp='cissor'
    gp()
    n=str(input(f"{user} 🤠 :---> ")) 
    a=game(comp,n)
    bg()
    gp()
    print(f"{bot} 🤖 :I chose ---> {comp}")
    if a==None:
        bg()
        gp()
        print(f"{bot} 🤖 :{username},This is a draw, play Again by texting spc:|")
        
    elif a==True :
        bg()
        gp()
        print(f"{bot} 🤖 :{username},You won,I lost :(, play Again by texting spc")
        
    else:
        bg()   
        gp()    
        print(f"{bot} 🤖 :{username},You lose,I won :),play Again by texting spc")
        
pass  
#Quadratic equation
def q():
    try:
        bg()
        gp()
        print(f"{bot} 🤖 :The general quadratic equation is (a)x^2 + (b)x + (c) = 0 , So plz mention the values of a,b and c")
        l()
        a=float(eval(input(f"{user}:a=")))
        b=float(eval(input(f"{user}:b=")))
        c=float(eval(input(f"{user}:c=")))
        l()
        x1=round((-b-(((b*b)-(4*a*c)))**0.5)/2*a, 4) 
        x2=round((-b+(((b*b)-(4*a*c)))**0.5)/2*a,4)
        bg()
        gp()
        print(f'''{bot}:Since, The given quadratic equation is 
        ({a})x^2 + ({b})x + ({c}) = 0''')
        bg()
        gp()
        print(f'{bot} 🤖 :{username},So the values are x={x1},{x2}')
    except Exception:
        l()
        bg()
        gp()
        print(f"{bot}:{username},plz input numerical value and try again :(")
pass

#STAR MOUNTAIN
def star(n):
    bg()
    gp()
    print(f"{bot}:{username},so type the bulding block of your mountain!")
    l()
    o=str(input(f"{user}: "))
    l()
    bg()
    gp()
    print(f"{bot}:There you go {username} !")
    gp()
    k=n+1
    for i in range (1,k):
        print(f"{o}"*i)
    for j in range (1,k):
        print(f"{o}"*(k-(j+1)))
    for i in range (1,k):
        print(f"{o}"*i)
    for j in range (1,k):
        print(f"{o}"*(k-(j+1)))
    for i in range (1,k):
        print(f"{o}"*i)
    for j in range (1,k):
        print(f"{o}"*(k-(j+1)))
pass


gp()
intro='''|||||||||||||||||||LOADING|||||||||||||||||||'''

for v1 in intro:
    sys.stdout.write(v1)
    time.sleep(0.01)
gp()
gp()
class isc:
    def space(self):
        sp=[]
        for i in self.name:
            if i.isalpha():
                sp.append(i)
        if len(sp)>0:
            return True      
        else:
            return False
pass    

while True:
    username=str(input("ENTER YOUR NAME 🤠 : "))
    user=cap(username)
    gp()
    botname=str(input("ENTER BOT NAME 🤖 : "))
    bot=cap(botname)
    userna=isc()
    userna.name=username
    botna=isc()
    botna.name=botname
    if (userna.space() and botna.space()) is True and username!=botname:
        break
    elif username=="n" and botname=="n":
        import random
        name=["babita","popatlal","iyer","champaklal","tappu","jethalal","bagha","rakhi","panda","vivek","deepaklal","hindustanibhau","joginder"]
        r1=random.randint(0,len(name)-1)
        r2=random.randint(0,len(name)-1)
        username=str(name[r1])
        botname= str(name[r2])
        user=cap(name[r1])
        bot=cap(name[r2])        
        l()
        print(f"PROGRAMMER:Ok fine then, I'll take your name as {username} and bot's name as {botname}")
        break
    elif (userna.space() or botna.space()) is False:
        l()
        print("PROGRAMMER:Plz don't leave it empty")
        l()
    elif userna.space() is True and botna.space() is False:
        l()
        print(f"PROGRAMMER:Plz input some botname 😂 ")
        l()
    elif botna.space() is True and userna.space() is False: 
        l()
        print(f"PROGRAMMER:Plz input some username 😂 ")
        l()
    elif username==botname:
        l()
        print(f"PROGRAMMER:Username and botname should be different 😂 ")
        l()
l()
print(f"PROGRAMMER:{username},Ask what {botname} can do :)")
l()
bg()
gp()
print(f"{bot}:Hello {username}! Iam currently on learning stage :),So plz don't get irritated when i miss something.")

while True:
    qa=open("ques.txt","a")
    aa=open("ans.txt","a")
    qr=open("ques.txt","r").read()
    ar=open("ans.txt","r").read()
    ql=qr.split("_")
    al=ar.split("_")
    qna=dict()
    for c,v in zip(ql,al):
        qna.update({c:v})
    ques=qna.keys()
    l()
    n=str(input(f"{user} 🤠 :"))
    n1=isc()
    n1.name=n
    l() 
    if "bye" in n or "tata"in n:
        bg()
        gp()     
        print(f"{bot} 🤖 :Ok bye {username}, plz come again! 😢 and apologies for inconviniencies. ")
        l()
        tata=f"{username},Don't forget to review programme :)," 
        for v2 in tata:
            sys.stdout.write(v2)
            time.sleep(0.01)      
        gp()
        gp()
        break
    elif "qna" in n:
        bg()
        gp()
        print(f'{bot} :This is my key and value {username},you too can programme my replies by texting me "new chat".')
        gp()
        print("| KEY |==============>| VALUE |")
        for c,v in zip(ql,al):
                print(f"|{c}| ------> |{v}|")                     
    elif "uniqui" in n:
        bg()
        gp()
        print(f'{bot} 🤖 :Now text me all the characters which you want me to uniquify')
        l()                                              
        N=str(input(f'{user} 🤠 :')).upper()
        l()
        bg()
        gp()
        print(f"{bot} 🤖 :There you go {username} :)")
        gp()
        for j in N:
            print(d.get(j),end="") 
    elif "factor" in n and "of " in n:    
        try: 
            if n==0 or n==1:
                print(f"{botname} 🤖 :Factorial of 1 or 0 is 0")       
            else:
                mul=[]
                num=n.split(" ")
                for i in num:
                    if i.isdigit():
                       mul.append(i)
                u=(int(mul[0]))
                fact=1
                for i in range (1,u):
                    fact*=u
                    u=u-1
                bg()
                gp()
                print(f"{bot} 🤖 :Factorail of {mul[0]}! is {fact}")
        except Exception as e:
            bg()
            gp()
            print(f"{bot}:Be more specific.")
    elif 'quadrat' in n:
        try:
            bg()
            gp()
            print(f"{bot} 🤖 :The general quadratic equation is ax**2 + bx + c = 0 , So plz mention the values of a , b and c")
            l()
            A=float(eval(input(f"{user}:a=")))
            B=float(eval(input(f"{user}:b=")))
            C=float(eval(input(f"{user}:c=")))
            l()
            a=1
            b=B/A
            c=C/A
            x1=(-(b)-(b**2-(4*a*c))**0.5)/2
            x2=(-(b)+(b**2-(4*a*c))**0.5)/2
            bg()
            gp()
            print(f'''{bot}:Since, The given quadratic equation is 
            ({A})x^2 + ({B})x + ({C}) = 0''')
            bg()
            gp()
            print(f'{bot} 🤖 :{username},So the values are x={x1},{x2}')
        except Exception:
                l()
                bg()
                gp()
                print(f"{bot}:{username},plz input integer value and try again :(")
    elif 'reverse'in n:
        bg()
        gp()     
        print(f"{bot} 🤖 :{username},type the text which u want it to get reversed!")
        l()
        n=str(input(f"{user} 🤠 :"))
        l()
        print(f"{bot} 🤖 :Here's your reversed text {username}:)")
        gp()
        z3=strrev(n)
        gp()
    elif 'wave'in n:
        bg()
        gp()
        print(f"{bot} 🤖 :ok {username} there u go!")
        z7=m(username)       
    elif 'mounta'in n:
        try:
            bg()
            gp()
            print(f"{bot} 🤖 :ok {username},plz type your mounntain's desired height in integer only :)")
            l()
            n=int(input(f"{user} 🤠 :"))
            l()        
            z6=star(n)       
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot}:{username}, plz enter only integer value and try again :(") 
    elif 'matri' in n:
        try:
            bg()
            gp()
            print(f"{bot}:{username},determinant of 2 x 2 or 3 x 3 ?")
            l()
            n=str(input(f"{user}: "))
            l()
            if "2" in n:
                bg()
                gp()
                print(f"{bot}:{username},Plz type all the elements ")
                print(f'''
| a11  a12 | 
| a21  a22 |
                ''')
                l()
                y0=int(eval(input(f"{user} 🤠 : a11=")))
                y1=int(eval(input(f"{user} 🤠 : a12=")))
                y2=int(eval(input(f"{user} 🤠 : a21=")))
                y3=int(eval(input(f"{user} 🤠 : a22=")))
                l()
                bg()
                gp()
                print(f"{botname}:This is your determinant {username}")
                r1=[y0,y1]
                r2=[y2,y3]
                gp()
                for i in r1:
                    print(i,end=" ")
                gp()
                for j in r2:
                    print(j,end=" ")
                gp()  
                bg()
                gp()
                deter=y0*y3-y1*y2
                print(f"{bot}:| The value of determinant is {deter} |")
                m11=y3
                m12=-1*y2
                m21=-1*y1
                m22=y0
                bg()
                gp()
                print(f"|Cofactor|")
                m1=[m11,m12]
                m2=[m21,m22]
                
                for i in m1:
                    print(i,end=" ")
                gp()
                for j in m2:
                    print(j,end=" ")
                gp()
                bg()
                gp()
                print("| Adjoint |")
                ma1=[m11,m21]
                ma2=[m12,m22]
                for i in ma1:
                    print(i,end=" ")
                gp()
                for j in ma2:
                    print(j,end=" ")
                gp()
                bg()
                gp()
                print(f"Divide each & every element  of below matrix by {deter}.")
                print("| Inverse |")
                for i in ma1:
                    print(i,end=" ")
                gp()
                for j in ma2:
                    print(j,end=" ")
                gp()
                
            elif "3" in n:
                bg()
                gp()
                print(f"{bot}:{username},Plz type all the elements ")
                
                print(f'''
| a11  a12 a13 | 
| a21  a22 a23 |
| a31  a32 a33 |
                ''')
                l()
                y0=int(eval(input(f"{user}: a11= ")))
                y1=int(eval(input(f"{user}: a12= ")))
                y2=int(eval(input(f"{user}: a13= ")))
                y3=int(eval(input(f"{user}: a21= ")))
                y4=int(eval(input(f"{user}: a22= ")))
                y5=int(eval(input(f"{user}: a23= ")))
                y6=int(eval(input(f"{user}: a31= ")))
                y7=int(eval(input(f"{user}: a32= ")))
                y8=int(eval(input(f"{user}: a33= ")))
                l()
                bg()
                gp()
                print(f"{botname}:This is your determinant {username}")
                r1=[y0,y1,y2]
                r2=[y3,y4,y6]
                r3=[y7,y8,y8]
                gp()
                for i in r1:
                    print(i,end=" ")
                gp()    
                for j in r2:
                    print(j,end=" ")
                gp()    
                for k in r3:
                    print(k,end=" ")
                gp()
                
                deter=(y0*(y4*y8-y7*y5)) - (y1*(y3*y8-y6*y5)) + (y2*(y3*y7-y6*y4))
                bg()
                gp()
                print(f'''{bot}:| value of determinant is {deter} |''')
                m11=(y4*y8)-(y5*y7)
                m12=-((y3*y8)-(y6*y5))
                m13=(y3*y7)-(y6*y4 )
                m21=-((y1*y8 )-(y7*y2 ))
                m22=(y0*y8)-(y2*y6)
                m23=((y0*y7)-(y6*y1))
                m31=(y1*y5)-(y4*y2)
                m32=-((y0*y5)-(y2*y3))
                m33=(y0*y4)-(y1*y3)
                bg()
                gp()
                print(f"{botname}:| co-factor |")
                print(f'''
|     {m11}   {m12}   {m13}     | 
|     {m21}   {m22}   {m23}     |
|     {m31}   {m32}   {m33}     |''')
                bg()
                gp()
                print(f'''{bot}: | Adjoint | : 
|     {m11}   {m21}   {m31}     | 
|     {m12}   {m22}   {m32}     |
|     {m13}   {m32}   {m33}     |''')
                bg()
                gp()
                print(f'''{bot}: | Inverse |
1/{deter} |     {m11}   {m21}   {m31}     |   
          |     {m12}   {m22}   {m32}     |
          |     {m13}   {m32}   {m33}     |''')
            else:
                bg()
                gp()
                print(f"{bot}:Plz input specified input")
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot}:{username}, plz enter only integer value and try again :(")
    elif 'triang'in n:
        try:
            bg()
            gp()
            print(f"{bot} 🤖 :{username},text maximum number for u r triange 📐" )
            gp()
            l()
            n=int(eval(input(f"{user} 🤠 :")))
            l()
            bg()
            gp()
            print(f"{bot} 🤖 :here's your number triangle,{username} 😉 ")
            triange=nm(n)
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot}:{username},plz input only integer value and try again :(")
    elif 'percent' in n:
        try:
            bg()
            gp()
            print(f"{bot} 🤖 :For how many subjects {user}?")
            c1=per()      
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot}:{username}, plz enter only integer value and try again :(")         
    elif 'pyra' in n:
        b1=pyd()
    elif 'table'and'of'in n:
        try:
            mul=[]
            num=n.split(" ")
            for i in num:
                if i.isdigit():
                   mul.append(i)
            u=int(mul[0])
            bg()
            gp()
            print(f"{bot} : There you go {username}")
            gp()
            for k in range(11):
                print(f"{u} X {k} = {u*k}")
        except:
            print("PROB> :(") 
    elif 'table' in n:
        bg()
        gp()
        print(f"{bot} 🤖 :ok {username} of which table/multiples u want? plz text ony integer")
        l()
        try:
            n=float(input(f"{user} 🤠 :"))
            l()
            bg()
            gp()
            print(f"{bot} : Till which multiples {username}?")
            l()
            n7=int(eval(input(f"{user}: ")))
            l()
            bg()
            gp()
            print(f"{bot} 🤖 :Here's your table,{username} ;)")
            for i in range(1,n7):
                print(f"{n} X {i+1} = {n*(i+1)}")
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot}:{username} plz Try again by inputing real number and try again :( ")               
    elif 'spc'in n or 'stone'in n or 'paper'in n or 'scissor'in n or 'cissor'in n:
        z8=sps()
    elif 'reflex' in n:
        print(f"             | REFLEXY | ")
        bg()
        gp()
        print(f'''{bot}:Now before playing let me make u aware of rules:
1)You have to gain maximum sychronicity of letters with mine
2)The moment u fail to sychronize any letter with mine u r out then.
3)Type without seeing keyboard.
So, should we (s)Start the game or you wanna leave it ?''')
        score=[]
        gp()
        u=str(input(f"{user} :"))
        if "s" in u:
            while True:
                import random
                letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                ran=random.randint(0,len(letters)-1)
                gp()
                print(f"{bot}:Your letter -> {letters[ran]}")
                gp()
                n=str(input(f"{user} :"))
                score.append(n)
                x=int(len(score)-1) 
                y=open('c2.txt','r').read()
                z=int(y)
                if letters[ran]!=n:
                    bg()
                    gp()
                    print(f"{bot}:{username},You missed my letter, you're out.")
                    if x > z:
                        y1=open('c2.txt','w')
                        y1=y1.write(str(x))
                        bg()
                        gp()
                        score.pop(int(len(score)-1))
                        print(f'''{bot}:Hey!!! congrats {username} you broke your previous record

Previous record:{str(y)} letters
New high score :{str(x)} letters

         | LETTERS |''')           
                        for i in score:
                            print(i,end=" ")
                        print(" ")
                        break
                    elif letters[ran]==n:
                        gp()
                        print(f"{bot}:Your letter -> {letters[ran]}")    
                        for i in score:
                            print(i,end=" ")
                        print(" ")
                        break
                    elif x < z:
                        bg()
                        gp()
                        score.pop(int(len(score)-1))
                        print(f'''{bot}:Lets play again {username}
                        
current score : {x} letters
High score    : {y} letters

         | LETTERS |''')
                        for i in score:
                            print(i,end=" ")
                        print(" ")
                        break           
        elif "lea" in u:
            bg()
            gp()
            print(f"{bot} :Please play this game :)")
        else:
            bg()
            gp()
            print(f"{bot}:Plz input specified inputs.")     
    elif "edit" in n or "write" in n:
            f1=open('c1.txt','a')
            bg()
            gp()
            print(f"{bot} 🤖 :{username},input whatever text u want,and you can see ur updated text in CHATBOTT.txt")
            l()           
            n=str(input(f"{user} 🤠 :"))
            f1.write(" "+n)
            f1.close()              
    elif "read" in n:
            f=open('c1.txt','r')
            datar=f.read()
            bg()
            gp()
            print(f"{bot} 🤖 :Here it is")
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print(datar)
            f.close() 
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")         
    elif "capitalize" in n:
            bg()
            gp()
            print(f"{bot} 🤖 :{username},TEXT me to capitalize all the texts.")
            l()         
            n=str(input(f"{user} 🤠 :"))
            l()
            c=cap(n)
            bg()
            gp()
            print(f'''{bot} 🤖 :There you go {username}!
{c}''')          
    elif 'can' in n and' do' in n:
        bg()
        gp()
        print(f'''{bot} 🤖 :hey {username}!following are the tasks I can perform 🤩
        
1)I Can literally tell any table.😱

2)I Can literally tell any factorial.😱

3)I can tell multiples of any composite number till any where.😱

4)I Can literally print half wave via your name({username}) along length of your phone  ⛰️  .

5)I Can literally print right angled triangle of number till any where u say 📐.

6)I Can literally print mountain of desired height and of desired buildiing blocks ♦️ .

7)I Can summate till any where.

8)I Can give u input to write a note without acsessing notepad 🗒️.

9)I can capitalize texts 🔠.

10)I Can calculate percentage.

11)I Can play stone paper and scissor (RAHUL:type 'spc' for this ) 🗿  📰  ✂️.

12)I Can evaluate math.

13)I Can solve quadratic quration  📈📉.

14)I can make pyramid with inputed character. 🗻

15)I Can uniquify any character you input.(RAHUL:Type 'uni' for this.) 💞

16)I can solve 2x2 and 3x3 matrix's determinant,adjoint,cofactor and inverse.

17)I Can play refelxy game and increase your typing speed.

18)I can play Tic-tac-toe.

19)I Can encode and decode texts.

Ask me again {username} 🤠  if u  forget :) 
        ''')    
    elif 'evalu' in n:
        try:
            bg()
            gp()
            print(f"{bot}: Give me calculation {username}")
            gp()  
            you=str(input(f"{user}: "))
            bg()
            gp()
            print(f"{bot}: {str(you)}={eval(you)}")
        except Exception:
            bg()
            gp()
            print(f"{bot}: There was an unknown error {username}")
        pass
    elif 'multip' in n:
        try:
            bg()
            gp()
            print(f"{bot} : Now input a composite number {username} [COMPOSITE : A NUMBER WHICH IS NOT A PRIME NUMBER]")
            l()
            n5=int(eval(input(f"{user} :")))
            bg()
            gp()
            print(f"{bot} : Range ?")
            l()
            n6=int(eval(input(f"{user} :")))
            l()
            bg()
            gp()
            print(f"{bot} :Here it is {username}")
            gp()
            num=[]
            for i in range(n6+1):
                for j in range(n6+1):
                    if i*j==n5:
                        print(f"{i} x {j} = {n5}")
                        num.append(f"{i} x {j} = {n5}")
            bg()
            gp()
            print(f"{bot}:There are total {len(num)} multiples of {str(n5)} from table 1 to table {str(n6)}")
        except Exception:
            l()
            bg()
            gp()
            print(f"{bot} :Plz input composite number.")
    elif 'summat' in n:
        try:    
            bg()
            gp()
            print(f"{bot} : Till where u want to sum?")
            l()
            n=int(eval(input(f"{user} :")))
            l()
            no=[]
            for i in range(0,n+1):
                no.append(i)
            bg()
            gp()
            print(f"{bot} : ⅀ Summation from 0 to {str(n)} is {sum(no)}")
        except Exception:
            bg()
            gp()
            print(f"{bot} :Plz input integer value {username}")
    elif "new chat" in n:
        bg()
        gp()
        print(f'{bot} :What will be the key {username},Remember you can see all your new chat\'s data by texting "qna"')
        l()
        qq=str(input(f"{user}:"))
        qqs=isc()
        qqs.name=qq
        if qqs.space() is True:
            bg()
            gp()
            print(f'{bot}: And,What should I reply when you have "{qq}" in your text?')
            l()
            aq=str(input(f"{user}:"))
            aqs=isc()
            aqs.name=aq
            if aqs.space() is True:
                qa.write("_"+qq)
                ql.append(str(qq))
                aa.write("_"+aq)    
                al.append(str(aq))
            else:
                bg()
                gp()
                print(f"{bot}:{username},Plz input some values in Answer's place ")
        else:
            bg()
            gp()
            print(f"{bot}:Plz input some values in Question's place {username}")
    elif "tic" in n and "tac" in n:
        print(18*" "+"|| TIC-TAC-TOE ||")
        gp()
        print(f'{bot} :Ok then mine is "O" and your\'s is "X",You can quit the game by texting "leave" or "quit"')
        gp()
        print(f'{bot}:Now type the position of your X accordance with specified numbers from 1 to 9')
        gp()
        ####TIC TAC TOE VIA OOP###
        import random
        options=["1","2","3","4","5","6","7","8","9"]
        def checker(n):
            for opts in options:
                if opts == n:
                    return True
        pass
        pass
        def Grid():
            #11
            print(12*" "+"_"*19)
            for p in row1:
                print(p,end="  |  ")
            gp()
            for q in row2:
                print(q,end="  |  ")
            gp()
            for r in row3:
                print(r,end="  |  ")
            gp()
            print(12*" "+"¯"*19)
            
        def Replace_and_add(list,n,str,who):
            list.pop(int(who)-n)
            list.insert(int(who)-n,(str))
            pass
        def everything(who,string):
            for a in row1:
                if a in who:
                    Replace_and_add(row1,0,(string),who)
                    Grid()
            for b in row2:
                if b in who:
                    Replace_and_add(row2,3,(string),who)
                    Grid()
            for c in row3:
                if c in who:
                    Replace_and_add(row3,6,(string),who)
                    Grid()
        pass 
        row1=[" "*10,"1","2","3"]
        row2=[" "*10,"4","5","6"]
        row3=[" "*10,"7","8","9"]
        Grid()
        def onlyend():
            if breaker() is True:
                Grid()
        def breaker():
            if row1[1]==row2[1]==row3[1]:
                return True
            elif row1[2]==row2[2]==row3[2]:
                return True
            elif row1[3]==row2[3]==row3[3]:
                return True
            elif row1[1]==row2[2]==row3[3]:
                return True
            elif row1[3]==row2[2]==row3[1]:
                return True
            elif row1[1]==row1[2]==row1[3]:
                return True
            elif row2[1]==row2[2]==row2[3]:
                return True
            elif row3[1]==row3[2]==row3[3]:
                return True
            else:
                return False
        while True:
            print(("⊳")*45)
            you=str(input(f"{user}:"))
            print(("⊳")*45)
            if checker(you) is True:
                options.remove(you)
                breaker() is False==True
                if len(options)==0:
                    everything(you,"X")
                if (len(options)==0) and (breaker() is False):
                    bg()
                    gp()
                    print(f"{bot}: !!! DRAW !!!")
                    break
                if len(options)>1:
                    computer=str(random.choice(options))
                    options.remove(computer)
                    for a in row1:
                        if a in you:
                            Replace_and_add(row1,0,"X",you)
                            onlyend()  
                    for b in row2:
                        if b in you:
                            Replace_and_add(row2,3,"X",you)
                            onlyend()    
                    for c in row3:
                        if c in you:
                            Replace_and_add(row3,6,"X",you)
                            onlyend()
                    pass
                    #everything(you,"X")
                    if (breaker() is True) and (len(options)!=0):
                        fini()
                        break
                    bg()
                    gp()
                    print(f"{bot}:I will go with {computer}")
                    everything(computer,"O")
                    if (breaker() is True) and (len(options)!=0):
                        fini()
                        break
                else:
                    fini()
                    break
            elif "quit"in you:
                bg()
                gp()
                print(f"{bot}: Don't forget to review !!")
                break
            elif checker(you) is not True:
                bg()
                gp()
                print(f'{bot}: Please input within given grid !! Or text "quit/leave" to quit the game.')
        pass
    elif n1.space() is False:
        bg()
        gp()
        print(f"{bot}:Plz text something don't leave empty!")
    elif "encode" in n:
        print(f"{bot}: Now enter String to encode")
        n1=str(input(f"{user} 🤠 :"))
        decoded_text = Cesar("enc", n1)
        print(f"{bot}: Here's your decoded text -> {decoded_text}")
    elif "decode" in n:
        print(f"{bot}: Now enter String to decode")
        n1=str(input(f"{user} 🤠 :"))
        decoded_text = Cesar("dec", n1)
        print(f"{bot}: Here's your decoded text -> {decoded_text}")
    else:
        def uno(n):
            for o in ques:
                if o in str(n):
                    return True
        if uno(n) is True:
            for o in ques:
                if o in str(n):
                    bg()
                    gp()
                    print(f"{bot}:{qna.get(str(o))}")
        else:
            bg()
            gp()
            print(f"{bot}:What do you mean {username}?")