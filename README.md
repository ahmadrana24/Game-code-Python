# Game-code-Python
Text based game code in Python. 
This is the Project of my first semester in which I coded this text based game.
# key usings
Strings.

Functions.

Loops.

File handling.

Graphical map with Turtle.

Conditions.

and much more you can explore the code.

Turtle Library.

def pink():

    while True:
        
        time.sleep(1)
        
        space()
        
        a=open("files\\pink1.txt","r")
        
        slowprint(a.read(),0.04)
        
        a.close()
        
        space()
        
        while True:
            
            do=input("what do you want to do ? ")
            
            do=do.lower()
            
            if 'look' in do:
                
                time.sleep(1)
                
                b=open("files\\looka1.txt","r")
                
                slowprint(b.read(),0.04)
                
                b.close()
                
                space()
                
                continue
                
                time.sleep(1)
            
            elif "map" in do:
                
                map()
                
                space()
                
                continue
            
            elif 'examine' in do or "inspect" in do or "detect" in do:
                
                time.sleep(1)
                
                c=open("files\\examine1.txt","r")
                
                slowprint(c.read(),0.04)
                
                c.close()
                
                space()
                
                while True:
                    
                    space()
                    
                    time.sleep(1.5)
                    
                    r=open('files\\search1.txt','r')
                    
                    slowprint(r.read(),0.04)
                    
                    r.close()
                    
                    space()
                    
                    time.sleep(1.5)
                    
                    w=input("where you want to search ? (search in street go left or right)")
                    
                    w=w.lower()
                    
                    if 'right' in w:
                        
                        time.sleep(1.5)
                        
                        space()
                        
                        q=open("files\\right1.txt","r")
                        
                        slowprint(q.read(),0.04)
                        
                        q.close()
                        
                        space()
                        
                        print("Going back to the building and standing infront of it again  ")
                        
                        time.sleep(1.5)
                    
                    elif "map" in w:
                        
                        map()
                        
                        space()
                        
                        continue
                    
                    elif 'left' in w:
                        
                        space()
                        
                        time.sleep(1.5)
                        
                        p=open("files\\left1.txt","r")
                        
                        slowprint(p.read(),0.04)
                        
                        p.close()
                        
                        time.sleep(1.5)
                        
                        space()
                        
                        while True:
                            
                            z=input("Where you want to search now ?")
                            
                            z=z.lower()
                            
                            if "gutter" in z:
                                
                                space()
                                
                                time.sleep(1.5)
                                
                                qq=open("files\\guter.txt","r")
                                
                                slowprint(qq.read(),0.04)
                                
                                qq.close()
                                
                                space()
                                
                                time.sleep(1.5)
                                
                                continue
                            
                            elif "trash" in z or "bin" in z or "garbage" in z:
                                
                                trash()
                            
                            elif "plant" in z or "green" in z or "small plants" in z:
                                
                                time.sleep(1.5)
                                
                                space()
                                
                                ee=open("files\\plant.txt","r")
                                
                                slowprint(ee.read(),0.04)
                                
                                ee.close()
                                
                                continue
                            
                            elif "all" in z or "every" in z or "them" in z:
                                
                                time.sleep(1.5)
                                
                                space()
                                
                                qq=open("files\\guter.txt","r")
                                
                                slowprint(qq.read(),0.04)
                                
                                qq.close()
                                
                                space()
                                
                                time.sleep(1.5)
                                
                                ee=open("files\\plant.txt","r")
                                
                                slowprint(ee.read(),0.04)
                                
                                ee.close()
                                
                                space()
                                
                                trash()
                            
                            elif 'quit' in z:
                                
                                sys.exit()
                            
                            elif "map" in z:
                                
                                map()
                                
                                space()
                                
                                continue
                            
                            else:
                               
                               invalid()
                               
                               continue
                    
                    else:
                        
                        space()
                        
                        invalid()
                        
                        space()
            
            elif 'walk' in do:
                
                time.sleep(1)
                
                d=open("files\\walk1.txt","r")
                
                slowprint(d.read(),0.04)
                
                d.close()
                
                space()
                
                time.sleep(1)
                
                continue
            
            elif 'where' in do:
                
                g=open("files\\where1.txt","r")
                
                slowprint(g.read(),0.04)
                
                g.close()
            
            elif 'lestrade' in do:
                
                i=open("files\\lestrade1.txt","r")
                
                slowprint(i.read(),0.04)
                
                i.close()
            
            elif "map" in do:
                
                map()
                
                space()
                
                continue
            
            elif 'quit' in do:
                
                sys.exit()
            
            else:
                
                invalid()
                
                space()
                
                continue
                
                time.sleep(1)
        
def credits(): #AHMED ASHRAF SP18-BSE-009
    
    c=open("files\\credits.txt","r")
    
    slowprint(c.read(),0.04)
    
    c.close()
    
    space()

def help(): #AHMED ASHRAF SP18-BSE-009
    
    h=open("files\\help.txt","r")
    
    slowprint(h.read(),0.04)
    
    h.close()
    
    space()
    
def play(): #AHMED ASHRAF SP18-BSE-009
    
    while True:
        
        f=open("files\\1.txt","r")
        
        slowprint(f.read(),0.04)
        
        f.close()
        
        space()
        
        while True:
            
            ride = input('''want to go with

1) Lestrade in police car

2) cab/Taxi ''')
            
            ride = ride.lower()
            
            if 'cab' in ride or 'taxi' in ride or '2' in ride:
                
                c=open("files\\cab.txt","r")
                
                slowprint(c.read(),0.04)
                
                c.close()
                
                pink()
            
            elif 'lestrade' in ride or '1' in ride:
                
                d=open("files\\lestrade.txt","r")
                
                slowprint(d.read(),0.04)
                
                d.close()
                
                space()
                
                pink()
            
            elif 'quit' in ride or 'exit' in ride :
                
                sys.exit()
            
            elif "map" in ride:
                
                map()
                
                space()
                
                continue
            
            else:
                
                space()
                
                invalid()
                
                space()
                
                time.sleep(1)
                
                continue
            
def menue(): #AHMED ASHRAF SP18-BSE-009
    
    while True:
        
        m='''PRESS 1 TO PLAY

PRESS 2 FOR HELP/INSTRUCTIONS

PRESS 3 FOR CREDITS

PRESS 4 FOR CHARACTERS

PRESS 5 FOR MAP

PRESS 6 FOR EXIT : '''
        
        menu_1 = input(m)
        
        menu_1= menu_1.lower()
        
        if '1' in menu_1 or 'play' in menu_1:
            
            space()
            
            play()
        
        elif '2' in menu_1 or 'help' in menu_1 or 'instructions' in menu_1:
            
            space()
            
            help()
        
        elif '3' in menu_1 or 'credits' in menu_1:
        
            space()
            
            credits()
        
        elif '4' in menu_1 or 'characters' in menu_1:
            
            space()
            
            time.sleep(1)
            
            aa=open('files\\characters.txt','r')
            
            slowprint(aa.read(),0.04)
            
            aa.close()
            
            space()
        
        elif '6' in menu_1 or 'quit' in menu_1 or 'exit' in menu_1:
            
            space()
            
            break
        
        elif "map" in menu_1 or '5' in menu_1:
            
            map()
            
            space()
            
            continue
        
        else:
            
            invalid()
            
            space()
            
            continue
            
def start(): #AHMED ASHRAF SP18-BSE-009
    
    a=open("files\\intro1.txt","r")
    
    slowprint(a.read(),0.04)
    
    a.close()
    
    time.sleep(0.5)
    
    b=open('files\\intro2.txt','r')
    
    slowprint(b.read(),0.04)
    
    b.close()
    
    space()
    
    menue()

start()

