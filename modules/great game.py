import time
import sys


def space():
    print("\n")
def invalid():
    print("TRY ANOTHER COMMAND ")

def slowprint(message, speed):    #using for printing the string slowly
    for x in range(0, len(message)):     
        if x ==  len(message)-1:
            print(message[x])     
        else:
            print(message[x], end="")  #it will print index by index
            sys.stdout.flush()
            time.sleep(speed)
def call():
    while True:
        q=input("you want to examine shoes for clues or leave them ? ")
        q=q.lower()
        if "leave" in q or "ignore" in q or "donot examine" in q:
            ww=open("2nd\\ignore2.txt","r")
            slowprint(ww.read(),0.04)
            ww.close()
            space()
            time.sleep(1)
            continue
        elif "examine" in q or "investigate" in q or "inspect" in q or "check" in q:
            qq=open("2nd\\examine2.txt","r")
            slowprint(qq.read(),0.04)
            qq.close()
            space()
            time.sleep(1)
            while True:
                p=input('''where you want to Search for information about carl power's
1) Locker
2) Swiming pool''')
                p=p.lower()
                if "swiming pool" in p and not "donot search in swiming pool" in p or "2" in p:
                    o=open("2nd\\swiming.txt","r")
                    slowprint(o.read(),0.04)
                    o.close()
                    space()
                    time.sleep(1)
                    continue
                elif "locker" in p and not "donot search in locker" in p or 1 in p:
                    pp=open("2nd\\locker.txt","r")
                    slowprint(pp.read(),0.04)
                    pp.close()
                    while True:
                        i=input('''what do you think the reason could be of his death :
1) Murder
2) sucide
3) natural ''')
                        i=i.lower()
                        if "murder" in i or "killed" in i or "1" in i:
                            k=open("2nd\\killed.txt","r")
                            slowprint(k.read(),0.04)
                            k.close()
                            space()
                            time.sleep(1)
                            l=open("2nd\\1solve.txt","r")
                            slowprint(l.read(),0.04)
                            l.close()
                            greatgame2()
                            
                        elif "sucide" in i or '2' in i:
                            ss=open("2nd\\sucide.txt","r")
                            slowprint(ss.read(),0.04)
                            ss.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "natural" in i or "3" in i:
                            n=open("2nd\\natural.txt","r")
                            slowprint(n.read(),0.04)
                            n.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "quit" or "exit" in i:
                            sys.exit()
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                            
                elif "quit" in p or "exit" in p:
                    sys.exit()
                else:
                    invalid()
                    space()
                    time.sleep(1)
        elif "where" in q:
            print("still in the rooom")
            space()
            time.sleep(1)
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            
a=['Pink Iphone','gun','microscope','gloves']

def envelope():
    space()
    time.sleep(1)
    q=open("2nd\\envelop1.txt","r")
    slowprint(q.read(),0.04)
    q.close()
    while True:
        w = input("what to do now ? ")
        w = w.lower()
        if "go there" in w or "lets go" in w or "move" in w:
            space()
            time.sleep(1)
            e=open("2nd\\221c.txt","r") #opening the file
            slowprint(e.read(),0.04)
            e.close()#closing the file
            space()
            time.sleep(1)
            while True:
                r=input("What to do now ? ")
                r=r.lower()
                space()
                time.sleep(1)

                if "examine" in r or "inspect" in r:
                    t=open("2nd\\examine1.txt","r")
                    slowprint(t.read(),0.04)
                    t.close()
                    space()
                    time.sleep(1)
                    while True:
                        qq = input("Want to pick the call or not ? ")
                        qq = qq.lower()
                        if "pick it" in qq or "pick" in qq and not "donot pick" in qq or "recieve" in qq or "attend" in qq:
                            ww=open("2nd\\call.txt","r")
                            slowprint(ww.read(),0.04)
                            ww.close()
                            space()
                            time.sleep(1)
                            call()
                        elif "ignore" in qq or "donot pick" in qq:
                            ee=open("2nd\\ignore1.txt","r")
                            slowprint(ee.read(),0.04)
                            ee.close()
                            space()
                            time.sleep(1)
                        elif "lestrade" in qq or "watson" in qq:
                            print("Its better you pick the call ")
                            space()
                            time.sleep(1)
                        elif "quit" in qq or "exit" in qq:
                            sys.exit()
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                elif "leave" in r or "donot check" in r or "ignore" in r or "cannot" in r:
                    y=open("2nd\\donot1.txt","r")
                    slowprint(y.read(),0.04)
                    y.close()
                    space()
                    time.sleep(1)

                elif "where" in r:
                    print("You are in 221C in the basment of Mrs. Hudesn house.")
                    space()
                    time.sleep(1)

                elif "quit" in r or "exit" in r:
                    sys.exit()
                else:
                    invalid()
                    space()
                    time.sleep(1)

        elif "donot go" in w or " we cannot go" in w or "donot" in w:
            space()
            time.sleep(1)
            r=open("2nd\\donot.txt","r") #opening the file
            slowprint(r.read(),0.04)
            r.close() #closing the file
            space()
            time.sleep(1)

        elif "where" in w:
            
            print("you are standing in the police station")
            space()
            time.sleep(1)

        elif "quit" in w or "exit" in w:
            sys.exit()
        
        else:
            invalid()
            space()
            time.sleep(1)



def thegreatgame():
    while True:
        q=open("2nd\\great.txt","r") #reading from great in 2nd folder
        slowprint(q.read(),0.04) #calling to print character by character
        q.close()
        time.sleep(1)
        w=open("2nd\\bomb.txt","r") #getting the text
        slowprint(w.read(),0.04)
        w.close()
        while True:
            call = input("what do you want to do ? ") #input from the user
            call = call.lower()
            space()
            time.sleep(1)
            if "attend" in call or "recieve" in call or "pick call" in call:
                a=open("2nd\\attend.txt","r")
                slowprint(a.read(),0.04)
                a.close()
                space()
                time.sleep(1)
                while True:
                    d=open("2nd\\cab.txt","r")
                    slowprint(d.read(),0.04)
                    d.close()
                    space()
                    time.sleep(1)
                    while True:
                        f=input("what to do now ? ")
                        f=f.lower()
                        if "examine" in f or "inspect" in f or "open" in f:
                            g=open("2nd\\envelope.txt","r")
                            slowprint(g.read(),0.04)
                            g.close()
                            envelope()
                        elif "ignore" in f or "walk" in f or "talk" in f:
                            print("Lestrade : Sherlock inspect the envelope ")
                            space()
                            time.sleep(1)
                        elif "where" in f:
                            print("you are in the police stattion with John")
                            space()
                            time.sleep(1)
                        elif "quit" in f or "exit" in f:
                            sys.exit()
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                            
            elif "ignore" in call or "donot attend" in call or "donot recieve" in call or "donot pick" in call:
                s=open("2nd\\ignore.txt","r")
                slowprint(s.read(),0.04)
                s.close()
                space()
                time.sleep(1)
            elif "quit" in call or "exit" in call:
                sys.exit()
            else:
                invalid()
                space()
                time.sleep(1)
            
thegreatgame()
