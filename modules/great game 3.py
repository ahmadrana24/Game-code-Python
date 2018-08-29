import time
import sys

#AHMED ASHRAF SP18-BSE-009
def slowprint(message, speed):    #using for printing the string slowly
    for x in range(0, len(message)):     
        if x ==  len(message)-1:
            print(message[x])
        else:
            print(message[x], end="")
            sys.stdout.flush()
            time.sleep(speed)
def space(): #AHMED ASHRAF SP18-BSE-009
    print("\n")
def invalid(): #AHMED ASHRAF SP18-BSE-009
    print("TRY ANOTHER COMMAND ")

def last():
    print("The pink phone rings again ")
    space()
    while True:
        a=input("what do you want to do ?")
        a=a.lower()
        if "pick" in a or "recieve" in a or "attend" in a:
            space()
            b = open("4rth\\last.txt","r")
            slowprint(b.read(),0.000001)
            b.close()
            while True:
                c=input("Go to the complex")
                if "go" in c or "sure" in c or "yes" in c:
                    space()
                    d= open("4rth\\complex.txt","r")
                    slowprint(d.read(),0.000001)
                    d.close()
                    space()
                    e=input("Press any key to continue....")
                    space()
                    f=open("4rth\\complex2.txt","r")
                    slowprint(f.read(),0.000001)
                    f.close()
                    l=open("4rth\\complex3.txt","r")
                    slowprint(l.read(),0.000001)
                    l.close()
                    space()
                    time.sleep(2)
                    print("After few days")
                    reichenbach_fall()
                elif "no" in c or "later" in c or "leave" in c:
                    space()
                    print("You have to go to the pool to reveal who the bomber is ")
                    space()
                    time.sleep(1)
                    continue
                elif "where" in c:
                    space()
                    print("You are at your house and planing to go to the pool.")
                    space()
                    time.sleep(1)
                    continue
                elif "map" in c:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
        elif "no" in a or "ignore" in a or "no" in a:
            space()
            print("you have to pick the call its from the bomber")
            space()
            time.sleep()
            continue
        elif "map" in a:
            map()
            space()
            continue
        elif "where" in a:
            space()
            print("you are at the police station.")
            space()
            time.sleep()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
def connie2():
    a=open("4rth\\done.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    space()
    time.sleep(1)
    while True:
        b=input("would you like to tell him your deductions")
        b=b.lower()
        if "yes" in b or "sure" in b or "tell" in b or "why not" in b:
            c=open("4rth\\tell.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            e=input("press any key to continue....")
            space()
            d=open("4rth\\tell2.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            while True:
                print("You have to go to the police station to tell Lestrade")
                space()
                g=input("what do you want to do ? ")
                g=g.lower()
                if "police" in g or "lestrade" in g or "go" in g or "yes" in g or "sure" in g:
                    f=open("4rth\\police3.txt","r")
                    slowprint(f.read(),0.000001)
                    f.close()
                    space()
                    i=input("press any key to continue.....")
                    space()
                    h=open("4rth\\police4.txt","r")
                    slowprint(h.read(),0.000001)
                    h.close()
                    last()
                elif "no" in g or "later" in g:
                    space()
                    time.sleep(1)
                    continue
                elif "map" in g:
                    map()
                    space()
                    continue
                else:
                    invalid
                    space()
                    time.sleep(1)
                    continue
        elif "no" in b or "later" in b:
            space()
            print("JOHN : Sherlock you can tell me your deduction I want to hear how close I was.")
            space()
            time.sleep(1)
            continue
        elif "where" in b:
            space()
            print("At Connie Prince house")
            space()
            time.sleep(1)
            continue
        elif "map" in b:
            map()
            space()
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)

def answer():
    while True:
        a = input('''What do you reply Lestrade
1) Missing what missing ?
2) You should get more information
3) Join John and find those things''')
        a=a.lower()
        if '1' in a or "missing what missing ?" in a:
            space()
            b=open("4rth\\missing.txt","r")
            slowprint(b.read(),0.000001)
            b.close()
            space()
            time.sleep(1)
            while True:
                f = open("4rth\\deliver.txt","r")
                slowprint(f.read(),0.000001)
                f.close()
                space()
                time.sleep(1)
                g=input("What do you want to do ? ")
                if "go" in g or "sure" in g or "ok" in g or "go" in g or "home" in g:
                    space()
                    time.sleep(1)
                    h = open("4rth\\221b.txt","r")
                    slowprint(h.read(),0.000001)
                    h.close()
                    space()
                    i=input("press any key to continue....")
                    space()
                    j=open("4rth\\221b2.txt","r")
                    slowprint(j.read(),0.000001)
                    j.close()
                    time.sleep(1)
                    while True:
                        l = input("What to do now ? ")
                        l=l.lower()
                        time.sleep(1)
                        if "recieve" in l or "attend" in l or "pick it" in l or "listen" in l:
                            space()
                            m=open("4rth\\call4.txt","r")
                            slowprint(m.read(),0.000001)
                            m.close()
                            connie2()
                        elif "ignore" in l or "no" in l or "cannot" in l or "leave" in l or "later" in l:
                            space()
                            print("you cannot ignore this call its from bomber")
                            space()
                            time.sleep(1)
                            continue
                        elif "map" in l:
                            map()
                            space()
                            continue
                        elif "where" in l:
                            space()
                            print("you are at your house 221b inspecting things with lestrade")
                            space()
                            time.sleep(1)
                            continue
                        else:
                            space()
                            invalid()
                            space()
                            time.sleep(1)
                            continue
                elif "no" in g or "later" in g or "sorry" in g:
                    space()
                    print("You have to go for further investigation.")
                    space()
                    time.sleep(1)
                    continue
                elif "where" in g:
                    space()
                    k=open("4rth\\w3.txt","r")
                    slowprint(k.read(),0.000001)
                    k.close()
                    space()
                    time.sleep(1)
                    continue
                elif "map" in g:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
                             
        elif '2' in a or "you should get more information" in a:
            space()
            c=open("4rth\\find.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            time.sleep(1)
            print("So you may ask another question.")
            space()
            continue
        elif '3' in a or "join John and find those things" in a:
            space()
            d=open("4rth\\join.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            time.sleep(1)
            continue
        elif "map" in a:
            map()
            space()
            continue
        elif "where" in a:
            space()
            e=open("4rth\\w2.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue


def connie():
    a=open("4rth\\police1.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    space()
    b=input("press any key to continue....")
    space()
    c=open("4rth\\police2.txt","r")
    slowprint(c.read(),0.000001)
    c.close()
    space()
    time.sleep(1)
    while True:
        d=open("4rth\\lestrade.txt","r")
        slowprint(d.read(),0.000001)
        d.close()
        space()
        time.sleep(1)
        while True:
            e=input("Continue the examining ?")
            e=e.lower()
            if "yes" in e or "sure" in e or "continue" in e or "examine" in e:
                space()
                f=open("4rth\\further.txt","r")
                slowprint(f.read(),0.000001)
                f.close()
                space()
                i=input("press any key to continue....")
                space()
                j=open("4rth\\further2.txt","r")
                slowprint(j.read(),0.000001)
                j.close()
                space()
                time.sleep(1)
                answer()
            elif "no" in e or "not" in e or "ignore" in e:
                space()
                g=open("4rth\\ignore2.txt","r")
                slowprint(g.read(),0.000001)
                g.close()
                space()
                time.sleep(1)
                continue
            elif "where" in e:
                space()
                h=open("4rth\\w2.txt","r")
                slowprint(h.read(),0.000001)
                h.close()
                space()
                time.sleep(1)
                continue
            
            elif "map" in e:
                map()
                space()
                continue
            else:
                space()
                invalid()
                space()
                time.sleep()
                continue
    
    
def greatgame3():
    space()
    a = input("press any key to continue....")
    time.sleep(2)
    b=open("4rth\\1.txt","r")
    slowprint(b.read(),0.000001)
    b.close()
    c=input("press any key to continue....")
    d=open("4rth\\2.txt","r")
    slowprint(d.read(),0.000001)
    space()
    time.sleep(1)
    e=open("4rth\\connie.txt","r")
    slowprint(e.read(),0.000001)
    e.close()
    space()
    while True:
        f=input("what do you want to do ?")
        f=f.lower()
        if "recieve" in f or "attend" in f or "pick it" in f or "listen" in f:
            space()
            g=open("4rth\\call.txt","r")
            slowprint(g.read(),0.000001)
            g.close()
            time.sleep(1)
            space()
            h=open("4rth\\call2.txt","r")
            slowprint(h.read(),0.000001)
            h.close()
            space()
            time.sleep(1)
            while True:
                print("Phone ringing and this time it's from Lestrade")
                space()
                k=input("what do you want to do ?")
                k=k.lower()
                if "recieve" in k or "attend" in k or "pick it" in k or "listen" in k:
                    space()
                    l=open("4rth\\call3.txt","r")
                    slowprint(l.read(),0.000001)
                    l.close()
                    time.sleep(1)
                    while True:
                        space()
                        o=input('''What do you want to do:
1) Go to police station
2) eat lunch first ''')
                        o=o.lower()
                        if "eat" in o or "lunch" in o:
                            space()
                            p=open("4rth\\eat.txt","r")
                            slowprint(p.read(),0.000001)
                            p.close()
                            space()
                            time.sleep(1)
                            connie()
                        elif "go" in o or "lestrade" in o or "police" in o:
                            space()
                            q=open("4rth\\police.txt","r")
                            slowprint(q.read(),0.000001)
                            q.close()
                            space()
                            time.sleep(1)
                            connie()
                        elif "map" in o:
                            map()
                            space()
                            continue
                        elif "where" in o:
                            space()
                            r=open("4rth\\w1.txt","r")
                            slowprint(r.read(),0.000001)
                            r.close()
                            space()
                            time.sleep(1)
                            continue
                        else:
                            space()
                            invalid()
                            space()
                            time.sleep(1)
                            continue
                        
                elif "ignore" in k or "no" in k or "cannot" in k or "leave" in k or "later" in k:
                    space()
                    m=open("4rth\\ignore1.txt","r")
                    slowprint(m.read(),0.000001)
                    m.close()
                    space()
                    time.sleep(1)
                    continue
                elif "where" in k:
                    space()
                    n=open("4rth\\w1.txt","r")
                    slowprint(n.read(),0.000001)
                    n.close()
                    space()
                    time.sleep(1)
                    continue
                elif "map" in k:
                    map()
                    space()
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue

        elif "ignore" in f or "no" in f or "cannot" in f or "leave" in f or "later" in f:
            space()
            i=open("4rth\\ignore.txt","r")
            slowprint(i.read(),0.000001)
            i.close()
            space()
            time.sleep(1)
            continue
        elif "where" in f:
            space()
            j=open("4rth\\w1.txt","r")
            slowprint(j.read(),0.000001)
            j.close()
            space()
            time.sleep(1)
            continue
        elif "map" in f:
            map()
            space()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
            
greatgame3()
