import time
import sys
def invalid():
    print("INVALID COMMAND")
def space():
    print("\n")
def slowprint(message, speed):    #using for printing the string slowly
    for x in range(0, len(message)):    
        if x ==  len(message)-1:
            print(message[x])
        else:
            print(message[x], end="")
            sys.stdout.flush()
            time.sleep(speed)
            
            
            
def final1():
    while True:
        zx=open("ali\\final.txt","r")
        slowprint(zx.read(),0.04)
        zx.close()
        time.sleep(2)
        space()
        space()
        zz=open("ali\\final1.txt","r")
        slowprint(zz.read(),0.04)
        zz.close()
        time.sleep(2)
        space()
        space()
        za=open("ali\\final2.txt","r")
        slowprint(za.read(),0.04)
        za.close()
        time.sleep(2)
        space()
        space()
        zc=open("ali\\final3.txt","r")
        slowprint(zc.read(),0.04)
        zc.close()
        time.sleep(2)
        space()
        space()
        zv=open("ali\\final4.txt","r")
        slowprint(zv.read(),0.04)
        zv.close()
        time.sleep(2)
        space()
        space()
        zs=open("ali\\final5.txt","r")
        slowprint(zs.read(),0.04)
        zs.close()
        time.sleep(2)
        space()
        space()
        while True:
            j=input("Do you want to jump?")
            j=j.lower()
            if 'yes' in j:
                zl=open("ali\\final6.txt","r")
                slowprint(zl.read(),0.04)
                zl.close()
                time.sleep(2)
                space()
                space()
            elif 'no' in j:
                ze=open("ali\\final7.txt","r")
                slowprint(ze.read(),0.04)
                ze.close()
                time.sleep(2)
                space()
                space()
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue

def final():
    while True:
        f=input("Do you want to fight Jim...??")
        f=f.lower()
        if 'fight' in f or 'yes' in f:
            dd=open("ali\\fighta.txt","r")
            slowprint(dd.read(),0.04)
            dd.close()
            time.sleep(2)
            space()
            space()
            final1()
        elif 'dont' in f or 'no' in f or "don't" in f:
            dc=open("ali\\fighta1.txt","r")
            slowprint(dc.read(),0.04)
            dc.close()
            time.sleep(2)
            space()
            space()
            final1()
        else:
            invalid()
            time.sleep(2)
            space()
            space()
            continue
            
            
            
        
def kitty():
    while True:
        aa=open("ali\\kitty.txt","r")
        slowprint(aa.read(),0.04)
        aa.close()
        time.sleep(2)
        space()
        space()
        bb=open("ali\\kitty2.txt","r")
        slowprint(bb.read(),0.04)
        bb.close()
        time.sleep(2)
        space()
        space()
        while True:
            z=input("Do you want to talk to Jim??")
            z=z.lower()
            if 'yes' in z:
                gg=open("ali\\kitty3.txt","r")
                slowprint(gg.read(),0.04)
                gg.close()
                time.sleep(2)
                space()
                space()
                while True:
                    hb=open("ali\\kitty4.txt","r")
                    slowprint(hb.read(),0.04)
                    hb.close()
                    time.sleep(2)
                    space()
                    space()
                    ee=open("ali\\kitty5.txt","r")
                    slowprint(ee.read(),0.04)
                    ee.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        gd=open("ali\\dr.txt","r")
                        slowprint(gd.read(),0.04)
                        gd.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            w=input("Do you want to Talk with sherlock?")
                            w=w.lower()
                            if 'yes' in w:
                                qq=open("ali\\dr1.txt","r")
                                slowprint(qq.read(),0.04)
                                qq.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    bc=open("ali\\dr3.txt","r")
                                    slowprint(bc.read(),0.04)
                                    bc.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    sl=open("ali\\dr4.txt","r")
                                    slowprint(sl.read(),0.04)
                                    sl.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    while True:
                                        vv=open("ali\\dr5.txt","r")
                                        slowprint(vv.read(),0.04)
                                        vv.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        t=input("What to do now:?")
                                        t=t.lower()
                                        if 'chat' in t or 'talk' in t:
                                            vz=open("ali\\jump.txt","r")
                                            slowprint(vz.read(),0.04)
                                            vz.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            final()
                                            
                                        
                                        
                                        elif 'walk' in t or 'around' in t:
                                            mq=open("ali\\jump1.txt","r")
                                            slowprint(mq.read(),0.04)
                                            mq.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            final()
                                    
                                            
                                        
                                        else:
                                            invalid()
                                            time.sleep(2)
                                            space()
                                            space()
                                    
                            elif 'no' in w :
                                wr=open("ali\\dr2.txt","r")
                                slowprint(wr.read(),0.04)
                                wr.close()
                                time.sleep(2)
                                space()
                                space()
                            else:
                                invalid()
                                timesleep(2)
                                space()
                                space()
                                continue
            elif 'no' in z:
                    ss=open("ali\\kitty8.txt","r")
                    slowprint(ss.read(),0.04)
                    ss.close()
                    time.sleep(2)
                    space()
                    space()
                    kitty()
                
            else:
                    invalid()
                    time.sleep(2)
                    space()
                    space()
                    continue
            
def run():
    while True:
        az=open("ali\\run.txt","r")
        slowprint(az.read(),0.04)
        az.close()
        time.sleep(2)
        space()
        space()
        aa=open("ali\\run1.txt","r")
        slowprint(aa.read(),0.04)
        aa.close()
        time.sleep(2)
        space()
        space()
        while True:
            l=input("Do you want sherlock to run?")
            l=l.lower()
            if 'yes' in l or 'run' in l:
                hh=open("ali\\run2.txt","r")
                slowprint(hh.read(),0.04)
                hh.close()
                time.sleep(2)
                space()
                space()
                while True:
                    f=input("What to do Now")
                    f=f.lower()
                    if 'go' in f or 'walk' in  f or 'home' in f:
                        nb=open("ali\\home.txt","r")
                        slowprint(nb.read(),0.04)
                        nb.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            cc=open("ali\\sad.txt","r")
                            slowprint(cc.read(),0.04)
                            cc.close()
                            time.sleep(2)
                            space()
                            space()
                            c=input("Do you want to take the money")
                            c=c.lower()
                            if 'yes' in c:
                                az=open("ali\\home1.txt","r")
                                slowprint(az.read(),0.04)
                                az.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    rr=open("ali\\hell.txt","r")
                                    slowprint(rr.close(),0.04)
                                    rr.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    pp=open("ali\\hell1.txt","r")
                                    slowprint(pp.close(),0.04)
                                    pp.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    while True:
                                        y=input("Break-in or ring the bell?")
                                        if 'break' in y:
                                            la=open("ali\\hell2.txt","r")
                                            slowprint(la.close(),0.04)
                                            la.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            kitty()
                                        elif 'ring' in y or 'bell' in y:
                                            vv=open("ali\\hell3.txt","r")
                                            slowprint(vv.read(),0.04)
                                            vv.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            kitty()
                                        else:
                                            invalid()
                                            time.sleep(2)
                                            space()
                                            space()
                                            continue
                                            
                                        
                            elif 'no' in c:
                                dd=open("ali\\home2.txt","r")
                                slowprint(dd.close(),0.04)
                                dd.close()
                                time.sleep(2)
                                space()
                                space()
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
                    
                    
                    
            elif 'no' in l or 'dont' in l or "don't" in l:
                mn=open("ali\\run3.txt","r")
                slowprint(mn.read(),0.04)
                mn.close()
                time.sleep(2)
                space()
                space()
                
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue
def arrest():
    while True:
        ff=open("ali\\arrest.txt","r")
        slowprint(ff.read(),0.04)
        ff.close()
        time.sleep(2)
        space()
        space()
        while True:
            w=input("What to do now?:")
            w=w.lower()
            if 'go' in w:
                dd=open("ali\\arrest1.txt","r")
                slowprint(dd.read(),0.04)
                dd.close()
                time.sleep(2)
                space()
                space()
            elif 'dont' in w or "don't" in w:
                ds=open("ali\\arrest2.txt","r")
                slowprint(ds.read(),0.04)
                ds.close()
                space()
                space()
                aa=open("ali\\arrest4.txt","r")
                slowprint(aa.read(),0.04)
                aa.close()
                time.sleep(2)
                space()
                space()
                while True:
                    po=open("ali\\arrest5.txt","r")
                    slowprint(po.read(),0.04)
                    po.close()
                    time.sleep(2)
                    space()
                    space()
                    ll=open("ali\\arrest6.txt","r")
                    slowprint(ll.read(),0.04)
                    ll.close()
                    time.sleep(2)
                    space()
                    space()
                    k=input("Fight the police man..??")
                    k=k.lower()
                    if 'yes' in k or 'fight' in k:
                        jj=open("ali\\fight.txt","r")
                        slowprint(jj.read(),0.04)
                        jj.close()
                        time.sleep(2)
                        space()
                        space()
                        nn=open("ali\\fight2.txt","r")
                        slowprint(nn.read(),0.04)
                        nn.close()
                        time.sleep(2)
                        space()
                        space()
                        run()
                    elif 'no' in k or 'not' in k or 'dont' in k or "dont't" in k:
                        mm=open("ali\\fight1.txt","r")
                        slowprint(mm.read(),0.04)
                        mm.close()
                        time.sleep(2)
                        space()
                        space()
                        run()
                    else:
                        invalid()
                        time.sleep(2)
                        space()
                        space()
                        continue    
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                
def kidnap2():
    while True:
        az=open("ali\\sally.txt","r")
        slowprint(az.read(),0.04)
        az.close()
        time.sleep(2)
        space()
        space()
        aq=open("ali\\sally2.txt","r")
        slowprint(aq.read(),0.04)
        aq.close()
        time.sleep(2)
        space()
        space()
        af=open("ali\\sally3.txt","r")
        slowprint(af.read(),0.04)
        af.close()
        time.sleep(2)
        space()
        space()
        while True:
            o=input("Do you want to open the door?:")
            if 'yes' in o:
                rr=open("ali\\sally4.txt","r")
                slowprint(rr.read(),0.04)
                rr.close()
                time.sleep(2)
                space()
                space()
                arrest()
            elif 'no' in o:
                ew=open("ali\\sally5.txt","r")
                slowprint(ew.read(),0.04)
                ew.close()
                time.sleep(2)
                space()
                space()
                rr=open("ali\\sally6.txt","r")
                slowprint(rr.read(),0.04)
                rr.close()
                time.sleep(2)
                space()
                space()
                arrest()
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue
      
def addlestone():
    while True:
        df=open("ali\\addle.txt","r")
        slowprint(df.read(),0.03)
        df.close()
        time.sleep(2)
        space()
        space()
        while True:
            gg=open("ali\\addle2.txt","r")
            slowprint(gg.read(),0.03)
            gg.close()
            time.sleep(2)
            space()
            space()
            gq=open("ali\\addle3.txt","r")
            slowprint(gq.read(),0.03)
            gq.close()
            time.sleep(2)
            space()
            space()
            dd=open("ali\\taxi1.txt","r")
            slowprint(dd.read(),0.03)
            dd.close()
            time.sleep(2)
            space()
            space()
            while True:
                v=input("Aren't you feeling Hungry...!!!??")
                v=v.lower()  
                if 'yes' in v or 'hungary' in v or 'starving' in v:
                    bb=open("ali\\rest.txt","r")
                    slowprint(bb.read(),0.03)
                    bb.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        zz=open("ali\\rest2.txt","r")
                        slowprint(zz.read(),0.04)
                        zz.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnap2()
                elif 'no' in v or 'not' in v:
                    cc=open("ali\\rest1.txt","r")
                    slowprint(cc.read(),0.03)
                    cc.close()
                    time.sleep(2)
                    space()
                    space()
                    oo=open("ali\\rest3.txt","r")
                    slowprint(oo.read(),0.04)
                    oo.close()
                    time.sleep(2)
                    space()
                    space()
                    kidnap2()
                else:
                    invalid()
                    time.sleep(2)
                    space()
                    space()
                    continue
                    
def kidnapping():
    while True:
        qa=open("ali\\kidnap.txt","r")
        slowprint(qa.read(),0.03)
        qa.close()
        time.sleep(2)
        space()
        space()
        while True:
            q=input("Do you Want Dr. John to open it..??")
            if 'yes' in q or 'want' in q:
                sd=open("ali\\open.txt","r")
                slowprint(sd.read(),0.03)
                sd.close()
                time.sleep(2)
                space()
                space()
                while True:
                        qq=open("ali\\kid1.txt","r")
                        slowprint(qq.read(),0.03)
                        qq.close()
                        time.sleep(2)
                        space()
                        space()
                        er=open("ali\\asd.txt","r")
                        slowprint(er.read(),0.03)
                        er.close()
                        time.sleep(2)
                        space()
                        space()
                        az=open("ali\\kid2.txt","r")
                        slowprint(az.read(),0.03)
                        az.close()
                        time.sleep(2)
                        space()
                        space()
                        gg=open("ali\\kid3.txt","r")
                        slowprint(gg.read(),0.03)
                        gg.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            d=input("Do you Want to Sherlock to search the place?")
                            d=d.lower()
                            if 'yes' in d or 'sure' in d or 'why not' in d or 'search' in d or 'examine' in d:
                                we=open("ali\\search1.txt","r")
                                slowprint(we.read(),0.03)
                                we.close()
                                time.sleep(2)
                                space()
                                space()
                                ty=open("ali\\search2.txt","r")
                                slowprint(ty.read(),0.03)
                                ty.close()
                                time.sleep(2)
                                space()
                                space()
                                ee=open("ali\\search3.txt","r")
                                slowprint(ee.read(),0.03)
                                ee.close()
                                time.sleep(2)
                                space()
                                space()
                                pp=open("ali\\search4.txt","r")
                                slowprint(pp.read(),0.03)
                                pp.close()
                                time.sleep(2)
                                space()
                                space()
                                kk=open("ali\\search5.txt","r")
                                slowprint(kk.read(),0.03)
                                kk.close()
                                time.sleep(2)
                                space()
                                space()
                                mm=open("ali\\search6.txt","r")
                                slowprint(mm.read(),0.03)
                                mm.close()
                                time.sleep(2)
                                space()
                                space()
                                xx=open("ali\\search7.txt","r")
                                slowprint(xx.read(),0.03)
                                xx.close()
                                time.sleep(2)
                                space()
                                space()
                                cc=open("ali\\search8.txt","r")
                                slowprint(cc.read(),0.03)
                                cc.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    h=input("Do you Want Sherlock To pick wooden pieces??")
                                    h=h.lower()
                                    if 'yes' in h:
                                        hg=open("ali\\search9.txt","r")
                                        slowprint(hg.read(),0.03)
                                        hg.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        addlestone()
                                    elif 'no' in h:
                                        jn=open("ali\\search10.txt","r")
                                        slowprint(jn.read(),0.03)
                                        jn.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        addlestone()
                            elif 'no' in d or 'dont' in d or "don't" in d:
                                df=open("ali\\walks1.txt","r")
                                slowprint(df.read(),0.03)
                                df.close()
                                time.sleep(2)
                                space()
                                space()
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
def jim_mor():
    while True:
        ad=open("ali\\bribe.txt","r")
        slowprint(ad.read(),0.03)
        ad.close()
        time.sleep(2)
        space()
        space()
        while True:
            ff=open("ali\\2mon.txt","r")
            slowprint(ff.read(),0.03)
            ff.close()
            time.sleep(2)
            space()
            space()
            while True:
                aw=open("ali\\mycroft.txt","r")
                slowprint(aw.read(),0.03)
                aw.close()
                time.sleep(2)
                space()
                space()
                while True:
                    a=input("Do you want Dr. John to go??")
                    a=a.lower()
                    if 'yes' in a or 'sure' in a or 'want' in a:
                        fg=open("ali\\myc2.txt","r")
                        slowprint(fg.read(),0.03)
                        fg.close()
                        time.sleep(2)
                        space()
                        space()
                        kl=open("ali\\myc3.txt","r")
                        slowprint(kl.read(),0.03)
                        kl.close()
                        time.sleep(2)
                        space()
                        space()
                        kk=open("ali\\myc4.txt","r")
                        slowprint(kk.read(),0.03)
                        kk.close()
                        time.sleep(2)
                        space()
                        space()
                        bb=open("ali\\myc5.txt","r")
                        slowprint(bb.read(),0.03)
                        bb.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnapping()
                
                    elif 'no' in a or 'stay' in a or 'dont' in a or "don't" in a:
                        qw=open("ali\\stay.txt","r")
                        slowprint(qw.read(),0.03)
                        qw.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnapping()
                    else:
                        invalid()
                        space()
                        space()
                        time.sleep(2)
                        
def court_proceeding():
    az=open("ali\\court1.txt","r")
    slowprint(az.read(),0.03)
    az.close()
    time.sleep(2)
    space()
    space()
    while True:
        a=input("Would You like to Define Jim Moriarity?")
        a=a.lower()
        if 'yes' in a or 'sure' in a or 'why not' in a:
            aq=open("ali\\defjim.txt","r")
            slowprint(aq.read(),0.03)
            aq.close()
            time.sleep(2)
            space()
            space()
            while True:
                aa=open("ali\\judge.txt","r")
                slowprint(aa.read(),0.03)
                aa.close()
                time.sleep(2)
                space()
                space()
                while True:
                    ab=open("ali\\injail.txt","r")
                    slowprint(ab.read(),0.03)
                    ab.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        ag=open("ali\\iou.txt","r")
                        slowprint(ag.read(),0.03)
                        ag.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            c=input("Chat with Jim or first pour tea then chat?")
                            c=c.lower()
                            if 'yes' in c or 'chat' in c:
                                aw=open("ali\\chat.txt","r")
                                slowprint(aw.read(),0.03)
                                aw.close()
                                time.sleep(2)
                                space()
                                space()
                                jim_mor()
                            elif 'pour' in c or 'tea' in c or 'offer' in c:
                                af=open("ali\\chat1.txt","r")
                                slowprint(af.read(),0.03)
                                af.close()
                                time.sleep(2)
                                space()
                                space()
                                jim_mor()
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
def london_tower():
        aa=open("ali\\court.txt","r")
        slowprint(aa.read(),0.03)
        aa.close()
        time.sleep(2)
        space()
        space()
        while True:
            a=input("Do you want to search the place?")
            a=a.lower()
            if 'examine' in a or 'look around' in a or 'search' in a or 'yes' in a:
                ab=open("ali\\londontower.txt","r")
                slowprint(ab.read(),0.03)
                ab.close()
                time.sleep(2)
                space()
                space()
                while True:
                    cc=open("ali\\londontower1.txt","r")
                    slowprint(cc.read(),0.03)
                    cc.close()
                    time.sleep(2)
                    space()
                    space()
                    court_proceeding()
                    
def reichenbach_fall():
    while True:
        ab=open("ali\\abc.txt","r")
        slowprint(ab.read(),0.03)
        ab.close()
        time.sleep(2)
        space()
        space()
        while True:
            a=input("Do you want to reply back? : ")
            a=a.lower()
            if "ignore" in a or "dont reply" in a or "don't" in a or 'no' in a:
                bc=open("ali\\abc1.txt","r")
                slowprint(bc.read(),0.03)
                bc.close()
                time.sleep(2)
                space()
                space()
                london_tower()
            elif "message" in a or "reply" in a or "text" in a or 'yes' in a:
                cd=open("ali\\abc2.txt","r")
                slowprint(cd.read(),0.03)
                cd.close()
                time.sleep(2)
                space()
                space()
                london_tower()
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue
reichenbach_fall()
        
