import time
import sys

def slowprint(message, speed):    #using for printing the string slowly
    for x in range(0, len(message)):     
        if x ==  len(message)-1:
            print(message[x])
        else:
            print(message[x], end="")
            sys.stdout.flush()
            time.sleep(speed)

def space():
    print("\n")
def invalid():
    print("Try another command")
def police():
    a = open("3rd\\police.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    space()
    b=input("press any key to continue....")
    space()
    c=open("3rd\\police2.txt","r")
    slowprint(c.read(),0.000001)
    c.close()
    space()
    time.sleep(1)
    while True:
        d=input("Tell them the further assumption ?")
        d=d.lower()
        if "yes" in d or "sure" in d or "why not" in d or "tell" in d:
            space()
            e = open("3rd\\further.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
            f = input("press any key to continue....")
            space()
            g=open("3rd\\further2.txt","r")
            slowprint(g.read(),0.000001)
            g.close()
        elif "no" in d or "no" in d or "cannot" in d or "ignore" in d:
            space()
            e = open("3rd\\ignore3.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
            continue
        elif "where" in d:
            space()
            print("you are at the police car pund with watson and Lestrade to inspect the car.")
            space()
            time.sleep(1)
            continue
        elif "quit" in d or "exit" in d:
            sys.exit()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
 
def lab2():
    while True:
        print("JOHN : So what you deduced ? ")
        a=input("tell John or not ? ")
        if "tell" in a or "ok" in a or "sure" in a or "talk" in a:
            space()
            b=open("3rd\\john.txt","r")
            slowprint(b.read(),0.000001)
            b.close()
            space()
            time.sleep(1)
            while True:
                d=open("3rd\\lab.txt","r")
                slowprint(d.read(),0.000001)
                space()
                time.sleep(1)
                while True:
                    e=input("what to do ? ")
                    e=e.lower()
                    if "examine" in e or "investigate" in e or "check" in e or "look" in e:
                        space()
                        f = open("3rd\\blood.txt","r")
                        slowprint(f.read(),0.000001)
                        f.close()
                        space()
                        time.sleep(1)
                        while True:
                            i=input("attend the call ? ")
                            i=i.lower()
                            if "yes" in i or "sure" in i or "ok" in i or "attend" in i or "recieve" in i:
                                space()
                                j=open("3rd\\blood2.txt","r")
                                slowprint(j.read(),0.000001)
                                j.close()
                                space()
                                time.sleep(1)
                                police()
                            elif "no" in i or "donot" in i or "cannot" in i or "later" in i:
                                space()
                                k=open("3rd\\ignore2.txt","r")
                                slowprint(k.read(),0.000001)
                                k.close()
                                space()
                                time.sleep(1)
                                continue
                            elif "where" in i:
                                space()
                                l=open("3rd\\w3.txt","r")
                                slowprint(l.read(),0.000001)
                                l.close()
                                space()
                                time.sleep(1)
                                continue
                            elif "quit" in i or "exit" in i:
                                sys.exit()
                            else:
                                space()
                                invalid()
                                space()
                                time.sleep(1)
                                continue
                            
                    elif "donot" in e or "no" in e or "cannot" in e or "ignore" in e:
                        space()
                        g=open("3rd\\ignore1.txt","r")
                        slowprint(g.read(),0.000001)
                        g.close()
                        space()
                        time.sleep(1)
                        continue
                    elif "where" in e:
                        space()
                        h=open("3rd\\w2.txt","r")
                        slowprint(h.read(),0.000001)
                        h.close()
                        space()
                        time.sleep(1)
                        continue
                    elif "quit" in e or "exit" in e:
                        sys.exit()
                    else:
                        space()
                        invalid()
                        space()
                        time.sleep(1)
                        continue
                    
        elif "no" in a or "donot" in a or "cannot" in a or "later" in a:
            space()
            c=open("3rd\\john1.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            time.sleep(1)
            continue
        elif "quit" in a or "exit" in a:
            sys.exit()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
    
def scene():
    a=open("3rd\\scene.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    while True:    
        b=input("what to do now ?")
        b=b.lower()
        if "examine" in b or "investigate" in b or "check" in b or "ok" in b:
            c=open("3rd\\check.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            time.sleep(1)
            space()
            while True:
                q=input("talk to Mrs. Monkford or not ?")
                q=q.lower()
                if "talk" in q or "yes" in q or "sure" in q:
                    w=open("3rd\\mrs.txt","r")
                    slowprint(w.read(),0.000001)
                    w.close()
                    space()
                    t=open("3rd\\mrs2.txt","r")
                    slowprint(t.read(),0.000001)
                    t.close()
                    space()
                    time.sleep(1)
                    while True:
                        print("you have to go the JANUS cars for further investigation")
                        f=input("what to do now ?")
                        f=f.lower()
                        if "janus" in f or "go" in f or "ok" in f or "cab" in f:
                            print("you arrive at JANUS cars and goes to the manager's office.")
                            while True:
                                g=input("what to do now ?")
                                g=g.lower()
                                if "investigate" in g or "ask" in g or "examine" in g:
                                    A=open("3rd\\janus.txt","r")
                                    slowprint(A.read(),0.000001)
                                    A.close()
                                    space()
                                    time.sleep(1)
                                    Z=input("press any key to continue ....")
                                    space()
                                    time.sleep(1)
                                    B=open("3rd\\janus2.txt","r")
                                    slowprint(B.read(),0.000001)
                                    B.close()
                                    space()
                                    time.sleep(1)
                                    lab2()
                                elif "no" in g or "donot" in g or cannot in g or "later" in g:
                                    space()
                                    print("you have to investigate him.")
                                    space()
                                    time.sleep(1)
                                    continue
                                elif "where" in g:
                                    space()
                                    ii=open("3rd\\w.txt","r")
                                    slowprint(ii.read(),0.000001)
                                    ii.close()
                                    space()
                                    ttime.sleep(1)
                                    continue
                                elif "quit" in g or "exit" in g:
                                    sys.exit()
                                else:
                                    space()
                                    print("You have to in vestigate him.")
                                    space()
                                    invalid()
                                    space()
                                    time.sleep(0.000001)
                                    continue
                        elif "donot" in f or "no" in f or "cannot" in f or "later" in f:
                            pp=open("3rd\\no2.txt","r")
                            slowprint(pp.read(),0.000001)
                            pp.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "where" in f:
                            yy=open("3rd\\sea.txt","r")
                            slowprint(yy.read(),0.000001)
                            s.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "quit" in f or "exit" in f:
                            sys.exit()
                        else:
                            invalid()
                            sapce()
                            time.sleep(1)
                            continue

                elif "no" in q or "cannot" in q or "leave" in q or "not" in q:
                    r=open("3rd\\no.txt","r")
                    slowprint(r.read(),0.000001)
                    r.close()
                    space()
                    time.sleep(1)
                    continue
                elif "where" in q:
                    s=open("3rd\\sea.txt","r")
                    slowprint(s.read(),0.000001)
                    s.close()
                    space()
                    time.sleep(1)
                    continue
                elif "quit" in q or "exit" in q:
                    sys.exit()
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
        elif "lestrade" in b: 
            space()
            c=open("3rd\\lestrade3.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            time.sleep(1)
            continue
        elif "watson" in b:
            d=open("3rd\\watson.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            time.sleep(1)
            continue
        elif "where" in b:
            e=open("3rd\\sea.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
            continue
        elif "quit" in b or "exit" in b:
            sys.exit()
        else:
            invalid()
            space()
            time.sleep(1)
            continue
        
def call2():
    a=open("3rd\\call4.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    space()
    time.sleep(1)
    b=open("3rd\\call5.txt","r")
    slowprint(b.read(),0.000001)
    b.close()
    space()
    while True:
        c=input("Ask lestrade about the missing car ? ")
        c=c.lower()
        if "yes" in c or "ask him" in c or "talk to him" in c:
            d=open("3rd\\lestrade.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            time.sleep(1)
            scene()
        elif "no" in c or "donot" in c or "ignore" in c or "cannot" in c:
            e = open("3rd\\lestrade2.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
        elif "quit" in c or "exit" in c:
            sys.exit()
        elif "where" in c:
            print("you are at the police station with Watson and Lestrade")
            space()
            time.sleep(1)
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            continue
    
def message2():
    a=open("3rd\\car.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    while True:
        b=input("you want to pick the phone ? ")
        b=b.lower()
        if "pick the call" in b or "attend" in b or "recieve" in b or "pick it" in b or "pick call" in b:
            c=open("3rd\\call1.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            time.sleep(1)
            call2()
        elif "no" in b or "ask lestrade" in b or "ask watson" in b or "donot" in b or "cannot" in b:
            d=open("3rd\\call2.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            time.sleep(1)
            call2()
        elif "watson" in b or "ask watson" in b:
            e=open("3rd\\call3.txt","r")
            slowprint(e.read(),0.000001)
            e.close()
            space()
            time.sleep(1)
            call2()
        elif "quit" in b or "exit" in b :
            sys.exit()
        else:
            invalid()
            space()
            time.sleep(1)
            

#Ahmed ashraf
def greatgame2(): #3rd case
    a=open("3rd\\1.txt","r")
    slowprint(a.read(),0.000001)
    a.close()
    e=open("3rd\\2.txt","r")
    slowprint(e.read(),0.000001)
    e.close()
    space()
    time.sleep(1)
    while True:
        b=input("LESTRADE : lets have a cup of tea ")
        b=b.lower()
        if "drink" in b or "ok" in b or "sure" in b or "why not" in b or "yes" in b:
            c=open("3rd\\tea.txt","r")
            slowprint(c.read(),0.000001)
            c.close()
            space()
            time.sleep(1)
            message2()
        elif "no" in b or "not now" in b or "never" in b or "cannot" in b or "later" in b:
            d=open("\\ignore.txt","r")
            slowprint(d.read(),0.000001)
            d.close()
            space()
            time.sleep(1)
            message2()
        elif "quit" in b or "exit" in b:
            sys.exit()
        else:
            invalid()
            space()
            time.sleep(1)
    
greatgame2()